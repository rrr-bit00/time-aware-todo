from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    username = Column(String, nullable = False)
    email = Column(String, unique = True, index = True, nullable = False)
    hash_pass = Column(String, nullable = Falses)
