import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 8, 10])

model = LinearRegression()
model.fit(x, y)

predictions = model.predict(x)

plt.scatter(x, y)
plt.plot(x, predictions)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Linear Regression")
plt.show()