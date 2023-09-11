
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import User,Branch,engine,BankEmployeeDetails
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

branch_code= {
                "1" :'RBC Toronto', 
                "2" : 'RBC Ajax',
                "3" :'RBC Whitby',
                "4" :'RBC Niagara',
                "5" :'RBC Waterloo',
                "6" :'RBC Hamilton',
                "7"  :'RBC Calgery'
                }

def add_user():
    name=input("User name : ")
    
    print("Select branch - \n1. RBC Toronto \n2. RBC Ajax  \n3. RBC Whitby  \n4. RBC Niagara \n5. RBC Waterloo \n6. RBC Hamilton\n7. RBC Calgery" )
    id=int(input())
    print("1. Checking \n2. Savings \n13. High Interest Savings ")
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
    user = User(name=name, account_type=account_type, account_balance=account_balance, branch_id=id)
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
    user = session.query(User).filter_by(name=user_name).first()
    #print(user)
    if user == None:
        print("Customer not found ")
    else: 
        print("Please Enter Withdraw Amount : ")
        amount=int(input())
        balance=user.account_balance - amount
        if balance>=100:
            amount=user.account_balance - amount
            session.query(User).filter_by(name=user_name).update({User.account_balance :amount})
            session.commit()
        else:
            print("Sorry.. You dont have sufficient balance to withdraw funds")


        
    

def check_balance(user_name):
    user = session.query(User).filter_by(name=user_name).first()
    if user == None:
        print("Customer not found ")
    else: 
        print(f"Customer name : {user.name} Balance : {user.account_balance}")




if __name__ == '__main__':
  flag="y"
  while flag =="y":  
    print("SELECT YOUR ROLE ")
    print("-----------------")
    print("1. Banker \n2. Customer ")
    role=int(input())
   # print(" 1. Show Customer Details \n 2. Add User \n 3. Deposit Money \n 4. Withdraw Money \n 5. Check Balance ") 
    if(role == 1):
        print("Please select the following options ")
        print(" 1. View Customer Details \n 2. Add User \n")
        choice=int(input("Enter your choice : "))
        if choice == 1:
            customer=show_customer_details()
            print(customer)
        elif choice == 2:
            add_user()
        else:
            print("Invalid Input...Exiting........")
    elif role ==2:
        print("Please select the following options ")
        print(" 1. Deposit Money \n 2. Withdraw Money \n 3. Check Balance ")
        choice=int(input("Enter your choice : "))
        if choice ==1:
            user_name=input("Enter Account holder name : ")
            deposit_money(user_name)
        elif choice == 2:
            user_name=input("Enter Account holder name : ")
            withdraw_money(user_name)
        elif choice == 3:
            user_name=input("Enter Account holder name : ")
            check_balance(user_name)
        else:
            print("Invalid Input...Exiting........")
    else:
        print("Invalid Input...Exiting........")
    print("Do you want to continue : y or n ")
    flag=input();

    
    
   
    
    

#import ipdb; ipdb.set_trace()
    

