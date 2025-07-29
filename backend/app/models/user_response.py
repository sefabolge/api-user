from pydantic import BaseModel

class SupportInfo(BaseModel):
    url: str
    text: str

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    avatar: str

class FullUserResponse(BaseModel):
    data: UserResponse
    support: SupportInfo