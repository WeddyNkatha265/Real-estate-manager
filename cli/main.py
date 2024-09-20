import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Agent, Property, Buyer
from tabulate import tabulate

engine = create_engine('sqlite:///real_estate.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def display_menu():
    print("\nReal Estate Manager CLI")
    print("1. Add Agent")
    print("2. Add Property")
    print("3. Add Buyer")
    print("4. View All Agents")
    print("5. View All Properties")
    print("6. View All Buyers")
    print("7. Exit")

def add_agent():
    name = input("Enter agent name: ")
    phone = input("Enter agent phone: ")
    new_agent = Agent(name=name, phone=phone)
    session.add(new_agent)
    session.commit()
    print("Agent added successfully.")

def add_property():
    name = input("Enter property name: ")
    price = int(input("Enter property price: "))
    agent_id = int(input("Enter agent ID: "))
    new_property = Property(name=name, price=price, agent_id=agent_id)
    session.add(new_property)
    session.commit()
    print("Property added successfully.")

def add_buyer():
    name = input("Enter buyer name: ")
    email = input("Enter buyer email: ")
    new_buyer = Buyer(name=name, email=email)
    session.add(new_buyer)
    session.commit()
    print("Buyer added successfully.")

def view_all_agents():
    agents = session.query(Agent).all()
    print(tabulate([[agent.id, agent.name, agent.phone] for agent in agents], headers=["ID", "Name", "Phone"]))

def view_all_properties():
    properties = session.query(Property).all()
    print(tabulate([[prop.id, prop.name, prop.price, prop.agent_id] for prop in properties], headers=["ID", "Name", "Price", "Agent ID"]))

def view_all_buyers():
    buyers = session.query(Buyer).all()
    print(tabulate([[buyer.id, buyer.name, buyer.email] for buyer in buyers], headers=["ID", "Name", "Email"]))

def main():
    while True:
        display_menu()
        choice = input("Enter choice: ")
        if choice == '1':
            add_agent()
        elif choice == '2':
            add_property()
        elif choice == '3':
            add_buyer()
        elif choice == '4':
            view_all_agents()
        elif choice == '5':
            view_all_properties()
        elif choice == '6':
            view_all_buyers()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
