import numpy as np
class Perceptron:
    def __init__(self, input_size, lr=0.1, epochs=10):
        self.weights = np.zeros(input_size)
        self.bias = 0
        self.lr = lr
        self.epochs = epochs

    def activation(self, x):
        return 1 if x > 0 else 0
        # This is threshold activation function

    def predict(self, x):
        linear_output = np.dot(x, self.weights) + self.bias
        return self.activation(linear_output)

    def fit(self, X, y):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                prediction = self.predict(xi)
                error = target - prediction
                # Update weights and bias
                self.weights += self.lr * error * xi
                self.bias += self.lr * error

X = np.array([[0.5],[0.3],[0.2], [0.68]])
y = np.array([1, 0, 0, 1])

print("Training Data:")
for i in range(len(X)):
    print(f"Point {X[i]}: Label {y[i]}")

print("-----------------------------------------")
perceptron = Perceptron(input_size=1, lr=0.1, epochs=20)
perceptron.fit(X, y)

# Test predictions
test_points = np.array([[0.54], [0.89], [0.3]])
for point in test_points:
    print(f"Point {point} classified as: {perceptron.predict(point)}")
