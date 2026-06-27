from pydantic import BaseModel


# ---------- USERS ----------
class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True


# ---------- PRODUCTS ----------
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int


class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True


# ---------- NOTES ----------
class NoteCreate(BaseModel):
    user_id: int
    content: str


class NoteResponse(NoteCreate):
    id: int

    class Config:
        from_attributes = True
