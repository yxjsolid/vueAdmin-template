# /app.py
#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, render_template, redirect
from flask import Response
from flask import stream_with_context
import requests
from flask_sockets import Sockets
app = Flask(__name__)
sockets = Sockets(app)

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


#sockjs-node/911/tgmrdl5d/websocket

@sockets.route('/sockjs-node/<url>')
def handleNewClientDaemonConnect(ws):
    remote_addr = ws.environ.get("REMOTE_ADDR", "")

    print "remote_addr: ", remote_addr


    while not ws.closed:
        try:
            message = ws.receive()
        except Exception, e:
            print "error"
            print e

        if message == None:

            return
        print "msg:", message




if __name__ == '__main__':
  from gevent import pywsgi
  from geventwebsocket.handler import WebSocketHandler
  from os import popen


  print "server run"

  server = pywsgi.WSGIServer(("0.0.0.0", 5000), app.wsgi_app, handler_class=WebSocketHandler)
  server.serve_forever()


