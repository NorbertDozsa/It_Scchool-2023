from fastapi import FastAPI

app = FastAPI()


@app.get("/process_url/{url}")
def process_url(url: str):
    # Perform operations with the URL
    return {"url": url}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)