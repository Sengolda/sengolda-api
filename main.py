from quart import *
import random
import uuid

app = Quart(__name__)
app.config["SECRET_KEY"] = str(uuid.uuid4())


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
        fact = get_random_line("storage/facts.txt") # Get a new fact.
    
    return jsonify({"text": fact, "fact": fact})

@app.route("/api/website")
async def get_random_website():
    web_site = get_random_line("storage/websites.txt")
    if web_site == "": # If it's an empty line
        web_site = get_random_line("storage/facts.txt") # Get a new site.
    
    return jsonify({"text": web_site, "website": web_site, "site": web_site})

if __name__ == "__main__":
    app.run(debug=True)
