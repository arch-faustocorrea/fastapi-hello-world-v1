from fastapi import FastAPI
import logging

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Create FastAPI application instance
app = FastAPI(
    title="Python FastAPI Hello World",
    description="A simple FastAPI Hello World application",
    version="1.0.0"
)

@app.get("/")
async def read_root():
    """Basic Hello World endpoint"""
    logger.info("Hello World endpoint accessed")
    return {"message": "Hello, World!"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)