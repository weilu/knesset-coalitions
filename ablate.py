'''
Created on Mar 27, 2019

@author: Alan Tsang

This module imports data from a pickle file and randomly removes a desired number of rows of data,  
and exports the results to another pickle file 
'''

import helper
import random

IMPORT_PICKLE_NAME = 'law2vector.pickle'
EXPORT_PICKLE_NAME = 'law2vecA.pickle'
NUM_REMOVE = 706  # 10% of 7057, the number of rows in laws2vector.pickle (as of coding)

def ablate_pickle(pickle_in, pickle_out, num_remove):
    laws = helper.load_pickle(pickle_in)
    
    for i in range(num_remove):
        laws.pop(random.choice(list(laws.keys())))
    
    helper.dump_pickle(pickle_out, laws)
    return

if __name__ == '__main__':
    ablate_pickle(IMPORT_PICKLE_NAME, EXPORT_PICKLE_NAME, NUM_REMOVE)
    