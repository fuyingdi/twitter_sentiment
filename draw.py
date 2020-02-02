import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set(style="whitegrid")

afinn_res = [1,2,3]
nbayes_res = [1,2,3]
svm_res = [1,2,3]
data = {'class': [0,2,4,0,2,4,0,2,4], 'count': [],'algorithm':['afinn','afinn','afinn','nbayes','nbayes','nbayes','svm','svm','svm']}
data['count'] = afinn_res + nbayes_res + svm_res
print(data)
df = pd.DataFrame.from_dict(data)
print(df)

plt.figure(figsize=(12, 6))

# Draw a nested barplot to show survival for class and sex
g = sns.catplot(x="class", y="count", hue="algorithm", data=df,
                height=6, kind="bar", palette="muted")
# g.despine(left=True)
# g.set_ylabels("survival probability")
plt.savefig('test_out.png')

