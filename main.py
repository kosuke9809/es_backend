from fastapi import FastAPI
from api.routers import bert,mecab
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(bert.router)
app.include_router(mecab.router)

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)