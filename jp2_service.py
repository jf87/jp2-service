import glymur
import os
from flask import Flask
from flask import request, jsonify, abort
import io
from google.cloud import storage
import time

import tempfile
from contextlib import contextmanager

@contextmanager
def tempinput(data):
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(data)
    temp.close()
    try:
        yield temp.name
    finally:
        os.unlink(temp.name)

app = Flask(__name__)

def process_jp2(path, rlevel=-1):
    t0 = time.time()
    result = {}
    err = None
    client = storage.Client()
    bucket = client.get_bucket('gcp-public-data-sentinel-2')
    blob = bucket.get_blob(path)
    if blob == None:
        err = "Image not found"
        return None, err
    try:
        img = blob.download_as_string()
    except:
        err = "Could not download image"
        return None, err
    t1 = time.time()
    with tempinput(img) as tempfilename:
        try:
            jp2 = glymur.Jp2k(tempfilename)
            thumbnail = jp2.read(rlevel=rlevel)
            t2 = time.time()
            result = {"shape": thumbnail.shape, "img_data": thumbnail.tolist(),
                    "time_download": t1-t0, "time_processing": t2-t1}
            return result, err
        except:
            result = None
            err = "Error parsing jp2"
            return result, err

@app.route('/')
def index():
    return 'JP2 Service'

@app.route("/api/jp2", methods=["POST"])
def jp2():
    err = None
    try:
        body = request.get_json()
        path = body["path"]
        rlevel = body["rlevel"]
    except:
        err = "Bad json"
        return jsonify({"Error": err})
    res, err = process_jp2(path, rlevel)
    if err != None:
        return jsonify({"Error": err})
    print(res["shape"])
    return jsonify(res)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
