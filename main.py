from flask import Flask
import cv2

app = Flask(__name__)


@app.route("/")
def index():
    return "OpenCV: " + cv2.__version__


if __name__ == "__main__":
    app.run(debug=True)
