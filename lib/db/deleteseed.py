from models import User,Branch,BankEmployeeDetails
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from random import choice as rc
import random
from faker import Faker

engine = create_engine('sqlite:///banking.db')
Session = sessionmaker(bind=engine)
session = Session()


session.query(Branch).delete()
session.query(User).delete()
session.query(BankEmployeeDetails).delete()
session.commit()
