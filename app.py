from flask import Flask, render_template, request,jsonify
from pymongo import MongoClient

from scrap import my_scrap

client = MongoClient('localhost', 27107)
db = client.spartadb


app = Flask(__name__)

@app.route("/")
def home():

    return render_template('index.html')

@app.route('/news')
def my_news():
    my_data = my_scrap()
    print(my_data)
    return jsonify(my_data)

if __name__ == "__main__":
    app.run('0.0.0.0', 5000,debug=True)
