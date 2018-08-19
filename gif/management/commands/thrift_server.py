# import sys
# sys.path.append("gen-py")
# from gif import HelloSvc
#
# from thrift.transport import TSocket
# from thrift.transport import TTransport
# from thrift.protocol import TBinaryProtocol
# from thrift.server import TServer
#
# class HelloHandler:
#     def hello_func(self):
#         print("[Server] Handling client request")
#         return "Hello from the python server"
#
# handler = HelloHandler()
# proc = HelloSvc.Processor(handler)
#
# trans_svr = TSocket.TServerSocket(port=9090)
# trans_fac = TTransport.TBufferedTransportFactory()
# proto_fac = TBinaryProtocol.TBinaryProtocolFactory()
# server = TServer.TSimpleServer(proc, trans_svr, trans_fac, proto_fac)
# server.serve()
#
#
#

import sys
from django.core.management.base import BaseCommand

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
sys.path.append("gif/management/commands/gen-py")
from api import APIsvc
import logging
logging.basicConfig()
from gif.models import Gif

#now define the service handler according to your thrift method declaration
class APIHandler:
    def __init__(self):
        pass

    def getTop(self):
        print("[Server] Handling client request")
        return Gif.objects.first().description

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        handler = APIHandler()
        proc = APIsvc.Processor(handler)

        trans_svr = TSocket.TServerSocket(port=9090)
        trans_fac = TTransport.TBufferedTransportFactory()
        proto_fac = TBinaryProtocol.TBinaryProtocolFactory()
        server = TServer.TSimpleServer(proc, trans_svr, trans_fac, proto_fac)
        server.serve()

        # You could do one of these for a multithreaded server
        #server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
        #server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)



