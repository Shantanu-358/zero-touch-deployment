from fastapi import FastAPI

app = FastAPI(
    title="DevOps Portfolio Project",
    description="A simple FastAPI application for a DevOps portfolio",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Hello, World! Welcome to the entry-level DevOps portfolio project."}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
