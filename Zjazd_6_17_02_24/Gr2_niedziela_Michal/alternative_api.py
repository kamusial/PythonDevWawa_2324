from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def api_test():
    return {"rate": 4.55}
