import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
from matplotlib import cm
import pylab as pb
from mpl_toolkits.mplot3d import Axes3D


def gen_data1(e_value1, e_value2, disp1, disp2, number1, number2, fig):
    class1 = np.zeros(number1) - 1
    last_column1 = np.zeros(number1) + 1
    class2 = np.zeros(number2) - 1
    last_column2 = np.zeros(number2) - 1
    for i in e_value1:
        column = rand.normal(i, disp1, number1)
        class1 = np.column_stack((class1, column))
    class1 = np.column_stack((class1, last_column1))
    for i in e_value2:
        column = rand.normal(i, disp2, number2)
        class2 = np.column_stack((class2, column))
    class2 = np.column_stack((class2, last_column2))
    x1 = class1[:, 1]
    y1 = class1[:, 2]
    x2 = class2[:, 1]
    y2 = class2[:, 2]
    if class1.shape[1] > 4:
        z1 = class1[:, 3]
        z2 = class2[:, 3]
        axes = Axes3D(fig)
        axes = fig.gca(projection='3d')
        axes.plot(x1, y1, z1, lw = 0, marker = '.', ms = 10, markevery = None, color = 'red')
        axes.plot(x2, y2, z2, lw = 0, marker = '.', ms = 10, markevery = None, color = 'green')
        return np.vstack((class1, class2)), axes
    else:
        plt.plot(x1, y1, 'bo')
        plt.plot(x2, y2, 'ro')
        return np.vstack((class1, class2)), 0


def draw(weights, col, axes):
    def line(a, b, x):
        return a*x+b

    def plane(d, a, b, c, x, y):
        return -a*x/c-b*y/c+d/c
    if weights.shape[0] == 4:
        interval_x = np.arange (-10, 10, 1)
        interval_y = np.arange (-10, 10, 1)
        xgrid, ygrid = np.meshgrid(interval_x, interval_y)
        zgrid = plane(weights[0], weights[1], weights[2], weights[3], xgrid, ygrid)
        axes.plot_surface(xgrid, ygrid, zgrid, vmin = -10, vmax = 10, color = col, alpha=0.3)
        #axes.contour(xgrid, ygrid, zgrid, zdir='z', offset=10, cmap=cm.coolwarm)
        #axes.contour(xgrid, ygrid, zgrid, zdir='x', offset=10, cmap=cm.coolwarm)
        #axes.contour(xgrid, ygrid, zgrid, zdir='y', offset=10, cmap=cm.coolwarm)
        axes.set_zlim(-10, 10)
    if weights.shape[0] == 3:
        interval = np.arange(-10, 10, 1)
        pb.plot(interval, line(-weights[1]/weights[2], weights[0]/weights[2], interval))
        pb.xlim([-10, 10])
        pb.ylim([-10, 10])
