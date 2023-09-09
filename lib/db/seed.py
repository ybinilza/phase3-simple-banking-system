from models import User,Branch
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from random import choice as rc
import random
from faker import Faker


engine = create_engine('sqlite:///banking.db')
Session = sessionmaker(bind=engine)
session = Session()

# creating a faker instance
faker = Faker()

# generating 10 sample users to fill the database
users = []
account_types = ['Checking', 'Saving', 'High Interest Savings']
for i in range(10):
    user = User(
        name=faker.user_name(),
        account_type=random.choice(account_types),
        account_balance=random.randint(1000,100000)
    )
    users.append(user)

session.add_all(users)
session.commit()
