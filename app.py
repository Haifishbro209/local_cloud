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
    files = []
    for item in os.listdir(UPLOAD_FOLDER):
        item_path = os.path.join(UPLOAD_FOLDER, item)
        size = os.path.getsize(item_path)
        files.append({"name":str(item), "size": format_size(size)})


def format_size(bytes):
    for einheit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.2f} {einheit}"
        bytes /= 1024
    return f"{bytes:.2f} PB"

@app.route("/")
def index():
    get_files()
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