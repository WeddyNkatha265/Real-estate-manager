import sys
import os
import re

# sys.path.append adds the parent directory to the system path.
# This is necessary because the `models` folder is located in the parent directory.
# Without this, Python wouldn't be able to locate and import the `models` package.
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# Importing necessary components from SQLAlchemy
from sqlalchemy import create_engine  # Used to create a connection to the SQLite database
from sqlalchemy.orm import sessionmaker  # Used to create session objects for DB transactions

# Importing the Base class and ORM models (Agent, Property, Buyer) from the `models` package.
# These models represent the database tables.
from models import Base, Agent, Property, Buyer

# Importing `tabulate` for formatting output in a tabular format in the CLI.
from tabulate import tabulate

# Creating an engine that connects to the SQLite database.
# The database is named `real_estate.db` and will be created if it doesn't exist.
engine = create_engine('sqlite:///real_estate.db')

# Binds the engine to the Base class, allowing the models defined in Base
# (Agent, Property, Buyer) to interact with the database schema.
Base.metadata.bind = engine

# sessionmaker is a factory for session objects.
# Sessions are the intermediate between the Python code and the database,
# allowing you to query, add, and commit changes.
DBSession = sessionmaker(bind=engine)

# Creating a new session to start interacting with the database.
session = DBSession()

# Function to display the main menu of the CLI.
# It prints the available options for the user to interact with the system.
def display_menu():
    print("\nReal Estate Manager CLI")
    print("1. Add Agent")
    print("2. Add Property")
    print("3. Add Buyer")
    print("4. View All Agents")
    print("5. View All Properties")
    print("6. View All Buyers")
    print("7. Express Interest in Property")  # New option for many-to-many relationship
    print("8. View Buyer's Interested Properties")  # New option to view many-to-many relationship
    print("9. Exit")


# Function to add a new agent to the system.
# It takes the agent's name and phone number as input and creates a new Agent object.
def add_agent():
    # User input for the agent's name and phone number
    name = input("Enter agent name: ")
    phone = input("Enter agent phone: ")
    
    # Create a new Agent object using the input data
    new_agent = Agent(name=name, phone=phone)
    
    # Add the new Agent object to the session (staging it for committing to the DB)
    session.add(new_agent)
    
    # Commit the session to persist the new agent into the database
    session.commit()
    
    print("Agent added successfully.")  # Confirmation message for the user

# Function to add a new property to the system.
# It takes the property's name, price, and associated agent's ID as input and creates a new Property object.
def add_property():
    # User input for the property's name, price, and the ID of the agent managing it
    name = input("Enter property name: ").strip()
    if not name:
        print("Error: Property name cannot be empty.")
        return

    try:
        price = int(input("Enter property price: "))  # Ensuring price is an integer
        if price <= 0:
            print("Error: Price must be a positive integer.")
            return
    except ValueError:
        print("Error: Invalid input for price. Please enter a valid integer.")
        return

    try:
        agent_id = int(input("Enter agent ID: "))  # Ensuring agent ID is an integer
        # Check if the agent ID exists in the database
        agent = session.query(Agent).filter_by(id=agent_id).first()
        if not agent:
            print("Error: No agent found with the given ID.")
            return
    except ValueError:
        print("Error: Invalid input for agent ID. Please enter a valid integer.")
        return
    # Create a new Property object with the input values, linking it to the agent by agent_id
    new_property = Property(name=name, price=price, agent_id=agent_id)
    
    # Add the new Property object to the session (staging it for committing to the DB)
    session.add(new_property)
    
    # Commit the session to persist the new property into the database
    session.commit()
    
    print("Property added successfully.")  # Confirmation message for the user

# Function to add a new buyer to the system.
# It takes the buyer's name and email as input and creates a new Buyer object.

def is_valid_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

