from fastapi import FastAPI
from enum import Enum

app=FastAPI()

# predefined value

# class ProductCategory(str, Enum):
#     books = "books"
#     clothing="clothing"
#     electronics="electronics"

# @app.get("/product/{category}")
# async def get_products(category:ProductCategory):
#     return {"response" : "products fetched", "category":category}



class ProductCategory(str, Enum):
    books = "books"
    clothing="clothing"
    electronics="electronics"

@app.get("/product/{category}")
async def get_products(category:ProductCategory):
    if(category == ProductCategory.books):
        return {"category":category, "message":"books are awsome"}
    
    else:
        return{"message":"unknown category"}