FROM python:3

# WORKDIR /usr/src/app
# COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ADD /app/app.py ./

ADD requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

CMD [ "python3", "./app.py" ]
# ENTRYPOINT [ "python3" ]

# CMD [ "./app.py" ]