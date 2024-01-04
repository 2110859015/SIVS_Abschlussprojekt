import json

from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://2110859015:vs4DmX2YJmxl8h5N@sivs.liavbh1.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
mydb = client["SIVS_DB"]
mycol = mydb["SIVS_Collection"]
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/dashboard', methods=['POST'])
def login(name=None):
    form_name = request.form.get('username')
    form_password = request.form.get('password')

    return render_template('dashboard.html', name=form_name)

@app.route('/users', methods=['POST'])
def check_user():
    name = request.json['name']
    password = request.json['password']

    entry = {"name": name, "password": password}
    count = mycol.count_documents(entry)

    if count > 0:
        return "OK"
    return "NOT OK!!!!!!!!!!!!!"


if __name__ == '__main__':
    app.run(debug=True)
