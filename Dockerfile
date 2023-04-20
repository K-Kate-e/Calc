FROM python:3.10-alpine3.17

WORKDIR /calculator

COPY . .

RUN pip install -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0 --port 5555
