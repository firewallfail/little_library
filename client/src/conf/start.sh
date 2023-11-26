if [ "${DEPLOY_ENV}" = "PROD" ]; then
    nginx
    npm run dev
else
    npm run dev
fi