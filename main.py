import random
import uuid

import pymongo
from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse as jsonify
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from config import mongo_db_url

app = FastAPI(debug=True)
mongo_cluster = pymongo.MongoClient(mongo_db_url)
db = mongo_cluster["Sengolda-Api"]


def get_random_line(file):
    with open(file, "r", encoding="utf-8") as fp:
        lines = fp.read().splitlines()
        return random.choice(lines)


def check_request(request: Request):
    key = request.headers.get("Authorization", None)
    if not key:
        return None
    else:
        col = db["api_keys"]
        k = col.find({"key": key})
        k = list(k)
        try:
            k_dict = k[0]
        except Exception:
            return None

        if len(k_dict.keys()) == 0:
            return False
        else:
            return True


@app.get("/api/register")
async def register_for_the_api(request: Request):
    random_key = str(uuid.uuid4())
    col = db["api_keys"]
    col.insert_one({"key": random_key})
    return jsonify({"sucess": True, "key": random_key})


@app.get("/", response_class=HTMLResponse)
@app.get("/home", response_class=HTMLResponse)
async def hello():
    return open("templates/index.html", "r", encoding="Utf-8").read()


@app.get("/api", response_class=RedirectResponse)
async def json():
    return RedirectResponse(url="/")


@app.get("/api/fact", response_class=jsonify)
async def get_fact(request: Request):
    check = check_request(request=request)
    if not check:
        return status.HTTP_401_UNAUTHORIZED

    fact = get_random_line("storage/facts.txt")
    if fact == "":  # If it's an empty line
        fact = get_random_line("storage/facts.txt")  # Get a new fact.

    return jsonify({"text": fact, "fact": fact})


@app.get("/api/website", response_class=jsonify)
async def get_random_website(request: Request):
    check = check_request(request=request)
    if not check:
        return status.HTTP_401_UNAUTHORIZED

    web_site = get_random_line("storage/websites.txt")
    if web_site == "":  # If it's an empty line
        web_site = get_random_line("storage/websites.txt")  # Get a new site.

    return jsonify({"text": web_site, "website": web_site, "site": web_site})


@app.get("/api/cat", response_class=jsonify)
@app.get("/api/cats", response_class=jsonify)
async def get_random_cat(request: Request):
    check = check_request(request=request)
    if not check:
        return status.HTTP_401_UNAUTHORIZED

    url = get_random_line("storage/cats.txt")
    if url == "":  # If it's an empty line
        url = get_random_line("storage/cats.txt")  # Get a new image.

    return jsonify({"file": url, "url": url})


@app.exception_handler(StarletteHTTPException)
async def handle_http_exception(request, exc):
    return RedirectResponse("/")
