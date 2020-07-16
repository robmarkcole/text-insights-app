FROM tiangolo/uvicorn-gunicorn:python3.7
RUN apt-get update \
    && apt-get install tesseract-ocr -y 

ADD . /home/App
WORKDIR /home/App
COPY requirements.txt ./
COPY . .

RUN pip3 install -r requirements.txt

VOLUME ["/data"]
EXPOSE 8000 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]