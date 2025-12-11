from fastapi import FastAPI

app = FastAPI(
    title="FootyPundit AI Backend",
    description="Backend API for FootyPundit AI — ML predictions, simulations, and analytics.",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "FootyPundit AI Backend Running"}
