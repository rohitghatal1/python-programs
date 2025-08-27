import numpy as np
import matplotlib.pyplot as plt

class UnivariateLinearRegression():
    def _init_(self, lr=0.01, n_iters=500):
        self.weight = 0.0
        self.bias = 0.0
        self.lr = lr
        self.n_iters = n_iters
        self.loss_history = []
        self.weight_history = []
        self.bias_history = []

    def MSE_loss(self, y_pred, y):
        m = y.shape[0]
        loss = (1/(2*m)) * np.sum((y_pred - y) ** 2)
        return loss
    
    def gradient_descent(self, X, y, y_pred):
        m = y.shape[0]
       
        d_w = (1/m) * np.dot(X.T, (y_pred - y))

        d_b = (1/m) * np.sum((y_pred - y))

        self.weight -= self.lr * d_w
        self.bias -= self.lr * d_b
    
    def fit(self, X, y):
        X = X.reshape(-1,1)
        y = y.reshape(-1,1)

        for i in range(self.n_iters):
            y_pred = self.weight * X + self.bias
            loss = self.MSE_loss(y_pred, y)

            self.loss_history.append(loss)
            self.weight_history.append(self.weight)
            self.bias_history.append(self.bias)

            if i % 100 == 0:
                print(f"Iteration {i}, MSE Loss = {loss:.6f}")
            
            return self
        
    def predict(self, X):
        X = X.reshape(-1, 1)
        return self.weight * X + self.bias

    