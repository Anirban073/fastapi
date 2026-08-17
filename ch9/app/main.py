from fastapi import FastAPI
from enum import Enum

app=FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path:str):
    return {"you requested file at path": file_path}