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
import json
from django.core.cache import cache


class APIHandler:
    def __init__(self):
        pass

    def getGifs(self):
        queryset = Gif.objects.all()
        top = map(lambda item: {"url": item.url, "description": item.description, "views": item.views}, queryset)
        response = str(json.dumps(top))
        return response


    def getTop(self):

        print("[Server] Handling client request")


        if(cache.ttl("top")==0):

            print(":::CACHE EXPIRES")
            queryset = Gif.objects.all().order_by('-views')[:10]
            top = map(lambda item: {"url": item.url, "description": item.description, "views": item.views}, queryset)
            response = str(json.dumps(top))
            cache.set("top",response,timeout=10)
            print(":::DATABASE QUERYSET:::")
        else:
            print("::VALID CACHE::")
            response = cache.get("top")

        return response


    def getTopNoCache(self):
        print("[Server] Handling client request no cache")



        print(":::CACHE EXPIRES")
        queryset = Gif.objects.all().order_by('-views')[:10]
        top = map(lambda item: {"url": item.url, "description": item.description, "views": item.views}, queryset)
        response = str(json.dumps(top))
        cache.set("top", response, timeout=10)
        print(":::DATABASE QUERYSET:::")

        return response

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        handler = APIHandler()
        proc = APIsvc.Processor(handler)

        trans_svr = TSocket.TServerSocket(port=9090)
        trans_fac = TTransport.TBufferedTransportFactory()
        proto_fac = TBinaryProtocol.TBinaryProtocolFactory()
        server = TServer.TSimpleServer(proc, trans_svr, trans_fac, proto_fac)
        server.serve()





