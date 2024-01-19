FROM python:3.9
RUN pip install --upgrade pip
WORKDIR /app
COPY extractor/requirements.txt .
COPY extractor .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "-u" ,"extractor.py"]



