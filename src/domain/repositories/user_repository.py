from sqlalchemy.sql.elements import and_
from sqlalchemy.orm import joinedload
from src.domain.models.qrcode_model import CreateQrcodeModel, QrcodeModel
from src.domain.models.user_model import UserModel
from src.infra.entity import User
from src.infra.entity.qrcode_entity import Qrcode
from src.shared.repository.base_repository import BaseRepository

class UserRepository(BaseRepository):

    def get_user(self,id:int = None,**kwargs):
        
        query = self.session.query(User)
        if id:
            user_entity = query.options(
                    joinedload(User.qrcode)
                ).filter(User.id == id).first()
        else:
            filter_list = []
            for key in kwargs.keys():
                filter_list.append(getattr(User, key) == kwargs[key])
            user_entity = query.options(
                    joinedload(User.qrcode)
                ).filter(and_(True,*filter_list)).first()
        if user_entity:
            return UserModel.from_orm(user_entity)
        return None
    
    def get_qrcode(self,id:int = None,**kwargs):
        
        query = self.session.query(Qrcode)
        if id:
            user_entity = query.options(
                    joinedload(Qrcode.user)
                ).filter(Qrcode.id == id).first()
        else:
            filter_list = []
            for key in kwargs.keys():
                filter_list.append(getattr(Qrcode, key) == kwargs[key])
            user_entity = query.options(
                    joinedload(Qrcode.user)
                ).filter(and_(True,*filter_list)).first()
        if user_entity:
            return QrcodeModel.from_orm(user_entity)
        return None
    
    def create(self,create_user_model):

        user_entity = User()
        for create_user_model_field in list(create_user_model.dict().keys()):
            setattr(user_entity,create_user_model_field,getattr(create_user_model,create_user_model_field))

        self.model = user_entity
        self.save()
        return self.get_user(self.model.id)
    
    def create_qrcode(self,create_qrcode_model: CreateQrcodeModel):

        qrcode_entity = Qrcode()
        for create_qrcode_model_field in list(create_qrcode_model.dict().keys()):
            setattr(qrcode_entity,create_qrcode_model_field,getattr(create_qrcode_model,create_qrcode_model_field))

        self.model = qrcode_entity
        self.save()
        return self.get_qrcode(self.model.id)
