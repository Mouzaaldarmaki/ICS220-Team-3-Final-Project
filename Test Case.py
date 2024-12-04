# Importing the pickle module to enable data serialization and deserialization
import pickle
# Importing all classes and functions from the PythonCode module
from PythonCode import *

# Function to save customer data to a file
def save_data(filename, data):
    with open(filename, 'wb') as file:  # Open the file in write-binary mode
        if isinstance(data, list):  # Check if the data is a list of Customer objects
            serialized_data = []  # Initialize an empty list for serialized customer data
            for customer in data:  # Iterate over each customer object in the list
                if isinstance(customer, Customer):  # Check if the current object is a Customer instance
                    # Convert the Customer object to a dictionary with relevant attributes
                    serialized_data.append({
                        "user_id": customer.get_user_id(),
                        "name": customer.get_name(),
                        "email": customer.get_email(),
                        "password": customer.get_password(),
                        "phone_number": customer.get_phone_number(),
                    })
            pickle.dump(serialized_data, file)  # Serialize and save the list of dictionaries
        else:
            pickle.dump(data, file)  # Serialize and save the raw data

# Function to load customer data from a file
def load_data(filename):
    try:
        with open(filename, 'rb') as file:  # Open the file in read-binary mode
            data = pickle.load(file)  # Deserialize the data from the file
            customers = []  # Initialize an empty list for customer objects
            for record in data:  # Iterate over each record in the deserialized data
                # Create a Customer object from the record's attributes
                customer = Customer(
                    user_id=record["user_id"],
                    name=record["name"],
                    email=record["email"],
                    phone_number=record.get("phone_number", "0000000000"),  # Default phone number if missing
                )
                # Set the password for the Customer object (default to "default123" if missing)
                customer.set_password(record.get("password", "default123"))
                customers.append(customer)  # Add the Customer object to the list
            return customers  # Return the list of Customer objects
    except FileNotFoundError:  # Handle the case where the file is not found
        return []  # Return an empty list if no data file exists

# Function to run test cases for various classes and methods
def run_test_cases():
    # Create a Theme Park instance
    park = ThemePark(1, "Ferrari", "Abu Dhabi", "9 AM - 10 PM", ["Roller Coaster", "Ferris Wheel"])
    print(park)  # Print the Theme Park object

    # Create an Admin instance
    admin = Admin(101, "Mouza", "Mouza@park.com", "admin123", 5, 1000)
    print(admin)  # Print the Admin object

    # Create various Ticket instances
    single_day_pass = SingleDayPass(1, "2024-12-02", 100)
    annual_pass = AnnualPass(2, 10.0, "2025-12-01", "Alyazia", 50)
    vip_ticket = VIPExperienceTicket(3, expedited_access=True, reserved_seating=True, availability=20)
    group_ticket = GroupTicket(4, group_discount=15.0, group_size_limit=5, availability=30)
    two_day_pass = TwoDayPass(5, "2024-12-02", "2024-12-03", 50)
    child_ticket = ChildTicket(6, age_limit=12, availability=50)

    # Print the Ticket objects
    print(single_day_pass)
    print(annual_pass)
    print(vip_ticket)
    print(group_ticket)
    print(two_day_pass)
    print(child_ticket)

    # Create a Customer instance
    customer = Customer(201, "Mahra", "Mahra@example.com", "0501234567")
    customer.set_password("mahra123")  # Set the customer's password
    print(customer)  # Print the Customer object

    # Create an Order instance with multiple tickets
    order = Order(
        301,
        customer,
        [single_day_pass, annual_pass, vip_ticket, group_ticket, two_day_pass, child_ticket],
        "2024-12-02",
        payment_status="Pending"
    )
    customer.set_order_history([order])  # Add the Order to the Customer's order history
    print(order)  # Print the Order object

    # Create a Payment instance
    payment = Payment(401, order, 2750.0, "Credit Card", "Successful")
    print(payment)  # Print the Payment object

    # Create an Invoice instance
    invoice = Invoice(501, order, payment, "2024-12-02")
    # Print the detailed invoice
    print("\n" + "-" * 30 + " Invoice Details " + "-" * 30 + "\n")
    print(invoice.generate_invoice())  # Generate and print the invoice
    print("\n" + "-" * 75 + "\n")

    # Save customer data to a file
    save_data("customer_data.pkl", [customer])  # Serialize and save the customer data

    # Load customer data from the file
    loaded_customers = load_data("customer_data.pkl")  # Deserialize the customer data
    for loaded_customer in loaded_customers:  # Iterate over the loaded Customer objects
        print(f"Loaded Customer: {loaded_customer}")  # Print each loaded Customer object

# Entry point for the script
if __name__ == "__main__":
    run_test_cases()  # Execute the test cases