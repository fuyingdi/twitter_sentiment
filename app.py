import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os
import random
import sys


afinn_res=[]
nbayes_res=[]
svm_res=[]
true_res=[0,0,0]

afi_rate = 0
nby_rate = 0
svm_rate = 0

def run():
    sns.set(style="whitegrid")

    with open('__rand_pick', 'w+') as rand:
        _ = list(range(497))
        random.shuffle(_)
        [rand.write(str(_[i])+',') for i in range(100)]

    data = list(map(lambda k:(int(k[0]), k[1]), [line.split(', ') for line in open('test_out.dat')]))
    pick_index = open('__rand_pick').read().split(',')[:-1]
    pick_data = []
    # print(len(data))
    # [print(a) for a in afinn]
    [pick_data.append(data[int(i)]) for i in pick_index]
    data = pick_data
    content = [a[1] for a in data]
    true_score = [a[0] for a in data]

    for i in true_score:
        true_res[int(i/2)]+=1
    # print(true_res)
        

    print('---')
    os.system('python3 afinn.py')
    os.system('python3 svm.py')
    os.system('python3 naive_bayes.py')
    # print('===')

def out():
    afinn_res = [int(i) for i in open('__afi').read().split(',')[:3]]
    nbayes_res = [int(i) for i in open('__nby').read().split(',')[:3]]
    svm_res = [int(i) for i in open('__svm').read().split(',')[:3]]
    data = {'class': ['nag','mid','pos','nag','mid','pos','nag','mid','pos','nag','mid','pos'], 'count': [],'algorithm':['afinn','afinn','afinn','nbayes','nbayes','nbayes','svm','svm','svm','true','true','true']}
    data['count'] = afinn_res + nbayes_res + svm_res + true_res
    # print(data)
    df = pd.DataFrame.from_dict(data)
    # print(df)

    plt.figure(figsize=(12, 6))
    g = sns.catplot(x="class", y="count", hue="algorithm", data=df,
                    height=6, kind="bar", palette="muted")
    plt.savefig('out.png')

if __name__ == '__main__':
    if len(sys.argv)>1:
        for i in range(int(sys.argv[1])):
            run()
            _afinn_res = open('__afi').read().split(',')[3]
            _nbayes_res = open('__nby').read().split(',')[3]
            _svm_res = open('__svm').read().split(',')[3]
            afi_rate += int(_afinn_res)
            nby_rate += int(_nbayes_res)
            svm_rate += int(_svm_res)
        afi_rate/=int(sys.argv[1])
        svm_rate/=int(sys.argv[1])
        nby_rate/=int(sys.argv[1])
        print('\n\n======')
        print('@AFINN: avg rate:{}%'.format(afi_rate))
        print('@SVM: avg rate:{}%'.format(svm_rate))
        print('@N-BAYES: avg rate:{}%'.format(nby_rate))
        print('======')
        

    else:
        run()
        out()