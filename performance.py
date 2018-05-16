import time
from alch_query import query
from alch_commint import create_list_ord

start_time = time.time()
create_list_ord(10000)
'''query()'''
print("--- %s seconds ---" % (time.time() - start_time))