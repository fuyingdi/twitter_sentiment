import random

afinn = dict(map(lambda kv:(kv[0],int(kv[1])), [ line.split('\t') for line in open("AFINN-111.txt") ]))
data = list(map(lambda k:(int(k[0]), k[1]), [line.split(', ') for line in open('test_out.dat')]))
pick_index = open('__rand_pick').read().split(',')[:-1]
pick_data = []
# [print(a) for a in afinn]
[pick_data.append(data[int(i)]) for i in pick_index]
data = pick_data

# def drop(data):
#     del data[random.randint(0,100)]

# [drop(data) for i in range(400)] # random drop

content = [a[1] for a in data]
true_score = [a[0] for a in data]

def judge(_str):
    res = 0
    edge = 0
    for word in list(_str.split(' ')):
        if afinn.get(word):
            res+=afinn[word]
        else:
            continue
    if abs(res)<=edge:
        res = 2
    elif res>edge:
        res = 4
    elif res<-edge:
        res = 0
    return res
            
predict_score = map(judge ,content)
# print(predict_score)
hit = 0
miss = 0
out_res =[0,0,0]
for i, score in enumerate(predict_score):
    out_res[int(score/2)] += 1
    if score == true_score[i]:
        # print("hit")
        hit+=1
    else:
        # print("miss")
        miss+=1

print("@AFINN:hit:{}/100, hit rate:{}%".format(hit, 100*hit/(100)))

with open('__afi', 'w+') as file:
    [file.write(str(i)+',') for i in out_res]
    file.write(str(100-miss))