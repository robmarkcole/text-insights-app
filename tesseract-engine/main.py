import io
from PIL import Image
import pytesseract
from fastapi import FastAPI, File, UploadFile, HTTPException

app = FastAPI()


@app.get("/")
async def info():
    return """FastAPI app exposing tesseract OCR"""


@app.post("/process/")
async def process_file(file: UploadFile = File(...)):
    # Ensure that this is an image
    if file.content_type.startswith("image/") is False:
        raise HTTPException(
            status_code=400, detail=f"File '{file.filename}' is not an image."
        )
    try:

        contents = await file.read()
        pil_image = Image.open(io.BytesIO(contents))
        text = pytesseract.image_to_string(pil_image)
        return {"text": text}
    except:
        e = sys.exc_info()[1]
        raise HTTPException(status_code=500, detail=str(e))
