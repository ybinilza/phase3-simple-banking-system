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
    branch_id= Column(Integer(),ForeignKey('branch.id'))
    branch = relationship('Branch', back_populates='users')
    
    

    def __repr__(self):
        return f"Customer id :{self.id}: " \
            + f"{self.name}, " \
            + f"Branch Id :  {self.branch_id}, " \
            + f"Account Type :  {self.account_type}, " \
            + f"Account Balance :  {self.account_balance}" 



class Branch(Base):
    __tablename__ = 'branch'
    id = Column(Integer(), primary_key=True)
    branch_name=Column(String())
    branch_address= Column(String())
    branch_contactno=Column(String())
    users = relationship('User', back_populates='branch')
    employees = relationship('BankEmployeeDetails', back_populates='branch')

    def __repr__(self):
        return f"Branch : {self.id}: " \
            + f"Branch Name : {self.branch_name}, " \
            + f"Branch Address : {self.branch_address}, " \
            + f"Contact Number : {self.branch_contactno} "


class BankEmployeeDetails(Base):
    __tablename__ = 'bankemployeedetails'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    designation = Column(String())
    branch_id = Column(Integer, ForeignKey('branch.id'))
    branch = relationship('Branch', back_populates='employees')

    def __repr__(self):
        return f"Employee ID: {self.id}, Name: {self.name}, Branch ID: {self.branch_id}, Designation: {self.designation}"

