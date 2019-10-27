from json import dumps, loads
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as az_err
from pickle import load, dump

config = {
    'ENDPOINT': 'https://basepro.documents.azure.com:443/',
    'PRIMARYKEY': 'WFau3JjOINHhK3NrLBzlZxNOz3C4zHn0VP8FRX20moNtlTzOkBneMshBmiRTaQfR6YA6Tjrowj2NxxYlqPC0AQ==',
    'DATABASE': 'basepro'
}

def openContainer(containerID):
    client = cosmos_client.CosmosClient(url_connection=config['ENDPOINT'], auth={'masterKey': config['PRIMARYKEY']})

    try:
        db = client.CreateDatabase({'id': config['DATABASE']})
        with open('DB.pkl', 'wb') as f:
            dump(db, f, -1)
    except:
        with open('DB.pkl', 'rb') as f:
            db = load(f)

    try:
        options = {'offerThroughput': 400}
        container_definition = {'id': containerID}
        container = client.CreateContainer(db['_self'], container_definition, options)
        with open(containerID + '.pkl', 'wb') as f:
            dump(container, f, -1)
    except:
        with open(containerID + '.pkl', 'rb') as f:
            container= load(f)

    return client, container

def queryAction(queryText, client, container):
    query = {'query': queryText}

    options = {}
    options['enableCrossPartitionQuery'] = True
    options['maxItemCount'] = 2

    result = client.QueryItems(container['_self'], query, options)
    return result

def storeClient(client):
    cosm_client, container = openContainer('cliente')

    item1 = cosm_client.CreateItem(container['_self'], client)

    return item1

def storeLink(SenderHash, ReciverHash):
    return "00001", "Ok"

def storeRequest(requestInfo, requestID, reference):
    return "Ok"

def storeIncomeRequest(requestInfo, requestID, reference):
    return "Ok"

def storePeriodicService(serviceInfo, linkID):
    return "00001", "Ok"

def storePeriodicServiceAsk(serviceInfo, linkID):
    return "00001", "Ok"

def transfer(transferInfo):
    return "Ok"

def genID():
    return "00001"

def genRequestIDs():
    return "00001", "083FJS5339FJ"

def genRequestID():
	return "00001"

def auth(token):
    return True

def validService(serviceInfo):
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

def periodicServiceRegister(data):
    if (auth(data.get('userToken')) and validService(data.get('serviceInfo'))):
        serviceID, status = storePeriodicService(data.get('serviceInfo'), data.get('linkID'))
    else:
        serviceID = None
        status = 500

    response = {"serviceID":serviceID, "status":status}
    return dumps(response)

def askForPeriodicServiceRegister(data):
    if (auth(data.get('userToken')) and validService(data.get('serviceInfo'))):
        askID, status = storePeriodicServiceAsk(data.get('serviceInfo'), data.get('linkID'))
    else:
        askID = None
        status = 500

    response = {"askID":askID, "status":status}
    return dumps(response)

def transferFromSavings(data):
    if auth(data.get('userToken')):
        status = transfer(data.get('transferInfo'))
    else:
        status = 500

    response = {"status":status}
    return dumps(response)

def newIncomeRequest(data):
    if auth(data.get('userToken')):
        requestID = genRequestID(data.get('requestInfo'))
        status = storeIncomeRequest(data.get('requestInfo'), requestID, reference)
    else:
        status = 500

    response = {"status":status}
    return dumps(response)

def cancelPeriodicServiceRegister(data):
    if auth(data.get('userToken')):
        status = storePeriodicService(data.get('serviceID'))
    else:
        status = 500

    response = {"status":status}
    return dumps(response)
