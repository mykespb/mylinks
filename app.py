#!/usr/bin/env python3
# python app to support list of userful web links
# myke 2019-01-28 0.3

from flask import Flask, url_for, render_template, request
import requests
import re

app = Flask (__name__)

links = {}

@app.route('/', methods=['GET'])
def page ():
    return render_template("index.html", links=links)

@app.route('/add', methods=['POST'])
def add ():
    session = requests.Session()
    session.trust_env = False
    address = request.form ['address']
    if not address.startswith ('http'):
        address = 'http://' + address
    desc = request.form ['desc']
    page = session.get (address, timeout=15)
    search = re.search (r'<title>([^<]+)</title>', page.text)
    title = search.group(1)
    links [address] = {'title' : title, 'desc' : desc}
    return render_template("index.html", links=links)

if __name__ == "__main__":
    app.run (host="0.0.0.0", debug=True)
