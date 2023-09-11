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

# Delete existing data
session.query(Branch).delete()
session.query(User).delete()
session.query(BankEmployeeDetails).delete()
session.commit()



# creating a faker instance
faker = Faker()

# generating 10 sample users to fill the database
users = []
account_types = ['Checking', 'Savings', 'High Interest Savings']
for i in range(10):
    user = User(
        name=faker.user_name(),
        account_type=random.choice(account_types),
        account_balance=random.randint(1000,100000)
    )
    users.append(user)

session.add_all(users)
session.commit()

# generating 10 random Bank branch details to fill the database

branchs = []

# branch_name= ['RBC Toronto', 'RBC Ajax','RBC Whitby','RBC Niagara','RBC Waterloo','RBC Hamilton','RBC Calgery']

branch_code= {
                "1" :'RBC Toronto', 
                "2" : 'RBC Ajax',
                "3" :'RBC Whitby',
                "4" :'RBC Niagara',
                "5" :'RBC Waterloo',
                "6" :'RBC Hamilton',
                "7"  :'RBC Calgery'
                }

for i in range(7):
    branch= Branch(
        branch_name=branch_code[str(i+1)],
        branch_address=faker.address(),
        branch_contactno=faker.phone_number()
    )
    branchs.append(branch)

session.add_all(branchs)
session.commit()


# generating 10 random Bank Employee details to fill the database
employees=[]
designations_bank=["Teller","Customer Service Representative","Loan Officer","Branch Manager","Financial Advisor","Risk Analyst","Compliance Officer","Credit Analyst","Operations Manager"]
for i in range(10):
    employee = BankEmployeeDetails(
        name=faker.user_name(),
        designation=random.choice(designations_bank),
        branch_id=random.randint(1,7)
    )
    employees.append(employee)
session.add_all(employees)
session.commit()


#import ipdb; ipdb.set_trace()