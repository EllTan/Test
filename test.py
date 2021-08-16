from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def handler():
    return {
        "message": "Hello World"
    }