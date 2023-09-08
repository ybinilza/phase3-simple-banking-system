from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///banking.db')

Base = declarative_base()


class User(Base):
    __tablename__='user'

    account_no = Column(Integer(), primary_key=True)
    name = Column(String())
    account_type = Column(String())
    balance = Column(Integer())
    branch_code =Column(String())



