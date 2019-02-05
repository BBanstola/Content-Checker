import os
from os.path import join, dirname, realpath

from flask import Flask, render_template, request, send_from_directory
from start import LoadFiles
from werkzeug.utils import secure_filename

# Initialize the Flask application
app = Flask(__name__)

        # This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = join(dirname(realpath(__file__)),'uploads/')
        # These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt'])

        # For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return render_template('index.html')


        # Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
                # Get the name of the uploaded files
    uploaded_files = request.files.getlist("file[]")
    filenames = []
    for file in uploaded_files:
                # Check if the file is one of the allowed types/extensions
        if file and allowed_file(file.filename):
                # Make the filename safe, remove unsupported chars
            filename = secure_filename(file.filename)
                # Move the file form the temporal folder to the upload
                # folder we setup
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # Save the filename into a list, we'll use it later
            filenames.append(filename)

    return render_template('upload.html', filenames=filenames)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/calculate', methods=['POST'])
def calculate():
    result=LoadFiles()
    return render_template('upload.html', strings=result)


if __name__ == '__main__':
    app.run(
        port=int("4000"),
        debug=True
)