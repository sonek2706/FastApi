from fastapi import FastAPI

from dependencies import close_db_state, db_state
from models import metadata
from routers import users as users_router
from routers import products as product_router

app = FastAPI(
    on_startup=[lambda: metadata.create_all(bind=db_state.engine)],
    on_shutdown=[lambda: close_db_state(db_state)],
)
app.include_router(router=users_router.router, prefix="/users")
app.include_router(router=product_router.router, prefix="/products")
