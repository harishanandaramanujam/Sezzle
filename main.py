
from flask import Flask, render_template
from flask_socketio import SocketIO
from sympy import sympify
from flask_cors import CORS, cross_origin
data=[]
i=0

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app,cors_allowed_origins='*')


@app.route('/')
def session():
    return render_template('index.html')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    try:
        global i,data
        print('received my event: ' + str(json))
 
        json['message']+='='+str(sympify(json['message']))

        i+=1
        if i>10:
                data.pop(0)
        data.append(json)
        socketio.emit('my response', data)
    except:
        socketio.emit('my response', data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0',port=8000,debug=True)

