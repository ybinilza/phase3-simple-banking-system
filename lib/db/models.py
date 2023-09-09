from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///banking.db')

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    account_type = Column(String())
    account_balance=Column(Integer())
    branch_id=Column(Integer())

    def __repr__(self):
        return f"User {self.id}: " \
            + f"{self.name}, " \
            + f"Account Type {self.account_type}, " \
            + f"Account Balance {self.account_balance}" 



class Branch(Base):
    __tablename__ = 'branch'
    id = Column(Integer(), primary_key=True)
    branch_address= Column(String())
    branch_contactno=Column(String())

    def __repr__(self):
        return f"Branch {self.id}: " \
            + f"Branch Address{self.branch_address}, " \
            + f"Contact Number {self.branch_contactno} "

    
