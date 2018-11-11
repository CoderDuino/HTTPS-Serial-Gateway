import os
import SerialShell

from flask import Flask, request, render_template

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

def getSession(mode='r'):
    return open(os.getcwd() + '/session.txt', mode)

@app.route('/')
def index():
    with getSession() as myFile:
        return render_template("index.html", log=str(myFile.read()))

@app.route('/serial')
def mainpage():
    return '''<style>       body {            background-color: BLACK;        }        p {            font-family: monospace;            color: red;        }        button {            color: gray;            height: 30px;            width: 70px;            border: 2px outset gray;        }        #textsub {            background-color: black;            border: none;            color:white;        }    </style><p style="color:white;">Send over serial</p><hr style="color:blue;"><textarea id="textsub"></textarea><br></br><button onclick="go();">Send</button><script>    function go(){    self.location = "http://0.0.0.0:5000/send?cmd="+document.getElementById('textsub').html;    }</script>'''

@app.route('/run', methods=["POST"])
def sendcode():
    SerialShell.runCommand(request.args.get('cmd', ''))
    return SerialShell.getOutput()

if __name__ == '__main__':
    with getSession(mode="w") as myFile:
        myFile.write("")

    app.debug = True
    app.run(host='0.0.0.0')