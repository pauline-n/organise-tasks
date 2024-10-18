import mysql.connector
import logging
import time
from mysql.connector import errorcode

db_config = {
    'host': 'localhost',
    'user': 'pola',
    'password': 'pola',
    'database': 'todos',
    'use_pure': False
}
try:
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("something is wrong with username and password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Databse does not exist')
    else:
        print(err)
else:
    cnx.close()
    
#setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# log to console 
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# also log to a file
file_handler = logging.FileHandler('c-errors.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def connect_to_mysql(db_config, attempts=3, delay=2):
    attempt = 1
    #implement a reconnection routine
    while attempt < attempts + 1:
        try:
            return mysql.connector.connect(**db_config)
        except (mysql.connector.Error, IOError) as err:
            if (attempts is attempt):
                #attempts to reconnect failed; returning None
                logger.info('failed to connect, exiting without a connection: %s', err)
                return None
            logger.info(
                'COnnection failed: %s. Retrying (%d%d)...',
                err,
                attempt,
                attempts - 1,
            )
            # progressive reconnect delay
            time.sleep(delay **attempt)
            attempt += 1
        return None
    
    
# dummy data
# my_list= [
#     {"task": "Buy a puppy", "status":1}
# ]