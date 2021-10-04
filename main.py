from quart import Quart, render_template

app = Quart(__name__)

@app.route("/")
async def hello():
    return await render_template("index.html")

@app.route("/api")
async def json():
    return {"hello": "world"}

if __name__ == "__main__":
    app.run()
