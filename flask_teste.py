#!/usr/bin/python3
import os
from datetime import datetime 
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return datetime.now().strftime('%d-%b-%y %H:%M:%S')
    
    


if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=80, debug=True)