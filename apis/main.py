from fastapi import FastAPI

app = FastAPI()   # ← top-level, spelled exactly "app"

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/saludo/{nombre}")
def get_saludo(nombre: str):
    return {"message": f"Hola, {nombre}!"}
