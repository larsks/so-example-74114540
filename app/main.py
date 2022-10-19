from database import db
import os

from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

@app.get('/')
async def index():
    query = 'SELECT * FROM test_table'
    res = await db.fetch_all(query=query)
    return res
