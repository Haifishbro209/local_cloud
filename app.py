from flask import *
import os

UPLOAD_FOLDER = 'storage/'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


files = [{"name":"wow","size": "1MB", "upload_time":"13:50"}]

@app.route("/")
def index():
    return render_template("index.html", files = files)

@app.route("/upload", methods = ["POST, GET"])
def upload():
    f = request.files['file_name']
    f.save(os.path.join(app.config["UPLOAD_FOLDER"],f.filename))
    return "ok", 200
    
@app.route("/download/<name>")
def download(name):
    path = f"storage/{name}"
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)