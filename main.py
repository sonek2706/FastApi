# from my_package.utils import operations

# print(operations.add(2,3))
# print(operations.subtract(5, 2))
# print(operations.multiply(4, 6))
# print(operations.divide(10, 5))

from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Path parameters
@app.get("/add/{x}/{y}")
def add(x : float, y : float) -> float:
    return x+y

# Query parameters
# @app.get("/increment/{x}")
# def add(x : int, y : int, z : str | None = None) -> int:
#     return x+y

    
@app.get("/increment/{x}")
def add(x : int, y : int, z : Optional[str] = None) -> int:
    print(z or "Hello")
    return x+y



@app.get("/")
async def root():
    return {"message": "Hello World"}