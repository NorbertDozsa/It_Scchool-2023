from fastapi import FastAPI, Request

app = FastAPI()

URL = "https://youtu.be/PGNiXGX2nLU"

@app.get("/convert/")
async def convert():
    """Returns a converted ID for the given URL"""

    
