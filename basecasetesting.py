import numpy as np
import pandas as pd
matrix_1 = np.array([[0, 1, 2]])
# print(matrix_1)
matrix_2 = np.array([[5, 5, 5]])
matrix_3 = np.concatenate(matrix_1, matrix_2)
print(matrix_3)
print(matrix_1.shape)
