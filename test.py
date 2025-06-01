UPLOAD_FOLDER = 'storage/'

files = [{"name":"wow","size": "1MB"}]

def get_files():
    global files
    for item in os.listdir(UPLOAD_FOLDER):
        print(item)
