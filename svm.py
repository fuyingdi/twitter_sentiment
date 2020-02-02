import pandas
import sklearn
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.metrics import accuracy_score
import random

test_data = []
train_data = list(map(lambda kv:(int(kv[0]),kv[1]), [line.split(', ') for line in open("test_out.dat")]))
pick_index = open('__rand_pick').read().split(',')[:-1]
[test_data.append(train_data[int(i)]) for i in pick_index]
train_data = [a for i,a in enumerate(train_data) if str(i) not in pick_index]
# for i in range(100):
#     index = random.randint(0,400)
#     test_data.append(train_data[index])
#     del(train_data[index])
train_scores = list([a[0] for a in train_data])
train_tweets = list([a[1] for a in train_data])

# test_data = list(map(lambda kv:(int(kv[0]),kv[1]), [line.split(', ') for line in open("test_out.dat")]))
test_tweets = list([a[1] for a in test_data])
test_scores = list([a[0] for a in test_data])

vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(train_tweets).toarray()

clf = svm.SVC(kernel='rbf', C=1)
clf.fit(x, train_scores)
# print(clf)

v = vectorizer.transform(test_tweets).toarray()
res = clf.predict(v)
_res = clf.predict(v)

miss = 0
out_res = [0,0,0]
for i,score in enumerate(list(_res)):
    out_res[int(score/2)] += 1
    # print(str(i)+':'+str(score) + ' ' + str(test_scores[i]))
    if score!=test_scores[i]:
        miss+=1
print("@SVM:miss {}/{}, hit rate:{}%".format(miss, len(list(_res)), 100-100*miss/len(list(_res))))
with open('__svm', 'w+') as file:
    [file.write(str(i)+',') for i in out_res]
    file.write(str(100-miss))
