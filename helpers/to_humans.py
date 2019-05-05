from cvxopt import matrix, solvers


import helper
A = helper.load_pickle('../A.pickle')
b = helper.load_pickle('../b.pickle')
#print(A)
import numpy as np
import scipy.io

scipy.io.savemat('Ab.mat', dict(A=A, b=b))

with open("A.txt", "w") as text_file:
    print(f"{A}", file=text_file)
with open("b.txt", "w") as text_file:
    print(f"{b}", file=text_file)
