from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/weight/{height}")
async def weight(height: int):
    """
    This function is used to take a height and return a weight.
    :param height: user inputs the height
    :return: weight
    :model: y = mx + b
    """
    weight = 0.5772*height - 25.165
    return {"weight": weight}
