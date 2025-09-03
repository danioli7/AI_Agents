from fastapi import FastAPI

app = FastAPI(title="AI Agents - Hello")

@app.get("/")
def read_root():
    return {"msg": "Hola desde FastAPI ??"}

@app.get("/saluda/{nombre}")
def saluda(nombre: str):
    return {"saludo": f"Hola, {nombre}!"}
