from flask import Flask, request
from json import dumps, loads
from Register import newClient, newLink, newDepositRequest, periodicServiceRegister,transferFromSavings
app = Flask(__name__)

methods = ['POST']

@app.route("/")
def statusPage():
    return "Up and running baby ;)"

@app.route("/clientRegister", methods=methods)
def newClientService():
    clientID=newClient(request.json)
    return clientID

@app.route("/makeALink", methods=methods)
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

@app.route("/makeDepositRequest", methods=methods)
#{
#   "userToken":"XXXXXXXX",
#   "requestInfo":{
#      "linkID":"XXXXXXXX",
#      "amount":"XXXXXXXX",
#      "bank":"BANCO X",
#      "depositReason":"RAZON X",
#      "depositType":"<Ahorro/Directo>"
#   }
#}
def newDepositRequestService():
    response = newDepositRequest(request.json)
    return response

@app.route("/periodicServiceRegister", methods=methods)
#{
#   "userToken":"XXXXXXXX",
#   "linkID":"XXXXXXXX",
#   "serviceInfo":{
#       "provider":"Provider name",
#       "account":"XXXXXXXXXXXX",
#       "reference":"XXXXXXXXXXXX"
#   }
#}
def periodicServiceRegisterService():
    response = periodicServiceRegister(request.json)
    return response

@app.route("/transferFromSavings", methods=methods)
#{
#   "userToken":"XXXXXXXX",
#   "transferInfo":{
#       "linkID":"XXXXXXXX",
#       "ammount":"XXXXXXXXXX",
#   }
#}
def transferFromSavingsService():
    response = transferFromSavings(request.json)
    return response
