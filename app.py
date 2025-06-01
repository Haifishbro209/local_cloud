from flask import *
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'storage/'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


files = [{"name":"wow","size": "1MB"}]

def get_files():
    global files
    for item in os.listdir(UPLOAD_FOLDER):


@app.route("/")
def index():
    return render_template("index.html", files = files)

@app.route("/upload", methods=["POST"])
def upload():
    uploaded_files = request.files.getlist("file")
    if not uploaded_files or uploaded_files[0].filename == '':
        return 'choose a file!'

    for file in uploaded_files:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

    return f"{len(uploaded_files)} Files uploaded"


@app.route("/download/<name>")
def download(name):
    path = f"storage/{name}"
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)