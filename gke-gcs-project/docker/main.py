from flask import Flask, request
from google.cloud import storage
import logging

app = Flask(__name__)
BUCKET_NAME = "my-new-bucket-demo"  # Use the new bucket name

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        uploaded_file = request.files.get("file")
        if uploaded_file:
            try:
                # Use the default credentials (Workload Identity)
                client = storage.Client()
                bucket = client.bucket(BUCKET_NAME)
                blob = bucket.blob(uploaded_file.filename)
                blob.upload_from_file(uploaded_file)
                return "File uploaded successfully!"
            except Exception as e:
                logging.error(f"Error uploading file: {str(e)}")
                return f"Error uploading file: {str(e)}", 500
    return '''
    <!doctype html>
    <title>Upload File</title>
    <h1>Upload File to GCS</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)