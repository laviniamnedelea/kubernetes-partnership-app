from flask import Flask,request
import requests

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    print('Got response: ' + str(requests.get('http://business:8000/test/')))
    return 'OK'

@app.route('/give_me_partener/', methods=['POST'])
def give_me_partner():
    res = requests.post('http://business:8000/partnership/', json = request.json)
    print('Got response from Business Service http://business:8000/partnership/ ... ')
    return res.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)