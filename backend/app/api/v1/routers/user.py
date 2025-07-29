from fastapi import APIRouter, HTTPException
from fastapi import Request 
import httpx


from app.core.config import settings
from app.core.logger import logger
from app.core.limiter import limiter
from app.models.user_response import UserResponse, SupportInfo, FullUserResponse

router = APIRouter()

@router.get(
        "/user/{user_id}", 
        response_model=FullUserResponse, 
        tags=["Users"],
        summary="Get user by ID",
        description="Fetches a single user from the Reqres API and reformats the response."
        )
@limiter.limit("10/minute")
async def get_user(request: Request, user_id: int):
    url = f"{settings.REQRES_API_URL}/{user_id}"
    headers = {"x-api-key": settings.REQRES_API_KEY}

    logger.info(f"Requesting user {user_id} from Reqres")

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            logger.error(f"Failed to fetch user {user_id}: {e}")
            raise HTTPException(status_code=e.response.status_code, detail="User not found")

    # Parse Json response and extract user, support data
    raw = response.json()
    data = raw.get("data")
    support = raw.get("support")

    if not data:
        raise HTTPException(status_code=404, detail="User not found")

    return FullUserResponse(
        data=UserResponse(
            id=data["id"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            avatar=data["avatar"]
        ),
        support=SupportInfo(
            url=support["url"],
            text=support["text"]
        )
    )

    # # Optional shortcut if you're sure structure matches models
    # return FullUserResponse(
    # data=UserResponse(**data),
    # support=SupportInfo(**support)
    # )