from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings


def init_app() -> FastAPI:
    app = FastAPI(**settings.fastapi_kwargs)

    # CORS跨域
    app.add_middleware(CORSMiddleware, **settings.fastapi_cors_kwargs)

    # 路由
    # app.include_router(router)

    return app


app = init_app()
