import os
from flask import Flask, request, redirect, url_for, jsonify
from werkzeug import secure_filename
import sys

# assumes run from flaskapp directory
sys.path.append("../vision")
import locate
import db

UPLOAD_FOLDER = 'app/static'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def root():
    return app.send_static_file('index.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/wonders/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename.lower()):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            match = locate.find_match(path)
            del match["_id"]
            return jsonify(**match)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route("/guide/", methods=['GET', 'POST'])
def upload_guide_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename.lower()):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            match = locate.find_match(path, db.db.guide)
            del match["_id"]
            return jsonify(**match)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug = True)
