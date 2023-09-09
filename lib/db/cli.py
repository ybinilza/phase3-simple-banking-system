
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import User,Branch
import ipdb; 
#ipdb.set_trace()






if __name__ == '__main__':
    print('Welcome to my Simple Banking System ')
    print("Please select the following options ")
    print(" 1. Show Customer Details \n 2. Add User \n 3. Deposit Money \n 4. Withdraw Money \n 5. Check Balance ")
    choice=input("Enter your choice : ")

