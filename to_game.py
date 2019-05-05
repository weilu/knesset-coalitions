
''' The votes.csv consists of the data as is. votes for each law and each member. 7057 laws X 143 members. values represents:  1 - for the law, 2 - opposed to the law, 0 - didn't attend.
Here, we would like to convert this data to an input for a cooperative game. That is, sets of players (members) and theirs values.

1. represent as sets: A group is all the members that voted the same. We extracted only groups members that voted 1 or 2 which is for or against the law and ignored the others. each group is represented by a binary vector.
The output A is a matrix of all of these sets.
2. calculate the value of each set:  We calculate the value of a set to be 1 if the set won (they were the majority) and 0 otherwise.
The output b is a vector of the values for each set in A (same order as A)

we multiply A and b by -1 to suited the input for the LP

'''
import helper
from collections import Counter

LAW_PICKLE = 'law2vector.pickle'
#LAW_PICKLE = 'law2vecA.pickle'
A_PICKLE = 'A.pickle'
B_PICKLE = 'b.pickle'

def is_zeroes(x):
    new_x=[]
    new_x[:] = (value for value in x if value != 0) # trim the zeroes
    #print (new_x)
    if len(new_x)==0:
        return True
    return False


# input: x - votes' list, output: int. return 1 if the majority voted 1 (for the law), else, return 2.
def majority(x):
    new_x=[]
    new_x[:] = (value for value in x if value != 0) # trim the zeroes
    new_x[:] = (value for value in new_x if value != 3)
    new_x[:] = (value for value in new_x if value != 4)
    occrs = Counter(new_x).most_common(2)
    #print (occrs)
    #if len(occrs)==0: return 2
    if len(occrs)==2 and occrs[0][1] == occrs[1][1]: #equal votes for and against
        return 2 #  2 - the law has not being approved
    else:
        return occrs[0][0]

# x = [0,0,0]
# print (majority(x))

def to_sets(items):
    set1 = [1 if x == 1 else 0 for x in items]
    set2 = [1 if x == 2 else 0 for x in items]
    return set1, set2

#x = [0,0,0]
def to_set_and_value(A,b,x):
    m = majority(x)
    set1, set2 = to_sets(x)

    v1 = 1 if m == 1 else 0
    b.append(v1)
    A.append(set1)

    b.append(1 - v1)
    A.append(set2)
    #print(A,b)
    return A, b

def to_set_and_value_no_dup(A,b,x):
    m = majority(x)
    set0, set1, set2 = to_sets(x)

    if set0 not in A:
        A.append(set0)
        b.append(0)

    v1 = 1 if m == 1 else 0
    if set1 not in A:
        b.append(v1)
        A.append(set1)

    if set2 not in A:
        b.append(1 - v1)
        A.append(set2)
    #print(A,b)
    return A, b

def to_set_and_value_lst(A,b,x):
    m = majority(x)
    set0, set1, set2 = to_sets(x)
    if set0 not in A:
        A.append(set0)
        b.append([0])
    else:
        inx = A.index(set0)
        b[inx].append(0)

    v1 = 1 if m == 1 else 0
    if set1 not in A:
        b.append([v1])
        A.append(set1)
    else:
        inx = A.index(set1)
        b[inx].append(v1)

    if set2 not in A:
        b.append([1 - v1])
        A.append(set2)
    else:
        inx = A.index(set2)
        b[inx].append(1 - v1)
    #print(A,b)
    return A, b

def to_avg_val(b):
    #calc the avg value
    newb = []
    for l in b:
        avg = (l.count(1))/len(l)
        newb.append(avg)
    return newb

#laws = {991:[1,1,0], 990:[1,1,0] ,992:[2,2,0] ,999:[0,0,0]}
def iterate(laws):
    A=[]
    b=[]
    for vote_id, l in laws.items():
        if is_zeroes(l): continue
        A, b = to_set_and_value(A,b,l) # use the other functions if there are duplicates in the data (right now, we don't have)
    #print("NOTE: calc the avg value.")
    #b = to_avg_val(b)
    #print(A,b)
    return A, b

def minus(A,b):
    # multiply A and b by -1
    newA=[]
    for a in A:
        new_a = [-1 if x == 1 else 0 for x in a]
        newA.append(new_a)
    b = [-1 if x == 1 else 0 for x in b]
    return newA, b

# Includes additional constraint that sum-total of payoffs must EXCEED a certain amount
# This should be DONE AFTER the A,b = minus(A,b) step
def minpay(A,b,payout):
    dim = len(A[0])
    A.append([-1] * dim)
    b.append(-1*payout)
    return A, b

laws = helper.load_pickle(LAW_PICKLE) #'law2vector.pickle' is of the same sturcture as votes.csv. that is a vector of all the vote results for each law
A,b = iterate(laws)
A,b = minus(A,b)
A,b = minpay(A,b,18.81)
helper.init_pickle(A_PICKLE)
helper.init_pickle(B_PICKLE)
helper.dump_pickle(A_PICKLE, A)
helper.dump_pickle(B_PICKLE, b)









