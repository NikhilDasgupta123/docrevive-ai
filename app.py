from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="DocReceive AI",
    version="1.0.0"
)

@app.get("/")
def root():
    return{
        "messgae": " Running"
    }

@app.get("/health")
def health():
    return{
        "status":"ok"
    }

if __name__=="__main__":
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )