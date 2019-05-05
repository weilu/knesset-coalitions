import pickle
import datetime

def load_pickle(pickle_file):
    with open(pickle_file, 'rb') as pf:
        dict = pickle.load(pf)
        return dict

def dump_pickle(pickle_file,dict):
    with open(pickle_file, 'wb') as handle:
        pickle.dump(dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return

def init_pickle(name_pickle):
    with open(name_pickle, 'wb') as handle:
        pickle.dump({}, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return

#adds idx field to kmmbrs
def add_idx(kmmbrs):
    i=0
    for k in kmmbrs:
        print(k, kmmbrs[k])
        kmmbrs[k]['idx'] = i
        i = i+1
    return kmmbrs


'''
usage:
import helper
new_dict = helper.load_pickle('picklename.pickle') 

'''

import os
def save_as(postfix, name, date=None):
    i = 0
    res = ''  # not sure if this is needed...
    while os.path.exists(name+"(%s).txt" % i):
        i += 1

    with open(name+"(%s).txt"% i, "w") as text_file:
        if date: print(f"Date and Time': {datetime.datetime.now()}", file=text_file)
        print(f"{res}", file=text_file)
        return