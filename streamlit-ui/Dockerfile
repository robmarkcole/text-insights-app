FROM python:3.8
LABEL maintainer="Robin Cole @robmarkcole"

EXPOSE 8501

RUN mkdir -p /home/streamlit-ui
WORKDIR /home/streamlit-ui

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /home/streamlit-ui

ENTRYPOINT [ "streamlit", "run"]
CMD ["ui.py"]