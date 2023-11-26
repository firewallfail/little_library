FROM node:lts-alpine
# make the 'app' folder the current working directory
WORKDIR /app
# install mysql dependencies
RUN apk update \
    && apk add nginx
# copy 'package.json' to install dependencies
COPY ../client/package*.json ./
COPY ../client/src/conf/nginx/* /etc/nginx/http.d/default.conf
# install dependencies
RUN npm install
# copy files and folders to the current working directory (i.e. 'app' folder)
COPY ../client .
# build app for production with minification
RUN npm run build

# RUN adduser -D little_library
# RUN chown -R little_library:little_library ./
# USER little_library

EXPOSE 5173

# configure the container to run in an executed manner
ENTRYPOINT [ "sh" ]

CMD ["./src/conf/start.sh" ]