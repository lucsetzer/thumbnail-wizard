from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

app = FastAPI()

@app.get("/")
async def home():
    return JSONResponse({"status": "ok", "service": "thumbnail-wizard"})

@app.get("/health")
async def health():
    return JSONResponse({"status": "healthy"})

# ⚠️ VERCEL REQUIREMENT: Export ASGI app as 'app'
# Don't use 'handler = app' - Vercel looks for 'app' variable
# app variable is already defined above
