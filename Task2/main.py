import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.optimize import minimize
import gradientDescent as grad


def gen_data(dispersion, y_true):
    y_random = np.array([element + random.gauss(0, dispersion) for element in y_true])
    return y_random


def function(t, a):
    return np.array([a[0]*np.sin(coordinate) + a[1]*coordinate + a[2] for coordinate in t])


def error_square(y1, y2):
    b = (y1-y2)**2
    error = reduce(lambda x, y: x+y, b)
    return error


def error_modulus(y1, y2):
    a = reduce(lambda x, y: x + y, abs(y1 - y2))
    return a


def error_max_modulus(y1, y2):
    a = np.max(abs(y1 - y2))
    return a


def solve_problem_by(error_function, y_rand):
    def general_error(a):
        m = 200.0
        t = np.array([i*10.0/m for i in range(int(m))])
        y_test = function(t, a)
        return error_function(y_test, y_rand)
    initial = np.array([1, 1, 1])
    result = minimize(general_error, initial, method='nelder-mead')
    return result.x


def find_errors(y_rand):
    a_square = solve_problem_by(error_square, y_rand)
    y_square = function(t, a_square)
    a_modulus = solve_problem_by(error_modulus, y_rand)
    y_modulus = function(t, a_modulus)
    a_max_modulus = solve_problem_by(error_max_modulus, y_rand)
    y_max_modulus = function(t, a_max_modulus)
    #print a_square, a_modulus, a_max_modulus
    plt.plot(t, y_rand, color = 'blue')
    plt.plot(t, y_square, color = 'red')
    plt.plot(t, y_modulus, color = 'green')
    plt.plot(t, y_max_modulus, color = 'orange')
    plt.plot(t, y_true, color = 'black')
    #plt.ylim(0, 10)
    #plt.show()
    #error1, error2, error3 = error_square(y_square, y_true),\
                             #error_modulus(y_modulus, y_true), error_max_modulus(y_max_modulus,y_true)
    #return error1, error2, error3


a_true = np.array([2, 1, 3])
m = 200.0
t = np.array([i*10.0/m for i in range(int(m))])
y_true = function(t, a_true)
#y_rand[30] = y_rand[0]+50
#print find_errors()


