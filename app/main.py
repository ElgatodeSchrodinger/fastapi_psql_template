from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def health():
    return {
        "message": "Successful"
    }