# This is not recommended for production
FROM python:3.8
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python app.py