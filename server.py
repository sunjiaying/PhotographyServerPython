from flask import Response, Flask, request, send_file
import json
import os, sys
from thumbnails import get_thumbnail
from io import BytesIO
from thumbnails.conf import settings


execpath = os.path.dirname(os.path.realpath(sys.argv[0]))
port = 3000
rootpath = os.path.join(execpath, 'images')
baseurl = 'http://localhost:' + str(port)

settings.THUMBNAIL_PATH = os.path.join(execpath, 'thumbnails-cache')
settings.THUMBNAIL_URL = os.path.join(execpath, 'thumbnails-cache')

# 定义返回的数据结构 Photo.class
class Photo:
    def __init__(self, filename):
        self.filename = filename
        self.url = baseurl + '/original/' + filename
        self.thumbnail = baseurl + '/thumbnail/' + filename


app = Flask(__name__)

@app.route('/')
def projects():
    return 'Hello, I am PhotographyServer.'

@app.route('/list')
def list():
    data = []
    for root, dirs, files in os.walk(rootpath):
      for file in files:
        if os.path.splitext(file)[1].upper() == '.JPG': 
          filename = os.path.join(root, file)
          data.append(Photo(file).__dict__)
    
    return json.dumps(data)

@app.route("/original/<filename>")
def original(filename):
    path = rootpath + "/%s" % filename
    resp = Response(open(path, 'rb'), mimetype="image/jpeg")
    return resp

@app.route("/thumbnail/<filename>")
def thumbnail(filename):
    path = rootpath + "/%s" % filename
    print(path)
    thumbnail_filename = get_thumbnail(path, '200x200', crop='center').url
    resp = Response(open(thumbnail_filename, 'rb'), mimetype="image/jpeg")
    return resp

app.run(host='0.0.0.0', port=port)
