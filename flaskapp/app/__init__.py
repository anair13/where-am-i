import os
from flask import Flask, request, redirect, url_for, jsonify
from werkzeug import secure_filename

sys.path.append("../../vision")
import locate

UPLOAD_FOLDER = 'app/static'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            match = locate.find_match(filename)
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
