from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse as jsonify, RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

import random

app = FastAPI(debug=True)


def get_random_line(file):
    with open(file, "r", encoding="utf-8") as fp:
        lines = fp.read().splitlines()
        return random.choice(lines)


@app.get("/", response_class=HTMLResponse)
@app.get("/home", response_class=HTMLResponse)
async def hello():
    return open("templates/index.html", "r", encoding="Utf-8").read()


@app.get("/api", response_class=RedirectResponse)
async def json():
    return RedirectResponse(url="/")


@app.get("/api/fact", response_class=jsonify)
async def get_fact():
    fact = get_random_line("storage/facts.txt")
    if fact == "":  # If it's an empty line
        fact = get_random_line("storage/facts.txt")  # Get a new fact.

    return jsonify(
        {"text": fact, "fact": fact}
        )


@app.get("/api/website", response_class=jsonify)
async def get_random_website():
    web_site = get_random_line("storage/websites.txt")
    if web_site == "":  # If it's an empty line
        web_site = get_random_line("storage/facts.txt")  # Get a new site.
    
    return jsonify(
        {"text": web_site, "website": web_site, "site": web_site}
    )


@app.exception_handler(StarletteHTTPException)
async def handle_http_exception(request, exc):
    return RedirectResponse("/")
