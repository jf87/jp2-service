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
    # https://console.cloud.google.com/storage/browser/[bucket-id]/
    bucket = client.get_bucket('gcp-public-data-sentinel-2')
    # blob = bucket.get_blob("tiles/33/U/UP/S2A_MSIL1C_20150711T100006_N0204_R122_T33UUP_20160812T055924.SAFE/GRANULE/S2A_OPER_MSI_L1C_TL_EPA__20160811T174848_A000262_T33UUP_N02.04/IMG_DATA/S2A_OPER_MSI_L1C_TL_EPA__20160811T174848_A000262_T33UUP_B8A.jp2")
    # print(':'.join(hex(ord(x))[2:] for x in path))
    # print(':'.join(hex(ord(x))[2:] for x in str(path)))
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


def test_me():
    client = storage.Client()
    # https://console.cloud.google.com/storage/browser/[bucket-id]/
    bucket = client.get_bucket('gcp-public-data-sentinel-2')
    print(bucket)
    # Then do other things...
    blob = bucket.get_blob("tiles/33/U/UP/S2A_MSIL1C_20150711T100006_N0204_R122_T33UUP_20160812T055924.SAFE/GRANULE/S2A_OPER_MSI_L1C_TL_EPA__20160811T174848_A000262_T33UUP_N02.04/IMG_DATA/S2A_OPER_MSI_L1C_TL_EPA__20160811T174848_A000262_T33UUP_B8A.jp2")
    img = blob.download_as_string()
    res, err = process_jp2(img)
    if err == None:
        print(res)
    else:
        print(err)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
