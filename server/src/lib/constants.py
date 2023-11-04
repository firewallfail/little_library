import os

# Token stuff
SECRET_KEY = os.environ.get('SECRET_KEY', 'devkey')

# DB stuff
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_DATABASE = os.environ.get('DB_DATABASE')
DB_HOSTNAME = os.environ.get('DB_HOSTNAME')

# Google stuff
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

NO_UPDATE_NEEDED = -1

# Errors
ERRORS = {
    'BOOK_NOT_FOUND': 20,
    'UPDATE_COUNT_FAIL': 21
}