# pip install fastapi==0.115.12 uvicorn==0.34.2 fastapi[standard]
# 开启调试 fastapi dev app.py
# 运行服务 uvicorn app:app --reload

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
