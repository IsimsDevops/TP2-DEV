
from fastapi import FastAPI
import socket

app = FastAPI()

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

@app.post("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Division par zéro impossible"}
    return {"result": a / b}

@app.post("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}
