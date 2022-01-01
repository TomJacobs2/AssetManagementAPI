#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from fastapi import FastAPI

from app.api.routes import asset_route


class FastAPIApp:
    def __init__(self):
        self.app = FastAPI()
        self.app.include_router(asset_route.router)

    def get_app(self):
        return self.app


fast_api_app = FastAPIApp()
