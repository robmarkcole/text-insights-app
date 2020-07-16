Manually run from you venv with `streamlit run ui.py`

## Docker
Currently need to pass in IP address of computer hosting tesseract api.
```
docker build -t text-insights-app-ui .
docker run -p 8501:8501 -e TESSERACT_API_IP='192.168.1.133' text-insights-app-ui
```

## Using a venv
```
source venv/bin/activate
cd streamlit-ui/
streamlit run ui.py
```