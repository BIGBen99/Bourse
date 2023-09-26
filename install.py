import json
import os
import psycopg2

if os.path.isfile(os.path.dirname(__file__) + '/.env'):
    print('DEV')
    with open(os.path.dirname(__file__) + '/.env') as f:
        data = f.read()

        config = json.loads(data)
else:
    print('pas DEV')

print(config)

# conn = psycopg2.connect(host=config['host'], user=config['user'], password=config['password'], dbname=config['dbname'], application_name=config['application_name'])
# conn.close()