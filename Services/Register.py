from json import dumps, loads

def storeClient(client):
    return "Ok"

def genID():
    return "00001"


def newClient(data):
    human=data.get('human')
    ExternalID=data.get('ExternalID')
    IDprovider=data.get('IDprovider')
    clientID=genID()
    client={'clientID':clientID, 'human':human, 'ExternalID':ExternalID, 'IDprovider':IDprovider}
    status=storeClient(client)
    return dumps(clientID)
