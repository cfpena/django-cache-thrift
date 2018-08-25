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
from flask import render_template
app = Flask(__name__, template_folder="templates")


#trans = TSocket.TSocket("104.131.10.154", 9090)
trans = TSocket.TSocket("localhost", 9090)
trans = TTransport.TBufferedTransport(trans)
proto = TBinaryProtocol.TBinaryProtocol(trans)
client = APIsvc.Client(proto)

trans.open()

@app.route("/")
def hello():


    msg = client.getTop()
    data = json.loads(msg)


    gifs = client.getGifsPaginated(2)
    print(gifs)
    return render_template('index.html',data=data,gifs=gifs)

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
