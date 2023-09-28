import json
import log
import os
import psycopg2

log.log(log.INFO, 'Debut de l\'installation')
def load_config():
    if os.path.isfile(os.path.dirname(__file__) + '/.envv'):
        log.log(log.INFO, 'Environnement de DEV')
        with open(os.path.dirname(__file__) + '/.env') as f:
            data = f.read()

            config = json.loads(data)
    else:
        config = {}
        if 'POSTGRESQL_HOST' in os.environ:
            config['host'] = os.environ['POSTGRESQL_HOST']
        else:
            log.log(log.ERROR, 'POSTGRESQL_HOST env var must be set')
        if 'POSTGRESQL_USER' in os.environ:
            config['user'] = os.environ['POSTGRESQL_USER']
        else:
            log.log(log.ERROR, 'POSTGRESQL_USER env var must be set')
        if 'POSTGRESQL_PASSWORD' in os.environ:
            config['password'] = os.environ['POSTGRESQL_PASSWORD']
        else:
            log.log(log.ERROR, 'POSTGRESQL_PASSWORD env var must be set')
        if 'POSTGRESQL_DBNAME' in os.environ:
            config['dbname'] = os.environ['POSTGRESQL_DBNAME']
        else:
            log.log(log.ERROR, 'POSTGRESQL_DBNAME env var must be set')
        if 'POSTGRESQL_APPLICATION_NAME' in os.environ:
            config['application_name'] = os.environ['POSTGRESQL_APPLICATION_NAME']
        else:
            log.log(log.ERROR, 'POSTGRESQL_APPLICATION_NAME env var must be set')
        return config

config = load_config()
log.log(log.DEBUG, 'postgreSQL config: ' + str(config))

# conn = psycopg2.connect(host=config['host'], user=config['user'], password=config['password'], dbname=config['dbname'], application_name=config['application_name'])
# conn.close()

log.log(log.INFO, 'Fin de l\'installation')