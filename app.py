from Email import email
from datetime import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/send_email', methods=['POST','GET'])
def send_email():
    if request.method == 'POST':
        data = request.get_json()
        print(data['to'], '===>' , data['content'])
        try:
            gm = email.Gmail(data['to'],data['username'], data['password'])
            gm.send_message(
                'Python Email'+datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), 
                data['content']
                )
            return 'true'
        except BaseException as BE:
            return 'false'