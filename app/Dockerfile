FROM python:3.10.13


WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install openai --upgrade


CMD [ "streamlit","run","app.py","--server.port","8080" ]