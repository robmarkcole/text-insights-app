import io
import flask
from PIL import Image
import pytesseract

app = flask.Flask(__name__)


@app.route("/")
def info():
    return """Flask app exposing tesseract OCR"""


@app.route("/process", methods=["POST"])
def process_file():
    data = {"success": "false"}
    if not flask.request.method == "POST":
        return

    if flask.request.files.get("image"):
        image_file = flask.request.files["image"]
        image_bytes = image_file.read()
        pil_image = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(pil_image)
        data["text"] = text
        data["success"] = "true"
    return flask.jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
