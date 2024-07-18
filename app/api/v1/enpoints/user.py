from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.models.user import User
from app.db.session import get_session

router = APIRouter()

@router.get("/", response_model=User)
def read_user(session: Annotated[Session, Depends(get_session)]):
    return {}
