from fastapi import FastAPI
import uvicorn

from api.health import router as health_router

app = FastAPI(
    title="DocReceive AI",
    version="1.0.0"
)

@app.get("/")
def root():
    return{
        "messgae": " Running"
    }

# Health check up route
app.include_router(health_router, tags=['HEALTH CHECK UP'])

if __name__=="__main__":
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )