from fastapi import FastAPI
# Version: $(date +%s) - forces fresh build
fastapi==0.104.1
uvicorn[standard]==0.24.0
app = FastAPI()

@app.get("/")
async def home():
    return {"status": "working", "test": "simple"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
