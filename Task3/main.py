import math
import numpy as np
from scipy.optimize import newton_krylov
import CentralPath


A = np.array(([[1, -1],[2, -1],[0, 1]]))
b = np.array([1, 3, 5])
c = np.array([1, 0])



param = np.array([1, 1, 1, 1, 1])
lin_prog = CentralPath.CentralPathMethod(param)
lin_prog.fit(c, A, b)
print lin_prog.method(np.ones(8))

