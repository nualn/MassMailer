import os

dirname = os.path.dirname(__file__)

DB_FILE_NAME = 'database.sqlite'
DB_FILE_PATH = os.path.join(dirname, '..', 'data', DB_FILE_NAME)
