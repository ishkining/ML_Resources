import library as tf
import numpy as np


def model(x): return 1.23 * x + 4


train_X = np.linspace(0, 50, 50).reshape((-1, 1))
train_Y = np.array([model(x) for x in train_X]).reshape((-1, 1))

print(train_Y)

X = np.array([0.4])
w = np.array([[0.4, 0.1, 0.2]])
b = np.array([[0.4, 0.1, 0.2]]).T

print(X.shape, w.shape)
print(X.dot(w))
