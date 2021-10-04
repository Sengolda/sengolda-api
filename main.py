from quart import *
import random

app = Quart(__name__)

def get_random_line(file):
    with open(file, "r", encoding="utf-8") as fp:
        lines = fp.read().splitlines()
        return random.choice(lines)

@app.route("/")
async def hello():
    return await render_template("index.html")

@app.route("/api")
async def json():
    return await redirect(url_for("/"))

@app.route("/api/fact")
async def get_fact():
    fact = get_random_line("storage/facts.txt")
    if fact == "": # If it's an empty line
        fact = get_random_line() # Get a new fact.
    
    return jsonify({"text": fact, "fact": fact})


if __name__ == "__main__":
    app.run(debug=True)
