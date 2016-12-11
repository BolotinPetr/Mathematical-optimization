import numpy as np
import math


def gradient_descent(function, initial, accuracy, gradQ):
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
    delta = 0.1
    h = 0.000000001
    step = 0.01
    number = initial.shape[0]
    grad = np.zeros(number)
    status = 1
    counter = 0
    while status != 0:
        counter += 1
        grad = gradQ(initial)
        step = choose_step(step)
        initial = initial - grad * step
        print grad, step
        if np.all(grad*step <= accuracy) and np.all(grad*step >= -accuracy):
            status = 0
    norma = map(lambda x: x*x, initial)
    norma = math.sqrt(reduce(lambda x, y: x+y, norma))
    print counter, grad
    return initial/norma, counter
