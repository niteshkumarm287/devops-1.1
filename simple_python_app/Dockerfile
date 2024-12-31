FROM python:3.13.1-slim-bookworm
RUN pip install flask
WORKDIR /myapp
COPY main.py /Docker/main.py
CMD [ "python", "/Docker/main.py" ]