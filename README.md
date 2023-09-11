SIMPLE BANKING SYSTEM
-------------------------------
Description
Simple Banking System is a Python project that models a basic banking system using SQLAlchemy. 

#Features

•It allows the banker to create a new account 

•	It allows the banker to view customer details

•	It allows the customer to deposit money

•	It allows the customer to withdraw money

•	It allows the customer to check balance

#Installation

1.	 Install python version 3.8.13, pyenv, and pipenv.
2.	Clone the repository
3.	Navigate into the project directory : phase3-simple-banking-system/lib/db
4.	Install dependencies: pipenv install
5.	Enter into the virtual environment: pipenv shell
6.	Initialize alembic : alembic init alembic
7.	Create Initial Migration: alembic revision --autogenerate -m "Initial migration"
8.	Apply migration: alembic upgrade head
9.	Seed the database: python seed.py
10.	Run the application: python cli.py
    
#Licence

 MIT Licence
