from fastapi import FastAPI
from app.api.v1 import endpoints as v1_endpoints

app = FastAPI()

app.include_router(v1_endpoints.router, prefix="/api/v1")
