from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

@app.route('/assets/<path:filename>')
def serve_file(filename):
    public_dir = os.path.join(app.root_path, 'public')
    try:
        return send_from_directory(public_dir, filename)
    except FileNotFoundError:
        abort(404)

@app.route('/')
def index():
    views_dir = os.path.join(app.root_path, 'views')
    return send_from_directory(views_dir, "index.html")

if __name__ == '__main__':
    app.run(debug=True)