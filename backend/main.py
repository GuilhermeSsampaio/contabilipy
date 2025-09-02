import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()
INTERFACE_URL = os.getenv("INTERFACE_URL", "http://localhost:8501")

@app.get("/")
def root():
    return "Rota home"

@app.get("/health")
def health():
    return {"status":"ok"}

@app.get("/interface")
def interface():
        return RedirectResponse(INTERFACE_URL)


