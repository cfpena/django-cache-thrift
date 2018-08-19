import sys
sys.path.append("gen-py")
from api import APIsvc
import json
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

#trans = TSocket.TSocket("104.131.10.154", 9090)
trans = TSocket.TSocket("localhost", 9090)
trans = TTransport.TBufferedTransport(trans)
proto = TBinaryProtocol.TBinaryProtocol(trans)
client = APIsvc.Client(proto)

trans.open()

#FOR ALL GIFS
msg = client.getGifs()
data = json.loads(msg)
print("[Client] all gifs: %s" % str(data))


#FOR TOP
msg = client.getTop()
data = json.loads(msg)
print("[Client] top: %s" % str(data))

#FOR TOP NO CACHE
msg = client.getTopNoCache()
data = json.loads(msg)
print("[Client] top no cache: %s" % str(data))
trans.close()

