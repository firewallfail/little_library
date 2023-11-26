# define python image
FROM python:3.9-alpine

# copy the requirements file into the image
COPY ../server/src ./app
# switch working directory
WORKDIR /app

RUN adduser -D little_library

# install mysql dependencies
RUN apk update \
    && apk add --virtual build-deps \
    gcc \
    python3-dev \
    musl-dev \
    libpq-dev \
    mariadb-dev \
    curl \
    linux-headers\
    libc-dev

# install the dependencies and packages in the requirements file
RUN pip install -r ./conf/requirements.txt

# copy every content from the local file to the image
RUN chown -R little_library:little_library ./
USER little_library

# configure the container to run in an executed manner
ENTRYPOINT [ "sh" ]

CMD ["./conf/start.sh" ]