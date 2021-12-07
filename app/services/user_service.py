from fastapi import  Depends,status,HTTPException
from app.models.models import  User
from app.repositories.user_repository import  UserRepository
from app.api.user.schemas import UserSchema
import bcrypt




class UserService:
    def __init__(self, user_repository:   UserRepository = Depends()):
                self.user_repository = user_repository
                

    def create_user(self, email,user: UserSchema):
        email_DB = self.user_repository.find_by_email(email)
        if  email_DB:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Ja existe um email para esse usuário")
        user.password = bcrypt.hashpw(
        user.password.encode('utf8'), bcrypt.gensalt())
        self.user_repository.create(User(**user.dict())) 

    
    def update_user(self,user: UserSchema):
        if not   self.user_repository.find_email_id(self.user.id,self.user.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Ja existe um usuário para esse email")
        user.password = bcrypt.hashpw(
        user.password.encode('utf8'), bcrypt.gensalt())
        self.user_repository.update(User(**user.dict())) 
        

        
