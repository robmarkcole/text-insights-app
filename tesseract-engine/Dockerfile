FROM ubuntu:18.04
RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    python3 \
    #python-setuptools \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove


ADD . /home/App
WORKDIR /home/App
COPY requirements.txt ./
COPY . .

RUN pip3 install -r requirements.txt

VOLUME ["/data"]
EXPOSE 5000 5000
CMD ["python3" ,"app.py"]