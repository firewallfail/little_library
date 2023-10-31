import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'devkey')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_DATABASE = os.environ.get('DB_DATABASE')
DB_HOSTNAME = os.environ.get('DB_HOSTNAME')

NO_UPDATE_NEEDED = -1