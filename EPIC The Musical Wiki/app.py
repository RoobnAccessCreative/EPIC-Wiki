from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/intro")
def home():
    item_list = ["item", "item", "item"]
    item_list[0] = "active"

    return render_template("index.html", item=item_list)

@app.route("/artists")
def artists():
    item_list = ["item", "item", "item"]
    item_list[1] = "active"

    return render_template("artists.html", item=item_list)

@app.route("/songlist")
def songlist():
    item_list = ["item", "item", "item"]
    item_list[2] = "active"

    with open("act1.json", 'r', encoding='utf-8') as f:
        act1 = json.load(f)

    with open("act2.json", 'r') as f:
        act2 = json.load(f)
    print(act1["Troy"]["3"]["artists"])
    return render_template("songlist.html", act1=act1, act2=act2, item=item_list)

if __name__ == "__main__":
    app.run(debug=True)
     