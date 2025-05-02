from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ยินดีต้อนรับสู่ระบบหมอฟิกส์!"}