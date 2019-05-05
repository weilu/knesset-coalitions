import helper
import pandas as pd
''' Creates a csv readable for humans -- votes.csv. 
7057 law ids (rows) x 143 kmmbrs ids (cols) 
1 - for the law, 2 - opposed to the law, 0 - didn't attend. 
In addition, we dump the same data structure to a pickle -- 'law2vector.pickle'
'''

#todo fix laws
laws = helper.load_pickle('laws.pickle')       # laws = {<vote_id>: { "kmmbrs2votes": {<kmmbr_id>: <vote_result>}}
kmmbrs = helper.load_pickle('kmmrs.pickle')    # kmmbrs = {<kmmbr_id> : {kmmbr_name: <kmmbr_name> , faction_id: <faction_id>, faction_name: <faction_name> }}

kmmbrs_num = len(kmmbrs)
kmmbrs_lst = list(kmmbrs.keys())

# convert kmmbrs2votes dict to a fixed list:
# creates: new_laws = {<vote_id>: [1,2,0,...,1]}}
def fix_members_lst(laws,kmmbrs):
    new_laws = {}
    for vote_id, kmmbrs2votes in laws.items():
        l = [0] * len(kmmbrs) # create a fixed list of the number of the knesset members
        for kmmbr_id, vote_result in kmmbrs2votes["kmmbrs2votes"].items():
            inx = kmmbrs[kmmbr_id]['idx']
            l[inx] = vote_result
        new_laws[vote_id] = l

    print(len(new_laws))
    return new_laws

def to_csv(new_laws):
    df = pd.DataFrame.from_dict(new_laws, orient='index', columns=kmmbrs_lst)
    df.to_csv('votes.csv')
    print("csv has created")
    return

new_laws = fix_members_lst(laws,kmmbrs)

# helper.init_pickle('law2vector.pickle')
# helper.dump_pickle('law2vector.pickle', new_laws)