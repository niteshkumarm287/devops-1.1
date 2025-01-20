FROM python:3.13.1-slim-bookworm 
RUN pip install flask
WORKDIR /app
COPY main.py /app/main.py
CMD [ "python", "/app/main.py" ]