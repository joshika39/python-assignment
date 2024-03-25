FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY app/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

LABEL maintainer="Joshua Hegedus <josh.hegedus@outlook.com>"
LABEL version="1.0"
LABEL description="A simple Python web application using FastAPI. University assignment."
LABEL vendor="Joshua Hegedus"
LABEL license="MIT"
LABEL url="https://py-assigment.kou-gen.net"
LABEL schema-version="1.0"

LABEL org.opencontainers.image.source="https://github.com/joshika39/python-assignment"
LABEL org.opencontainers.image.title="Python Assignment"
LABEL org.opencontainers.image.description="A simple Python web application using FastAPI. University assignment."
LABEL org.opencontainers.image.url="https://py-assigment.kou-gen.net"
LABEL org.opencontainers.image.documentation="https://py-assigment.kou-gen.net/docs"
