#!/usr/bin/env python

import sys
sys.path.append("gen-py")
from api import APIsvc
import json
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import time


trans = TSocket.TSocket("104.131.10.154", 9090)
trans = TTransport.TBufferedTransport(trans)
proto = TBinaryProtocol.TBinaryProtocol(trans)
client = APIsvc.Client(proto)




trans.open()


top_time = []
# FOR TOP
for number in range(1,20):
    a = time.time()
    msg = client.getTop()
    b = time.time()
    data = json.loads(msg)
    top_time.append(b - a)
    #print("[Client] top: %s" % str(data))
print("Pruebas con cache")
print(top_time)


top_no_cache_time = []
# FOR TOP NO CACHE
for number in range(1, 20):
    a = time.time()
    msg = client.getTopNoCache()
    b = time.time()
    data = json.loads(msg)
    top_no_cache_time.append(b - a)
    #print("[Client] top no cache: %s" % str(data))
trans.close()
print("Pruebas sin cache")
print(top_no_cache_time)



sum = 0
for number in top_time:
    sum += number
print("Cache time: " + str(sum / len(top_time)))

sum = 0
for number in top_no_cache_time:
    sum += number
print("No cache time: " + str(sum / len(top_no_cache_time)))





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



