from typing import Annotated

from fastapi import FastAPI, Request, Path
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.exceptions import RequestErrorModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
import requests

from app.linker import set_link_from_redis, get_link_from_redis

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

favicon_path = 'static/anger_favicon.ico'

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    name: str = ''
    price: float = 0.0
    is_in_offer: bool = None

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    read_root async function.

    :param response_class: class of response 
    :return: root navigation page
    """ 
    return templates.TemplateResponse("root.html", {"request": request})

@app.get("/main", response_class=HTMLResponse)
async def main(request: Request):
    """
    main async function.

    :param response_class: class of response 
    :return: main page with (bootstrap)
    """ 
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/items/{item_id}", response_class=HTMLResponse)
async def read_item(
    request: Request, 
    item_id: Annotated[int, Path(title='ID of the item to get', ge=0)], 
    q: str = None):
    """
    read_item async function.

    :param response_class: class of response 
    :param item_id: path parameter item id
    :param q: query parameter means nothing 
    :return: item page (html+css+js)
    """ 
    return templates.TemplateResponse("item.html", {"request": request, "item_id": item_id, "q": q})

@app.get("/create_link", response_class=HTMLResponse)
async def create_link(request: Request):
    """
    main async function.

    :param response_class: class of response 
    :return: main page with (bootstrap)
    """ 
    return templates.TemplateResponse("linker_input.html", {"request": request})

@app.get("/link/", response_class=RedirectResponse)
async def link(
    request: Request,
    link: str):
    """
    async function get link by key from redis.

    :param response_class: class of response 
    :return: redirect to link or None
    """ 
    URL = await get_link_from_redis(link)
    if URL.startswith('http'):
        return URL
    else:
        return ('/')

@app.get("/set_link", response_class=HTMLResponse)
async def set_link(
    request: Request,
    link: str):
    """
    async function to set link for key to redis.

    :param response_class: class of response 
    :return: key
    """ 
    try:
        url = await set_link_from_redis(link)
        if url:
            return templates.TemplateResponse("linker_output.html", {"request": request, "value": url})
        return url
    except Exception as e:
        # return ValueError('That link does not work!', e)
        return templates.TemplateResponse("root.html", {"request": request})
    
@app.put("/items/{item_name}")
async def update_item(item_id: int, item: Item):
    return {"Item_name": item.name, "Item_price": item.price}

@app.post("/items/{item_name}")
async def update_item(item_id: int, item: Item):
    return {"Item_name": item.name, "Item_price": item.price}
