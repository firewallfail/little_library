if [ "${DEPLOY_ENV}" = "PROD" ]; then
    uwsgi --ini-paste ./conf/uwsgi.ini
else
    alembic upgrade head
    pip install -r ./conf/requirements.txt
    python ./server.py
fi