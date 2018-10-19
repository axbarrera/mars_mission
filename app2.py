import sys
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars_sequel_2
app = Flask(__name__)


client = pymongo.MongoClient()
db = client.mars_mission
db.mars_stuff.drop()
collection = db.mars_stuff


@app.route('/scrape')
def scrape():
   # db.collection.remove()
    mars = scrape_mars_sequel_2.scrape()
    print("\n")
    db.mars_stuff.insert_one(mars)
    return home()

@app.route("/")
def home():
    mars = list(db.mars_stuff.find())
    print(mars)
    return render_template("index.html", mars = mars)


if __name__ == "__main__":
    app.run(debug=True)
