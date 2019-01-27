#!/usr/bin/env python3
# python app to support list of userful web links
# myke 2019-01-27 0.1

from flask import Flask

app = Flask (__name__)

@app.route('/')
def page ():
    return "Hello, darling!"

if __name__ == "__main__":
    app.run (host="0.0.0.0", debug=True)
