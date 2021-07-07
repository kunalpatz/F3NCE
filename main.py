from flask import Flask, render_template, request, url_for, send_from_directory, jsonify, redirect
from app import create_hashes

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/search', methods=['POST'])
def search():
    file_content = request.files['file'].stream.read()
    return render_template('search.html', result=create_hashes(file_content))


if __name__ == '__main__':
    app.run(port=6362)
