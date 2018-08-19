import sys
sys.path.append("gen-py")
from api import APIsvc

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

trans = TSocket.TSocket("localhost", 9090)
trans = TTransport.TBufferedTransport(trans)
proto = TBinaryProtocol.TBinaryProtocol(trans)
client = APIsvc.Client(proto)

trans.open()
msg = client.getTop()
print("[Client] received: %s" % msg)
trans.close()

