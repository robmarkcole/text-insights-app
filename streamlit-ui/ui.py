import streamlit as st
from PIL import Image
import io
import numpy as np
import requests

API_URL = "http://localhost:5000/process"
DEMO_IMAGE = "text1.jpg"


def pil_image_to_byte_array(image):
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, "PNG")
    return imgByteArr.getvalue()


@st.cache
def process_image(image_bytes):
    response = requests.post(API_URL, files={"image": image_bytes})
    return response


st.title("OCR with Tesseract")
img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])


if img_file_buffer is not None:
    image_bytes = pil_image_to_byte_array(Image.open(img_file_buffer))
    image_array = np.array(Image.open(img_file_buffer))

else:
    image_bytes = open(DEMO_IMAGE, "rb")
    image_array = np.array(Image.open(DEMO_IMAGE))

response = process_image(image_bytes)
if response.status_code == 200:
    processed_text = response.json()["text"]
else:
    processed_text = f"API response code {response.status_code}"

st.image(
    image_array, use_column_width=True,
)

st.header("Extracted text")
st.write(processed_text)
