#!/usr/bin/env python

import sys
sys.path.append("gen-py")
from api import APIsvc
import json
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import time


trans_local = TSocket.TSocket("localhost", 9090)
trans_local = TTransport.TBufferedTransport(trans_local)
proto = TBinaryProtocol.TBinaryProtocol(trans_local)
client_local = APIsvc.Client(proto)



trans_local.open()



top_time_local = []
# FOR TOP
for number in range(1, 20):
    a = time.time()
    msg = client_local.getTop()
    b = time.time()
    data = json.loads(msg)
    top_time_local.append(b - a)
    #print("[Client] top: %s" % str(data))
print(top_time_local)


top_no_cache_time_local = []
# FOR TOP NO CACHE
for number in range(1, 20):
    a = time.time()
    msg = client_local.getTopNoCache()
    b = time.time()
    data = json.loads(msg)
    top_no_cache_time_local.append(b - a)
    #print("[Client] top no cache: %s" % str(data))
trans_local.close()
print(top_no_cache_time_local)




sum = 0
for number in top_time_local:
    sum += number
print("Cache time local: " + str(sum / len(top_time_local)))

sum = 0
for number in top_no_cache_time_local:
    sum += number
print("No cache time local : " + str(sum / len(top_no_cache_time_local)))


import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(top_time,columns=['CACHE'])
print("Estadisticas de prueba con cache de servidor en EEUU")
print(df.describe())

df.plot.box()
print(plt.show())



df = pd.DataFrame(top_no_cache_time,columns=['NO CACHE'])
print("Estadisticas de prueba sin cache de servidor en EEUU")
print(df.describe())

df.plot.box()
plt.show()



df = pd.DataFrame(top_time_local,columns=['CACHE - LOCAL'])
print("Estadisticas de prueba con cache de servidor local")
print(df.describe())
df.plot.box()
df.plot.box(showfliers=False)
plt.show()



df = pd.DataFrame(top_no_cache_time_local,columns=['NO CACHE - LOCAL'])
print("Estadisticas de prueba sin cache de servidor local")
print(df.describe())
df.plot.box()
df.plot.box(showfliers=False)
plt.show()



