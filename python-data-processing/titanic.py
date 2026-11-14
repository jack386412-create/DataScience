from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(Path(__file__).parent / 'train.csv')


df['Age'] = df['Age'].fillna(df['Age'].median())


df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])


df['Cabin'] = df['Cabin'].fillna('Unknown')

print("=== [데이터 요약 1] 객실 등급(Pclass)별 평균 생존율 ===")
groupby_summary = df.groupby('Pclass')[['Survived']].mean()
print(groupby_summary, "\n")


print("=== [데이터 요약 2] 성별 및 Pclass별 평균 생존율 교차 분석 ===")
pivot_summary = pd.pivot_table(df, values='Survived', index='Sex', columns='Pclass', aggfunc='mean')
print(pivot_summary, "\n")


plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(1, 2, figsize=(14, 6))


sns.barplot(x='Pclass', y='Survived', hue='Sex', data=df, ax=axes[0], palette='pastel')
axes[0].set_title('Survival Rate by Pclass and Sex', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Mean Survival Rate')


sns.histplot(data=df, x='Age', hue='Survived', multiple='stack', bins=30, ax=axes[1], palette='Set2')
axes[1].set_title('Age Distribution by Survival', fontsize=14, fontweight='bold')
axes[1].set_ylabel('Count')

plt.tight_layout()


plt.savefig('titanic_visualizations.png', dpi=300)
plt.show()