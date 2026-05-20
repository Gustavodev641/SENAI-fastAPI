from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API SENAI rodando!"}

@app.get("/health")
def health():
    return {"status": "ok"}
