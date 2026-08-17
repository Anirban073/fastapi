from fastapi import FastAPI

app = FastAPI()


# # go to hom page
# @app.get("/")
# async def prod():
#     return {"response" : "go to the product path stpid!!"}

# get request
# read aor fetch all data
@app.get("/product")
async def all_products():
    return {"response" : "all products"}

# read or fetch single data
@app.get("/product/{product_id}")
async def single_products(product_id:int):
    return {"response" : "single data fetched"
            , "product_id":product_id}
    
    

# create or insert data
@app.post("/product")
async def create_product(new_product:dict):
    return {"response" : "product created", "new_product":new_product}



# update complete data
@app.put("/product/{product_id}")
async def update_product(new_updated_product:dict, product_id:int):
    return {"response" : "product updated", "new_updated_product":new_updated_product, "product_id":product_id}


# update partial data
@app.patch("/product/{product_id}")
async def partial_updated_product(new_updated_product:dict, product_id:int):
    return {"response" : "product updated partially", "new_updated_product":new_updated_product, "product_id":product_id}


# delete data
@app.delete("/product/{product_id}")
async def delete_product(product_id:int):
    
    return {"response" : "product deleted ","product_id":product_id}