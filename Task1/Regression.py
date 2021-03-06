import gradientDescent as grad
import math
import numpy as np


class LogisticRegression:
    def __init__(self):
        self.number = 0

    def fit(self, train_data):
        self.row_number = train_data.shape[0]
        self.column_number = train_data.shape[1]
        self.train = np.hsplit(train_data, (0, self.column_number-1))[1]
        self.target = np.hsplit(train_data, (0, self.column_number-1))[2]

    def gradQ(self, w):
        grad = np.zeros(len(w))
        for i in range(len(w)):
            grad_i = 0
            for j in range(self.train.shape[0]):
                M = -1 * self.target[j][0] * np.dot(w, self.train[j])
                grad_i += np.exp(M) / (1 + np.exp(M)) * -1 * self.target[j][0] * self.train[j][i]
            grad[i] = grad_i
        return grad

    def Q(self, w):
        s = 0
        for i in range(self.row_number):
            power = -1*self.target[i][0]*np.dot(w, self.train[i][:])
            s = s + math.log((1+math.exp(power)), math.e)
        return s

    def find_weights(self, initial_weights, accuracy):
        return grad.gradient_descent(self.Q, initial_weights, accuracy, self.gradQ)



