from fastapi import FastAPI

app = FastAPI()

# parameter with type
@app.get("/product/rode_nd_usb")
async def single_product_static():
    return {"response" : "single data fetched"}


@app.get("/product/{prooduct_title}")
async def single_product(prooduct_title:str):
    return {"response" : "single data fetched", "prooduct_title" : prooduct_title}

# wrong way
# @app.get("/product/rode_nd_usb")
# async def single_product_static():
#     return {"response" : "single data fetched"}