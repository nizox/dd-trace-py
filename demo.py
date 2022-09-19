"""

Install the requirements:

    python3 -m venv env
    source env/bin/activate

    pip install git+https://github.com/nizox/dd-trace-py.git@nicolas.vivet/demo-rc
    pip install flask

    DD_TRACE_DEBUG=1 DD_SERVICE=test-3 DD_ENV=staging DD_REMOTECONFIG_POLL_SECONDS=5 ddtrace-run python demo.py


Test the app:
    curl http://localhost:5000/attack\?test\=\<script\>alert\(\)

"""
import logging
from flask import Flask

from ddtrace import patch_all

patch_all()

app = Flask(__name__)


@app.route("/")
@app.route("/<path:path>")
def hello_world(path):
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app.run("localhost", 5000, debug=False)
