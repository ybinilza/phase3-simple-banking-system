
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import User,Branch,engine
import ipdb; 
#ipdb.set_trace()

# Create the session
Session = sessionmaker(bind=engine)
session = Session()

#Showing All Customer details

def show_customer_details():
    customers=session.query(User).all()
    return customers
# Adding new Customer

def add_user():
    name=input("User name : ")
    print("Select Account Type")
    
    print("1. Checking \n 2. Savings \n 3. High Interest Savings ")
    choice=int(input())

    if choice == 1:
        account_type="Checking"
    elif choice == 2:
        account_type="Savings"
    elif choice == 3:
        account_type= "High Interest Savings"
    else:
        print("Invalid Choice")
    
    account_balance = input("Intial Deposit Money")


    # creating new customer instance
    user = User(name=name, account_type=account_type, account_balance=account_balance)
    # adding and commiting the new user to the database
    session.add(user)
    session.commit()
    print(f"User {name} added successfully!")

#Depositing Money
#Assume names are unique

def deposit_money(user_name):
    user = session.query(User).filter_by(name=user_name).first()
    #print(user)
    if user == None:
        print("Customer not found ")
    else: 
        print("Deposit Amount : ")
        amount=int(input())
        amount=user.account_balance + amount
        session.query(User).filter_by(name=user_name).update({User.account_balance :amount})
        session.commit()

#Withdrawing Funds

def withdraw_money(user_name):
    pass

def check_balance(user_name):
    pass



if __name__ == '__main__':
    print("Please select the following options ")
    print(" 1. Show Customer Details \n 2. Add User \n 3. Deposit Money \n 4. Withdraw Money \n 5. Check Balance ")
    choice=int(input("Enter your choice : "))
    
    if choice == 1:
       customer=show_customer_details()
       print(customer)
    elif choice == 2:
        add_user()
    elif choice == 3:
        user_name=input("Enter Account holder name : ")
        deposit_money(user_name)
    elif choice == 4:
        user_name=input("Enter Account holder name : ")
        withdraw_money(user_name)
    elif choice == 3:
        user_name=input("Enter Account holder name : ")
        check_balance(user_name)
    else:
        print("Invalid Choice")
    
    
   
    
    

#import ipdb; ipdb.set_trace()
    

