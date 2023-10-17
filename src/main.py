from fastapi import FastAPI
import redis
import debugpy

app = FastAPI()

r = redis.Redis(host="redis", port=6379)
 
@app.get("/")
def root():
    return {"message": "Hello World 3333"}


@app.get("/hits")
def read_root():
    r.incr("hits")
    return {"number of hits": r.get("hits")}


@app.get("/stamps")
def read_root():
    r.incr("stamps")
    return {"number of stamps": r.get("stamps")}