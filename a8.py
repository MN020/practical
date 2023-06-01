import seaborn as sns
df = sns.load_dataset('titanic');
df.head()

sns.jointplot(data=df,x='fare',y='age')

sns.histplot(data=df,x='fare',kde=True)