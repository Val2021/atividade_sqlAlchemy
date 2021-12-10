from fastapi.param_functions import Depends
from app.db.db import get_db
from app.models.models import User
from .base_repository import BaseRepository
from sqlalchemy.orm import Session
from .crud.delete import CRUDDelete


class UserRepository(BaseRepository,CRUDDelete):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, User)

    def find_by_email(self, email):
        return self.session.query(self.model).filter_by(email=email).first()
    
    def find_email_id(self, id, email):
        query = self.session.query(self.model).filter_by(id=id,email=email).first()
        return query != None
    
    #new
    def remove(self, id):
        self.query().filter_by(id=id).delete()