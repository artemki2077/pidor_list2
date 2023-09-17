from flask import Flask, render_template, jsonify, request
import json
import redis
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

r = redis.StrictRedis(host='artemki77.ru', port=6379, password=os.getenv('password_db'), decode_responses=True, db=1)



@app.route('/')
def main():

    

    return render_template('index.html', pidors=pidors, enumerate=enumerate)

@app.route('/login')
def login():
    return render_template('login.html', pidors=pidors, enumerate=enumerate)



if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)