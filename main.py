from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
def root(request: Request):

    return templates.TemplateResponse(name='router.html', context={'request': request})


@app.get('/square')
def square(request: Request):
    return templates.TemplateResponse(name='form_square.html',
                                      context={'request': request})


@app.post('/square')
def square(request: Request, length: float = Form(...)):

    return templates.TemplateResponse(name='calc.html',
                                      context={'request': request, 'data': length * length, 'type': 'square'})
