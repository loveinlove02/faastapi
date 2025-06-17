from fastapi import FastAPI

app = FastAPI()

# ==================================================
# http://127.0.0.1:8001/
# ==================================================
@app.get("/")
def home():
    return {"message" : "hello world"}

# ==================================================
# http://127.0.0.1:8001/items/2
# 
# path 값으로 들어오는 문자열에서 { }로 지정된 변수는 path 파라미터. 
# ==================================================
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id" : item_id}


# uvicorn app_20250617_01:app --port=8001 --reload