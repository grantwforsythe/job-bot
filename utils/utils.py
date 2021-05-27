import logging
import sqlite3
import configparser
import mysql.connector
from mysql.connector import Error

# Set up log file
# This method allows the use of different loggers
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Reads levels INFO and higher: 1. DEBUG, 2. INFO, 3. WARNING, 4. ERROR, 5. CRITICAL

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('database.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def sqlite_connect() -> sqlite3.Connection:
    """
    Connect to a simple database using SQLite.

    If you are getting thrown an error when trying to connect, make sure 'jobs.db' exists.
    If it doesn't, run the follow lines of code:
    
    ```
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('CREATE TABLE jobs (title TEXT, company TEXT, date_applied TEXT, url TEXT)')
    conn.commit()
    ```
    
    :returns: A SQLite connection.
    """
    conn = None

    try:
        conn = sqlite3.connect('jobs.db')
    except sqlite3.DatabaseError as e:
        logger.error(e)
    finally:
        return conn


def mysql_connect() -> mysql.connector:
    """
    Connect to MySQL database.
    Edit the config file with your personal parameters.
    
    :returns: A MySQL connection.
    """
    conn = None

    config = configparser.ConfigParser()
    config.read('config.ini')

    host = config['database']['host']
    database = config['database']['database']
    user = config['database']['user']
    password = config['database']['password']

    try:
        conn = mysql.connector.connect(host=host,
                                       database=database,
                                       user=user,
                                       password=password)
    except Error as e:
        logger.error(e)
    finally:
        if conn:
            logger.info('Connected to database.')
        return conn