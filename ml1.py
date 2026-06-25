from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
y = np.array([40, 50, 58, 72, 75, 85, 90, 95])

model = LinearRegression()
model.fit(X, y)

predicted = model.predict([[9]])
print(f"공부시간 9시간 → 예상 점수: {predicted[0]:.1f}점")


import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

plt.scatter(X, y, color="blue", label="실제 데이터")
plt.plot(X, model.predict(X), color="red", label="예측선")
plt.xlabel("공부시간")
plt.ylabel("점수")
plt.title("선형 회귀")
plt.legend()
plt.show()
