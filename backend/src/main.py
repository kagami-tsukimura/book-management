import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def example():
    """
    起動確認としてHello Worldを返します。
    """

    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8011)
