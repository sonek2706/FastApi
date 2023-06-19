from typing import Annotated

import requests
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import parse_raw_as

from schemas import User, UserCreate, Product, Credentials, Category

app = FastAPI()
app.mount("/static", StaticFiles(directory="templates"), name="static")

templates = Jinja2Templates(directory="templates")

# @app.get("/login", response_class=HTMLResponse)
# def index(request: Request) -> HTMLResponse:
#     return templates.TemplateResponse(
#         "login.html", {"request": request}
#     )

# @app.post("/login", response_class=HTMLResponse)
# def login(username: Annotated[str, Form()], password: Annotated[str, Form()], request: Request) -> HTMLResponse:
    
#     credentials = Credentials(username=username, password=password)
#     response = requests.post("http://localhost:8001/users", json=credentials.dict())
#     response_user = parse_raw_as(User, response.text)

#     return templates.TemplateResponse(
#         "login.html", {"request": request}
#     )


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    response = requests.get("http://localhost:8001/categories")
    response_categories = parse_raw_as(list[Category], response.text)
    return templates.TemplateResponse("home.html", {"request": request, "categories": response_categories})


@app.get("/users", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    response = requests.get("http://localhost:8001/users")
    response_users = parse_raw_as(list[User], response.text)
    return templates.TemplateResponse(
        "user.html", {"request": request, "users": response_users}
    )


@app.post("/users", response_class=HTMLResponse)
def create_user(
    username: Annotated[str, Form()], email: Annotated[str, Form()], request: Request
) -> HTMLResponse:
    request_user = UserCreate(username=username, email=email)
    response = requests.post("http://localhost:8001/users", json=request_user.dict())
    response_user = parse_raw_as(User, response.text)
    return templates.TemplateResponse(
        "user.html", {"request": request, "user": response_user}
    )


@app.get("/products/detail/{product_id}", response_class=HTMLResponse)
def index(request: Request, product_id: int) -> HTMLResponse:
    response = requests.get(f"http://127.0.0.1:8001/products/detail/{product_id}")

    response_product = parse_raw_as(Product, response.text)
    return templates.TemplateResponse(
        "product_details.html", {"request": request, "product": response_product}
    )


@app.get("/products", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    response = requests.get("http://localhost:8001/products")
    response_products = parse_raw_as(list[Product], response.text)
    return templates.TemplateResponse(
        "products.html", {"request": request, "products": response_products}
    )


@app.get("/products/{category_id}", response_class=HTMLResponse)
def index(request: Request, category_id: int) -> HTMLResponse:
    response = requests.get(f"http://localhost:8001/products/{category_id}")
    response_products= parse_raw_as(list[Product], response.text)

    response = requests.get(f"http://localhost:8001/categories/{category_id}")
    response_category = parse_raw_as(Category, response.text)

    print(response_category)
    return templates.TemplateResponse(
        "products.html", {"request": request, "products": response_products, "category": response_category}
    )