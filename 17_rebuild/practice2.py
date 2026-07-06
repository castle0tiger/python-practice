import pandas as pd

df = pd.read_csv("17_rebuild/students.csv")
print(df)

print(f"평균: {df['score'].mean()}")

high_scores = df[df["score"] >= 80]
print(high_scores)

print("\n")
print(df["score"])