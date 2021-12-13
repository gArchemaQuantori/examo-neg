import uvicorn
from fastapi import FastAPI, File, UploadFile, Form

from app import routers

app = FastAPI()


app.include_router(routers.negation_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, debug=True)
