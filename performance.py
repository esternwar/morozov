import time
from alch_commint import create_list_ord

start_time = time.time()
create_list_ord(500)
print("--- %s seconds ---" % (time.time() - start_time))