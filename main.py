from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "notes-api V2 is running, 2nd instance here"}

@app.get("/health")
def health():
    return {"status": "ok"}
