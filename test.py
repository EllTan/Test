from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def handler():
    return {
        "Angelina! I love to look at you. )"
    }