from json import dumps, loads

def storeClient(client):
    return "Ok"

def storeLink(SenderHash, ReciverHash):
    return "00001", "Ok"

def storeRequest(requestInfo, requestID, reference):
    return "Ok"

def genID():
    return "00001"

def genRequestIDs():
    return "00001", "083FJS5339FJ"

def auth(token):
    return True

def newClient(data):
    human=data.get('human')
    ExternalID=data.get('ExternalID')
    IDprovider=data.get('IDprovider')
    clientID=genID()
    client={'clientID':clientID, 'human':human, 'ExternalID':ExternalID, 'IDprovider':IDprovider}
    status=storeClient(client)
    response = {"clientID":client.get('clientID'), "status":status}
    return dumps(response)

def newLink(data):
    UserSender = data.get('sender')
    UserReciver = data.get('reciver')
    if (auth(UserSender.get('token')) and auth(UserReciver.get('token'))):
        linkID, status = storeLink(UserSender.get('hash'), UserReciver.get('hash'))
    else:
        linkID = None
        status = 500
    response = {"linkID":linkID, "status":status}
    return dumps(response)

def newDepositRequest(data):
    if auth(data.get('userToken')):
        requestID, reference = genRequestIDs(data.get('requestInfo'))
        status = storeRequest(data.get('requestInfo'), requestID, reference)
    else:
        reference = None
        status = 500

    response = {"reference":reference, "status":status}
    return dumps(response)
