import seaborn as sns

df = sns.load_dataset('titanic')
df.head()

sns.boxplot(data=df,x='sex',y='age',hue='survived')