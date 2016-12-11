import math
import numpy as np
from scipy.optimize import newton_krylov
import CentralPath




A = np.array(([[1, -1],[2, -1],[0, 1]]))
b = np.array([1, 3, 5])
c = np.array([1, 0])

A_1 = np.array(([[2, 3, 1], [4, 1, 2], [3, 4, 2]]))
b_1 = np.array([5, 11, 8])
c_1 = np.array([5, 4, 3])



param = np.array([100, 0.01, 0.01, 0.01, 0.01])
lin_prog = CentralPath.CentralPathMethod(param)
lin_prog.fit(c_1, A_1, b_1)
print lin_prog.method()

