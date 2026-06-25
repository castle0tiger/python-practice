from sklearn.tree import DecisionTreeClassifier
import pandas as pd

data = {
    "공부시간": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "출석률":   [50, 60, 55, 70, 80, 75, 90, 85, 95, 100],
    "합격여부": [0, 0, 0, 0, 1, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["공부시간", "출석률"]]
y = df["합격여부"]

model = DecisionTreeClassifier()
model.fit(X, y)

result = model.predict(pd.DataFrame([[10, 50]], columns=["공부시간", "출석률"]))
print("합격" if result[0] == 1 else "불합격")

for feature, importance in zip(["공부시간", "출석률"], model.feature_importances_):
    print(f"{feature}: {importance:.2f}")



from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model2 = DecisionTreeClassifier()
model2.fit(X_train, y_train)

y_pred = model2.predict(X_test)
print(f"정확도: {accuracy_score(y_test, y_pred) * 100:.1f}%")
