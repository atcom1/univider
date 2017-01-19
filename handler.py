#coding=utf-8
import json

from flask import Flask, request, jsonify

from fetcher import fetch_page

app = Flask(__name__)

@app.route("/crawl", methods=['GET', 'POST'])
def crawl():

    # parse needs
    data = request.get_data()
    params  = json.loads(data)

    # handle needs
    result = fetch_page(params)

    # return needs
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5010,debug=True)