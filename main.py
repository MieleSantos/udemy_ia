from fastapi import FastAPI

from udemy_ia.api.routers import router

app = FastAPI(
    description="This is an API to interact with the OpenAI model",
    version="0.1.0",
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
