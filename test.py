from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hendler():
	return {
			"message": "hello world"
			}