def add_buyer():
    # User input for the buyer's name and email address
    name = input("Enter buyer name: ")
    email = input("Enter buyer email: ")
    if not is_valid_email(email):
        print("Error: Invalid email format.")
        return
    
    # Create a new Buyer object using the input data
    new_buyer = Buyer(name=name, email=email)
    
    # Add the new Buyer object to the session (staging it for committing to the DB)
    session.add(new_buyer)
    
    # Commit the session to persist the new buyer into the database
    session.commit()
    
    print("Buyer added successfully.")  # Confirmation message for the user

# Function to display all agents currently stored in the system.
# It queries the database for all Agent objects and prints them in a table format.
def view_all_agents():
    # Query the session to retrieve all Agent objects from the database
    agents = session.query(Agent).all()
    
    # Display the agents in a tabular format (using tabulate)
    # Each row contains the agent's ID, name, and phone number
    print(tabulate([[agent.id, agent.name, agent.phone] for agent in agents], headers=["ID", "Name", "Phone"]))

# Function to display all properties currently stored in the system.
# It queries the database for all Property objects and prints them in a table format.
def view_all_properties():
    # Query the session to retrieve all Property objects from the database
    properties = session.query(Property).all()
    
    # Display the properties in a tabular format (using tabulate)
    # Each row contains the property's ID, name, price, and the ID of the agent managing it
    print(tabulate([[prop.id, prop.name, prop.price, prop.agent_id] for prop in properties], headers=["ID", "Name", "Price", "Agent ID"]))

# Function to display all buyers currently stored in the system.
# It queries the database for all Buyer objects and prints them in a table format.
def view_all_buyers():
    # Query the session to retrieve all Buyer objects from the database
    buyers = session.query(Buyer).all()
    
    # Display the buyers in a tabular format (using tabulate)
    # Each row contains the buyer's ID, name, and email address
    print(tabulate([[buyer.id, buyer.name, buyer.email] for buyer in buyers], headers=["ID", "Name", "Email"]))

def express_interest_in_property():
    buyer_id = int(input("Enter buyer ID: "))
    
    # Check if the buyer exists
    buyer = session.query(Buyer).filter_by(id=buyer_id).first()
    if not buyer:
        print("Error: No buyer found with the given ID.")
        return

    property_id = int(input("Enter property ID: "))
    
    # Check if the property exists
    property = session.query(Property).filter_by(id=property_id).first()
    if not property:
        print("Error: No property found with the given ID.")
        return

    # Add the property to the buyer's interested_properties list
    buyer.interested_properties.append(property)
    
    # Commit the changes to the database
    session.commit()
    
    print(f"Buyer {buyer.name} is now interested in property {property.name}.")

def view_buyer_interested_properties():
    buyer_id = int(input("Enter buyer ID: "))

    # Check if the buyer exists
    buyer = session.query(Buyer).filter_by(id=buyer_id).first()
    if not buyer:
        print("Error: No buyer found with the given ID.")
        return

    # Print out all the properties this buyer is interested in
    if buyer.interested_properties:
        print(f"Buyer {buyer.name} is interested in the following properties:")
        print(tabulate([[prop.id, prop.name, prop.price] for prop in buyer.interested_properties], headers=["ID", "Name", "Price"]))
    else:
        print(f"Buyer {buyer.name} is not interested in any properties yet.")


# The main function that controls the flow of the application.
# It continuously displays the menu and executes the corresponding function based on user input.
def main():
    while True:  # Loop to keep the CLI running until the user chooses to exit
        display_menu()  # Display the menu options
        
        # Get user input (menu option)
        choice = input("Enter choice: ")
        
        # Based on the user's choice, call the corresponding function
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
            express_interest_in_property()  # Call the new function to express interest
        elif choice == '8':
            view_buyer_interested_properties()  # Call the new function to view interested properties
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# This ensures that the `main()` function is only executed when the script is run directly
# It prevents the function from being run if the script is imported as a module
if __name__ == '__main__':
    main()
