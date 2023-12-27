""" 
RUN: 
- uvicorn main:app
- uvicorn main:app --reload
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="webpages/"), name="static")
app.mount("/js", StaticFiles(directory="webpages/"), name="js")

templates = Jinja2Templates(directory="webpages")


@app.get("/", response_class=HTMLResponse)
async def load_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})