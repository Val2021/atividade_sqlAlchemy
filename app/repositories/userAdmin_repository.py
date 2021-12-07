from fastapi.param_functions import Depends
from app.db.db import get_db
from app.models.models import User
from .base_repository import BaseRepository
from sqlalchemy.orm import Session


class UserAdminRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, User)