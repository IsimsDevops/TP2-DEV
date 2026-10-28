
from fastapi import FastAPI
import socket

app = FastAPI()
items = {
    1: {"name": "Produit A"},
    2: {"name": "Produit B"}
}
@app.get("/")
def read_root():
    return {"message": "it works !"}

@app.get("/addition")
def addition(a: int, b: int):
    return {
        "result a+b=": a + b,
        "developer": "Dev1"
    }
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()

@app.get("/greeting")
def greeting(name: str):
    return {
        "message": f"Hello, {name}",
        "developer": "Dev2",
        "hostname": socket.gethostname(),
        "IP": get_local_ip()
    }

@app.put("/update/{id}")
def update_item(id: int, name: str):
    if id not in items:
        return {"error": "Élément introuvable"}
    items[id]["name"] = name
    return {"message": "Élément modifié", "item": items[id]}