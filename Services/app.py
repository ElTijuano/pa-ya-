from flask import Flask, request
from json import dumps, loads
from Register import newClient, newLink, newDepositRequest
app = Flask(__name__)


@app.route("/")
def statusPage():
    return "Up and running baby ;)"

@app.route("/clientRegister", methods=['POST'])
def newClientService():
    clientID=newClient(request.json)
    return clientID

@app.route("/makeALink", methods=['POST'])
#{
#   "sender":{
#      "hash":"XXXXXXXX",
#      "token":"XXXXXXXX"
#   },
#   "reciver":{
#      "hash":"XXXXXXXX",
#      "token":"XXXXXXXX"
#   }
#}
def newLinkService():
    response = newLink(request.json)
    return response

@app.route("/makeDepositRequest", methods=['POST'])
#{
#   "userToken":"XXXXXXXX"
#   "requestInfo":{
#      "linkID":"XXXXXXXX",
#      "amount":"XXXXXXXX",
#      "bank":"BANCO X"
#      "depositReason":"RAZON X",
#      "depositType":"<Ahorro/Directo>"
#   }
#}
def newDepositRequestService():
    response = newDepositRequest(request.json)
    return response
