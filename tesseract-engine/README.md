# Tesseract Engine
Provides a single `process` endpoint.

Build and run the Docker image, exposing the endpoint on port 5000:

```
docker build -t tesseract-engine .
docker run -p 5000:5000 tesseract-engine
```

From the root directory of this repo run: `curl -X POST -F image=@assets/text1.jpg 'http://localhost:5000/process'` which should return:
```
{
  "success": "true", 
  "text": "This is the first line of\nthis text example.\n\nThis is the second line\nof the same text."
}
```