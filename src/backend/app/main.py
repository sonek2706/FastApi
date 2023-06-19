from fastapi import FastAPI

from dependencies import close_db_state, db_state
from models import metadata

from routers import users as users_router
from routers import products as product_router
from routers import orders as order_router
from routers import categories as category_router
from routers import order_product as order_product_router

app = FastAPI(
    on_startup=[lambda: metadata.create_all(bind=db_state.engine)],
    on_shutdown=[lambda: close_db_state(db_state)],
)

app.include_router(router=users_router.router, prefix="/users")
app.include_router(router=category_router.router, prefix="/categories")
app.include_router(router=product_router.router, prefix="/products")
app.include_router(router=order_router.router, prefix="/orders")
app.include_router(router=order_product_router.router, prefix="/order_product")
