#!/usr/bin/env python3
# python app to support list of userful web links
# myke 2019-01-28 0.4

from flask import Flask, url_for, render_template, request
import requests
import re
#import httplib2

app = Flask (__name__)

links = {}

@app.route('/', methods=['GET'])
def page ():
    return render_template("index.html", links=links)

@app.route('/add', methods=['POST'])
def add ():
    address = request.form ['address']
    if not address.startswith ('http'):
        address = 'http://' + address

    desc = request.form ['desc']

    text = getpage_requests(address)

    search = re.search (r'<title>([^<]+)</title>', text)
    title = search.group(1)

    links [address] = {'title' : title, 'desc' : desc}
    return render_template("index.html", links=links)

def getpage_httplib (address):
    hl = httplib2.Http(".cache")
    headers, text = hl.request (address, "GET")
    return text

def getpage_requests (address):
    #session = requests.Session()
    #session.trust_env = False
    #session.headers.update({'User-Agent': requests.user_agent})
    #page = requests.get (address, timeout=15, verify=False)
    page = requests.get (address)
    return page.text

if __name__ == "__main__":
    app.run (host="0.0.0.0", debug=True)
