import helper
import datetime

A = helper.load_pickle('A.pickle')#[:3000]
b = helper.load_pickle('b.pickle')#[:3000]
c = [1]*len(A[0])

from scipy.optimize import linprog
res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), options={"disp": True},method='interior-point')

print(res)

# save in a txt:
import os
i = 0
while os.path.exists("scipylp(%s).txt" % i):
    i += 1

with open("scipylp(%s).txt" % i, "w") as text_file:
    print(f"Date and Time': {datetime.datetime.now()}", file=text_file)
    print(f"Parameters: method='interior-point'. \n Output\n: {res}", file=text_file)

