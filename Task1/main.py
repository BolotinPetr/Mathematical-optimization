import numpy as np
import Regression as reg
import pylab as pb
from scipy.optimize import minimize
import math
import support


def main(Expected1, Expected2, Dispersion1, Dispersion2, Number1, Number2, accuracy):
    fig = pb.figure()
    data, axes = support.gen_data1(Expected1, Expected2, Dispersion1, Dispersion2, Number1, Number2, fig)
    l_regression = reg.LogisticRegression()
    l_regression.fit(data)

    weights_by_grad = np.zeros(Expected1.shape[0]+1)
    weights_by_grad, N = l_regression.find_weights(weights_by_grad, accuracy)

    weights_by_scipy = np.zeros(Expected1.shape[0]+1)
    weights_by_scipy = minimize(l_regression.Q, weights_by_scipy, method='nelder-mead')

    norma2 = map(lambda x: x*x, weights_by_scipy.x)
    norma2 = math.sqrt(reduce(lambda x, y: x+y, norma2))
    weights_by_scipy.x /= norma2

    #print weights_by_grad, weights_by_scipy.x

    support.draw(weights_by_grad, 'black', axes)
    support.draw(weights_by_scipy.x, 'yellow', axes)
    pb.show()
    return N

Expected1 = np.array([1, 4])
Expected2 = np.array([4, 3])
Dispersion1 = 1
Dispersion2 = 1.5
Number1 = 20
Number2 = 20
accuracy = 0.001
print main(Expected1, Expected2, Dispersion1, Dispersion2, Number1, Number2, accuracy)