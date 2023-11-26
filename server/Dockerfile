FROM python:3.10.10-alpine

RUN apk update && \
    apk add --no-cache wget && \
    apk add --no-cache build-base libffi-dev openssl-dev && \
    apk add python3 py3-pip gcc musl-dev

RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
ENTRYPOINT [ "python3", "-u", "app.py" ]
EXPOSE 9090/udp