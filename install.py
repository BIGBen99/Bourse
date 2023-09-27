import json
import log
import os
import psycopg2

log.log(log.INFO, 'Debut de l\'installation')
if os.path.isfile(os.path.dirname(__file__) + '/.env'):
    log.log(log.INFO, 'Environnement de DEV')
    with open(os.path.dirname(__file__) + '/.env') as f:
        data = f.read()

        config = json.loads(data)
else:
    print()
    
log.log(log.DEBUG, 'postgreSQL config: ' + str(config))

# conn = psycopg2.connect(host=config['host'], user=config['user'], password=config['password'], dbname=config['dbname'], application_name=config['application_name'])
# conn.close()
log.log(log.INFO, 'Fin de l\'installation')