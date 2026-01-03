from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"status": "working", "test": "simple"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
