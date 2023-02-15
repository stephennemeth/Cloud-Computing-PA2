from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os, subprocess

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'cc', 'cpp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return "This is the about page"

@app.route("/result", methods=['POST'])
def grade():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    (score, submission) = grade()
    return render_template("result.html", score=score, submission=submission)

def grade():
    subprocess.call("rm -f ./a.out", shell=True)
    retcode = subprocess.call("/usr/bin/g++ uploads/walk.cc", shell=True) 

    if retcode:
        print("failed to compile walk.cc")
        exit()

    subprocess.call("rm -f ./output", shell=True) 
    retcode = subprocess.call("./test.sh", shell=True)
    submission = ''
    with open('uploads/walk.cc','r') as fs:
        submission = fs.read().replace('\n','<br>')
    
    return (retcode, submission)


if __name__ == "__main__":
    app.run(debug=True)