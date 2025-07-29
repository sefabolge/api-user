from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import Request
from slowapi.errors import RateLimitExceeded

from app.api.v1.routers import user
from app.core.limiter import limiter 
from app.core.config import settings

app = FastAPI(title="Line-up Coding Exercise API")


app.state.limiter = limiter

# Enable CORS for frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom exception handler for rate limits
@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded"}
    )

# Register user router
app.include_router(user.router, prefix="/api/v1")