# start by pulling the python image
FROM python:3.8-slim-buster

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

ENV FLASK_APP app.py
ENV FLASK_DEBUG development
ENV FLASK_RUN_PORT 8001
ENV FLASK_RUN_HOST 0.0.0.0

# install the dependencies and packages in the requirements file

RUN pip3 install --no-cache-dir -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner

ENTRYPOINT [ "python" ]
CMD ["app.py"]