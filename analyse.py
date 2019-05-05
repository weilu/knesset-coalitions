import helper
from collections import Counter
import scipy.stats
import numpy as np


x1 = helper.load_pickle('x.pickle')
# x2 = helper.load_pickle('x2_cvx.pickle')
# x3 = helper.load_pickle('x3_cvx.pickle')


import pandas as pd


def count_partic(laws, members):
    for k,v in members.items():
        v['took_part']=0

    for vote_id, kmmbrs2votes in laws.items():
        for kmmbr_id, vote_result in kmmbrs2votes["kmmbrs2votes"].items():
            if vote_result > 0 : members[kmmbr_id]['took_part']+=1

        for k,v in members.items():
            v['took_part']=v['took_part']/len(laws)
    #print('members','\n', members)
    return members


def count_won(laws, members):
    for k, v in members.items():
        v['won'] = 0

    for vote_id, kmmbrs2votes in laws.items():
        for kmmbr_id, vote_result in kmmbrs2votes["kmmbrs2votes"].items():
            if vote_result == 1: members[kmmbr_id]['won'] += 1

    for k, v in members.items():
        v['won'] = v['won'] / len(laws)
    #print('members', '\n', members)
    return members

laws = helper.load_pickle('laws.pickle')
members = helper.load_pickle('kmmrs.pickle')
names, faction, part, won = [],[],[],[]
count_partic(laws, members)
#count_won(laws, members)


for i in members:
    #print(members[i]['kmmbr_name'],members[i]['faction_name'])
    names.append(members[i]['kmmbr_name'])
    faction.append(members[i]['faction_name'])
    part.append(members[i]['took_part'])
    #won.append(members[i]['won'])



data={'name': names, 'payoff': x1, 'faction': faction, 'took_part': part}

df = pd.DataFrame.from_dict(data)
df.to_csv('payoff.csv')
print("new payoff.csv has created")

#print(df)

print()
pearson = scipy.stats.pearsonr(x1,part)
print("(pearson correlation , p-value)")
print(pearson)





