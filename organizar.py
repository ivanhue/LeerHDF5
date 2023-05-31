import numpy as np


array = np.array([0,1,2,3,0,1,2,3])

print(array.reshape((4,2), order='F'))