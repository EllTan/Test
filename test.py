from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def hendler():
	return {
			"message": "hello world"
			}