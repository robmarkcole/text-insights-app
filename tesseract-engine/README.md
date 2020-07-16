# Tesseract Engine
Provides a single `process` endpoint.

## Docker
Build and run the Docker image, exposing the endpoint on port 5000:

```
docker build -t tesseract-engine .
docker run -p 8000:8000 tesseract-engine
```

Alternatively pull from dockerhub: `docker run -p 8000:8000 robmarkcole/tesseract-engine:latest`

From the root directory of this repo run: `curl -X POST "http://127.0.0.1:8000/process/" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "file=@assets/text1.jpg;type=image/jpeg"` which should return:
```
{
  "success": "true",
  "text": "This is the first line of\nthis text example.\n\nThis is the second line\nof the same text."
}
```

## Using a venv
```
source venv/bin/activate
cd tesseract-engine
uvicorn main:app --reload
```
The API docs can be viewed at `localhost:8000/docs`