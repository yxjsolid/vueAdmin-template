# /app.py
#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, render_template, redirect
from flask import Response
from flask import stream_with_context
import requests

app = Flask(__name__)

@app.route('/')
def index():
  print "index"
  return app.send_static_file('index.html')

@app.route('/static/js/<filename>')
def npm(filename):
    print "xxxxxxxxxxx"
    print filename

    url = "http://localhost:9528/static/js/%s"%filename

    req = requests.get(url, stream = True)
    return Response(stream_with_context(req.iter_content()), content_type = req.headers['content-type'])

    # return app.send_static_file()
    # return redirect('http://localhost:9528/static/js/%s'%filename)

if __name__ == '__main__':
    app.run(debug=True)

