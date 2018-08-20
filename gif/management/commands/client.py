import sys
sys.path.append("gen-py")
from api import APIsvc
import json
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import time
from flask import Flask
from flask import render_template_string

app = Flask(__name__)


@app.route("/")
def hello():
    trans = TSocket.TSocket("104.131.10.154", 9090)
    # trans = TSocket.TSocket("localhost", 9090)
    trans = TTransport.TBufferedTransport(trans)
    proto = TBinaryProtocol.TBinaryProtocol(trans)
    client = APIsvc.Client(proto)

    trans.open()

    # top_time = []
    # # FOR TOP
    # for number in range(1, 10):
    #     a = time.time()
    #     msg = client.getTop()
    #     b = time.time()
    #     data = json.loads(msg)
    #     top_time.append(b - a)
    #     # print("[Client] top: %s" % str(data))
    #
    # top_no_cache_time = []
    # # FOR TOP NO CACHE
    # for number in range(1, 10):
    #     a = time.time()
    #     msg = client.getTopNoCache()
    #     b = time.time()
    #     data = json.loads(msg)
    #     top_no_cache_time.append(b - a)
    #     # print("[Client] top no cache: %s" % str(data))
    # trans.close()
    #
    # sum = 0
    # for number in top_time:
    #     sum += number
    # print("No cache time: " + str(sum / len(top_time)))
    #
    # sum = 0
    # for number in top_no_cache_time:
    #     sum += number
    # print("Cache time: " + str(sum / len(top_no_cache_time)))

    msg = client.getTopNoCache()
    data = json.loads(msg)

    html = "{% for gif in data %}" \
           "<img src={{ gif.url }}></img>" \
           "<div >Description: {{ gif.description }}</div>"\
            "<div >Views: {{ gif.views }}</div>" \
            "{% endfor %}"
    return render_template_string(html,data=data)


app.run(host='0.0.0.0', port=8080)







# all_gifs_time=[]
# #FOR ALL GIFS
# for number in range(1,100):
#     a = time.time()
#     msg = client.getGifs()
#     b = time.time()
#     data = json.loads(msg)
#     #print("[Client] all gifs: %s" % str(data))
#     all_gifs_time.append(b-a)




#print(all_gifs_time)

#print(top_no_cache_time)
#print("load all: " + str(b-a))
#print("load cache:"+ str(d-c))
#print("load no cache:"+ str(g-f))
