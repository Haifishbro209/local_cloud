from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download/<file>")
def download_file(file):
    path = f"storage/{file}"
    return send_file(path, as_attachment= True)

app.run(debug=True)