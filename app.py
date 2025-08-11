from flask import Flask, Response, request, render_template
from pymongo import MongoClient
import random
import json

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # ✅ allow UTF-8 output

cs = "mongodb+srv://br5183268:ocpIrbymEoNmuKyi@all-quotes.41zmkcu.mongodb.net/"
client = MongoClient(cs)
db = client["all-quotes"]
quotes = db["my-quotes"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random-shit-motivational-quote")
def rand_quote():
    all_quotes = list(quotes.find())
    chosen = random.choice(all_quotes)
    chosen["_id"] = str(chosen["_id"])
    return Response(
        json.dumps(chosen, ensure_ascii=False, indent=2),
        content_type="application/json; charset=utf-8"
    )

@app.route("/random-shit-motivational-quote/")
def category():
    author = request.args.get("author")
    category = request.args.get("category")
    deepness = request.args.get("deepness")
    spec_dic = {}
    if author:
        spec_dic["author"] = author
    if category:
        spec_dic["category"] = category
    if deepness:
        try:
            spec_dic["deepness"] = int(deepness)
        except:
            pass
    all_quotes = list(quotes.find(spec_dic))
    chosen = random.choice(all_quotes)
    chosen["_id"] = str(chosen["_id"])
    return Response(
        json.dumps(chosen, ensure_ascii=False, indent=2),
        content_type="application/json; charset=utf-8"
    )

if __name__ == "__main__":
    app.run(debug=True)