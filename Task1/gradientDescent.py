import numpy as np
import math


def gradient_descent(function, initial):
    def find_grad():
        x = np.zeros(number)
        x[:] = initial

        for i in range(initial.size):
            x[i] = initial[i] + h
            grad[i] = (function(x) - function(initial))/h
            x[i] = initial[i]

    def choose_step(step):
        status2 = 1
        step1 = step
        while status2==1:
            if (function(initial - grad * step1) > (function(initial) - eps*step*math.sqrt(np.dot(grad,grad)))):
                step1 *= delta
            else:
                status2 = 0
        return step1
    eps = 0.1
    delta = 0.5
    h = 0.0001
    step = 0.01
    number = initial.shape[0]
    grad = np.zeros(number)
    status = 1
    while status != 0:
        find_grad()
        step = choose_step(step)
        initial = initial - grad * step
        #print step
        if np.all(grad*step <= 0.001) and np.all(grad*step >= -0.001):
            status = 0
    norma = map(lambda x: x*x, initial)
    norma = math.sqrt(reduce(lambda x, y: x+y, norma))
    return initial/norma
