import flask
from PIL import Image
import pytesseract

__source__ = ""

app = Flask(__name__)


@app.route("process", methods=["POST"])
def process_file():
    data = {"success": False}
    if not flask.request.method == "POST":
        return

    if flask.request.files.get("image"):
        image_file = flask.request.files["image"]
        image_bytes = image_file.read()
        pil_image = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(pil_image)
        data["text"] = text
        data = {"success": True}
    return flask.jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
