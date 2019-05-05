from numpy import array, eye, hstack, ones, vstack, zeros
import numpy
import cvxopt
import helper
import datetime
import numpy as np

A = helper.load_pickle('A.pickle')
b = helper.load_pickle('b.pickle')

#toy example
# A= [[-1,-1,0,0,0], [0,0,-1,0,0],[0,0,0,-1,-1], [-1,0,0,0,0],[0,-1,-1,-1,0],[0,0,0,0,-1]]
# b=[-1,0,0,0,-1,0]

c = [1]*len(A[0])

def cvxopt_solve_min(b, A, solver=None):
    n= len(A[0])
    c = ones(n)

    # cvxopt constraint format: G * x <= h

    h1 = b
    G1 = A
    G2 = -eye(n)
    h2 = 0 * ones(n)

    c = cvxopt.matrix(c)
    G = cvxopt.matrix(vstack([G1, G2]))
    h = cvxopt.matrix(hstack([h1, h2]))
    sol = cvxopt.solvers.lp(c, G, h, solver=solver)
    x = np.array(sol['x'])
    x = list(map(lambda i: i[0], x))

    print ('status:',sol['s'], 'optimal sol:', sol["primal objective"])
    return x

x = cvxopt_solve_min(b, A, solver=None)

helper.init_pickle('x.pickle')
helper.dump_pickle('x.pickle', x)


print(sum(x))
print(x)


