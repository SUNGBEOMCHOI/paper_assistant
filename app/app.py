from flask import Flask, send_from_directory, render_template

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/pdf/<filename>')
def pdf_viewer(filename):
    # Adjust the path according to your project structure
    return send_from_directory('database/pdf', filename)

@app.route('/view-pdf')
def view_pdf():
    return render_template('pdf_viewer.html')