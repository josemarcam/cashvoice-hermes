from sqlalchemy import Column, Integer, String
from src.config.database import base_entity

class Version(base_entity):
 
    __tablename__ = "version"

    ver_id = Column('ver_id', Integer, primary_key=True, autoincrement=True)
    ver_version = Column('ver_version', String(120), nullable=False, unique=True)
    ver_running = Column('ver_running', String, index=True, nullable=False)
    
    # created_at = Column('created_at', DateTime, nullable=False, server_default=func.now())
    # updated_at = Column('updated_at', DateTime, nullable=False, server_default=func.now(), server_onupdate=func.now())
