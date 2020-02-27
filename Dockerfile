FROM python:3

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY ..

CMD [ "PYTHON", "./app/app.py" ]