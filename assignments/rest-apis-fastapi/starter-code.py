from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# To run the server, use: uvicorn starter-code:app --reload
# Visit http://127.0.0.1:8000 to see the API
# Visit http://127.0.0.1:8000/docs for automatic documentation