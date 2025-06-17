from fastapi import FastAPI

app = FastAPI()

# ==================================================
# http://127.0.0.1:8001/
# ==================================================
@app.get("/")
def home():
    return {"message" : "hello world"}


# uvicorn app_20250617_01:app --port=8001 --reload