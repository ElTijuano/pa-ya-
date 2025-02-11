import azure.cosmos.cosmos_client as cosmos_client

config = {
    'ENDPOINT': 'https://basepro.documents.azure.com:443/',
    'PRIMARYKEY': 'WFau3JjOINHhK3NrLBzlZxNOz3C4zHn0VP8FRX20moNtlTzOkBneMshBmiRTaQfR6YA6Tjrowj2NxxYlqPC0AQ==',
    'DATABASE': 'basepro',
    'CONTAINER': 'server'
}

# Initialize the Cosmos client
client = cosmos_client.CosmosClient(url_connection=config['ENDPOINT'], auth={
                                    'masterKey': config['PRIMARYKEY']})

# Create a database
db = client.CreateDatabase({'id': config['DATABASE']})

# Create container options
options = {
    'offerThroughput': 400
}

container_definition = {
    'id': config['CONTAINER']
}

# Create a container
container = client.CreateContainer(db['_self'], container_definition, options)

# Create and add some items to the container
item1 = client.CreateItem(container['_self'], {
    'id': 'server1',
    'Web Site': 0,
    'Cloud Service': 0,
    'Virtual Machine': 0,
    'message': 'Hello World from Server 1!'
    }
)

item2 = client.CreateItem(container['_self'], {
    'id': 'server2',
    'Web Site': 1,
    'Cloud Service': 0,
    'Virtual Machine': 0,
    'message': 'Hello World from Server 2!'
    }
)

# Query these items in SQL
query = {'query': 'SELECT * FROM server'}

options = {}
options['enableCrossPartitionQuery'] = True
options['maxItemCount'] = 2

result_iterable = client.QueryItems(container['_self'], query, options)
for item in iter(result_iterable):
    print(item['message'])
