from fastapi import FastAPI,HTTPException, status

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "This server is running!"}
