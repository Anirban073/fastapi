from fastapi import FastAPI

app = FastAPI()

# parameter with type
@app.get("/product/{prooduct_title}")
async def single_product(prooduct_title:str):
    return {"response" : "single data fetched", "prooduct_title" : prooduct_title}