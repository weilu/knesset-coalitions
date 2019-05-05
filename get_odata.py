'''
README:

The full relevant url returns all the votes of the 20th Knesset (filtered by knesset_num eq 20) and selects only the wanted fields:

http://knesset.gov.il/Odata/Votes.svc/vote_rslts_kmmbr_shadow?$filter=knesset_num%20eq%2020&amp;$select=vote_id,%20kmmbr_id,%20kmmbr_name,%20vote_result,%20faction_id,%20faction_name'

Becuase the data is too big, we get only the first chunk of the data with a field that stated what to skip for the next query. url for example:

'http://knesset.gov.il/Odata/Votes.svc/vote_rslts_kmmbr_shadow?$filter=knesset_num%20eq%2020&amp;$select=vote_id,%20kmmbr_id,%20kmmbr_name,%20vote_result,%20faction_id,%20faction_name&amp&$skiptoken=%27000000427%27,22406'

We have to perform paging.

Here we use pyslet library that perform paging for us and parsing the ODATA xml.

The outputs are:
'laws.pickle' - structure is {<vote_id>: { "kmmbrs2votes": <kmmbr_id>: <vote_result>}}
'kmmrs.pickle' - structure is {<kmmbr_id> : {kmmbr_name: <kmmbr_name> , faction_id: <faction_id>, faction_name: <faction_name> }}

where vote_id, kmmbr_id (= knesset member), faction_id are ids given by the knesset system.
laws.pickle is the actual voting results -- for each voting we have the vote_result of each one of the members .
kmmrs.pickle helps to get the hebrew name of the knesset member (for later use).


'''

import helper
import logging
logging.basicConfig(level=logging.INFO)

from pyslet.odata2.client import Client
import pyslet.odata2.core as core

c = Client('http://knesset.gov.il/Odata/Votes.svc/')
res = c.feeds['vote_rslts_kmmbr_shadow'].open()
filter = core.CommonExpression.from_str("knesset_num eq 20")
res.set_filter(filter)
laws = helper.load_pickle('laws.pickle')       # laws = {<vote_id>: { "kmmbrs2votes": <kmmbr_id>: <vote_result>}}
kmmbrs = helper.load_pickle('kmmrs.pickle')    # kmmbrs = {<kmmbr_id> : {kmmbr_name: <kmmbr_name> , faction_id: <faction_id>, faction_name: <faction_name> }}
#helper.init_pickle('kmmrs.pickle') #use for first run
#helper.init_pickle('laws.pickle')  #use for first run

# todo fix products..naming
for p in res.itervalues():
    #print (p.key(), p['vote_id'].value, p['kmmbr_id'].value, p['kmmbr_name'].value, p['vote_result'].value, p['knesset_num'].value, p['faction_id'].value,p['faction_name'].value)
    vote_id, kmmbr_id, kmmbr_name, vote_result, faction_id, faction_name = p['vote_id'].value,  p['kmmbr_id'].value, p['kmmbr_name'].value, p['vote_result'].value, p['faction_id'].value,p['faction_name'].value
    if vote_id in laws:
        laws[vote_id]["kmmbrs2votes"][kmmbr_id] = vote_result
    else:
        laws[vote_id]={'kmmbrs2votes': {kmmbr_id: vote_result}}

    if kmmbr_id not in kmmbrs:
        kmmbrs[kmmbr_id] = {'kmmbr_id': kmmbr_id, 'kmmbr_name': kmmbr_name, 'faction_id': faction_id, 'faction_name': faction_name}
        print(kmmbrs)
        helper.dump_pickle('kmmrs.pickle', kmmbrs) #updates our pickles ones in a while
        helper.dump_pickle('laws.pickle', laws)

res.close()
# print()
# print('laws len:', len(laws))
# print()
# print('knesset mmbrs len:', len(kmmbrs))












