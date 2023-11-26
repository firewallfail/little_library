if [ "${DEPLOY_ENV}" = "PROD" ]; then
    nginx
    tail -f /var/log/nginx/access.log
else
    npm run dev
fi