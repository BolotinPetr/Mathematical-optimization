import math
import numpy as np
from scipy.optimize import newton_krylov, anderson, root, fsolve
from numpy import linalg as lin


class CentralPathMethod:
    def __init__(self, param):
        self.u, self.e1, self.e2, self.e3, self.e4 = param[0], param[1], param[2], param[3], param[4]
        print 'initiated'

    def fit(self, c, A, b):
        self.c = c
        self.A = A
        self.b = b
        self.n = self.c.shape[0]
        self.m = self.b.shape[0]

    def F(self, x, x_s, y, y_s):
        F_1 = np.dot(self.A, x) + x_s - self.b
        F_2 = np.dot(self.A.T, y) - y_s - self.c
        F_3 = np.dot(np.dot(np.diag(x), np.diag(y_s)), np.ones([self.c.size])) - self.u*np.ones(self.c.size)
        F_4 = np.dot(np.dot(np.diag(y), np.diag(x_s)), np.ones([self.b.size])) - self.u*np.ones(self.b.size)
        return np.concatenate((F_1, F_2, F_3, F_4))

    def J(self, x, x_s, y, y_s):
        n = x.size
        m = x_s.size
        result = [
                np.array(np.concatenate((self.A, np.eye(m), np.zeros([m, m]), np.zeros([m, n])), axis = 1)),
                np.array(np.concatenate((np.zeros([n, n]), np.zeros([n, m]), self.A.T, -np.eye(n)), axis = 1)),
                np.concatenate((np.diag(y_s), np.zeros([n, m]), np.zeros([n, m]), np.diag(x)), axis = 1),
                np.concatenate((np.zeros([m, n]), np.diag(y), np.diag(x_s), np.zeros([m, n])), axis = 1)
            ]
        return np.concatenate((result), axis = 0)

    def solve_F(self):
        A, b, c = self.A, self.b, self.c
        epsilon = 0.01
        n = self.n
        m = self.m

        x_k = np.ones(2*(n+m))
        k = 0
        while 1:
            k += 1
            tau = 1.
            x = x_k[0:n]
            x_s = x_k[n:n+m]
            y = x_k[n+m:n+m+m]
            y_s = x_k[n+m+m:n+n+m+m]

            F = self.F(x, x_s, y, y_s)

            if (lin.norm(F) < epsilon) or k > 100:
                return x_k

            J_F_inv = lin.inv(self.J(x, x_s, y, y_s))
            koef = np.dot(F, J_F_inv.T)

            x_k1 = x_k - koef*tau

            while (x_k1 < 0).any():
                x_k1 = x_k - koef*tau
                tau /= 2.

            tmp = np.copy(x_k1)
            x_k = np.copy(tmp)

    def method(self):
        x = self.solve_F()
        k = 0
        k_max = 10000
        path = []
        n, m = self.n, self.m
        while 1:
            k += 1
            x_prev = np.copy(x)
            self.u /= 10.
            x = self.solve_F()
            #path.append(x)
            if ((lin.norm(x_prev[0:n] - x[0:n]) < self.e1 and lin.norm(x_prev[n:n+m] - x[n:n+m]) < self.e2
                and lin.norm(x_prev[n+m:n+m+m] - x[n+m:n+m+m]) < self.e3
                and lin.norm(x_prev[n+m+m:n+n+m+m] - x[n+m+m:n+n+m+m]) < self.e4)
                or (k > k_max)):
                return x