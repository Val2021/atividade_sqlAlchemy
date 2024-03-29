from app.models.models import Base
from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, session, model):
        self.session = session
        self.model = model
    
    ##neww
    def query(self):
        return self.session.query(self.model)

    def get_all(self):
        return self.session.query(self.model).all()

    def create(self, model: Base):
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model

    def update(self, id: int, attributes: dict):
        self.query().filter_by(id=id).update(attributes)
        self.session.commit()
        return self.query().filter_by(id=id).first()

    def get_by_id(self, id: int):
        return self.session.query(self.model).filter_by(id=id).first()
    
    # def delete(self,id:int):
    #     self.session.query(self.model).filter_by(id=id).delete()
    #     self.session.commit()

    ##new
    def filter(self, args):
        return self.query().filter_by(**args).all()
    
    def remove(self, id):
        self.query().filter_by(id=id).delete()
        self.session.commit()
