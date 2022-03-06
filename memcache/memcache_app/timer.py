import threading, time
from datetime import datetime

from memcache_app import memcache
from memcache_app.models import modify_tables

def send_statistics():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    num, sz, requests, hit_rate, miss_rate = memcache.statistics()
    sz = str(format(sz / (1024 * 1024), '.3f')) + 'MB'
    # print(timestamp, sz, flush=True)
    modify_tables.upload_statistics(timestamp, num, sz, requests, hit_rate, miss_rate)
    threading.Timer(5, send_statistics).start()

# single thread version
# def send_statistics(interval=5):
#     def timer():
#         nextcall = time.time()
#         while True:
#             nextcall += interval
#             yield max(nextcall - time.time(), 0)

#     def send():
#         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         # modify_tables.upload_statistics(timestamp)       
#         print(timestamp)

#     t = timer()
#     while True:
#         time.sleep(next(t))
#         send()


