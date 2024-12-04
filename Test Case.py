import pickle  # Importing the pickle module to enable data serialization and deserialization
from PythonCode import *  # Importing all classes and functions from the PythonCode module


# Function to save customer data to a file
def save_data(filename, data):
    with open(filename, 'wb') as file:
        if isinstance(data, list):  # Check if the data is a list of Customer objects
            serialized_data = []
            for customer in data:
                if isinstance(customer, Customer):
                    serialized_data.append({
                        "user_id": customer.get_user_id(),
                        "name": customer.get_name(),
                        "email": customer.get_email(),
                        "password": customer.get_password(),
                        "phone_number": customer.get_phone_number(),
                    })
            pickle.dump(serialized_data, file)
        else:
            pickle.dump(data, file)


# Function to load customer data from a file
def load_data(filename):
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            customers = []
            for record in data:
                customer = Customer(
                    user_id=record["user_id"],
                    name=record["name"],
                    email=record["email"],
                    phone_number=record.get("phone_number", "0000000000"),  # Default phone number if missing
                )
                customer.set_password(record.get("password", "default123"))  # Default password if missing
                customers.append(customer)
            return customers
    except FileNotFoundError:
        return []  # Return an empty list if no data file is found


# Function to run test cases for various classes and methods
def run_test_cases():
    # Create a Theme Park instance
    park = ThemePark(1, "Ferrari", "Abu Dhabi", "9 AM - 10 PM", ["Roller Coaster", "Ferris Wheel"])
    print(park)

    # Create an Admin instance
    admin = Admin(101, "Mouza", "Mouza@park.com", "admin123", 5, 1000)
    print(admin)

    # Create various Ticket instances
    single_day_pass = SingleDayPass(1, "2024-12-02", 100)
    annual_pass = AnnualPass(2, 10.0, "2025-12-01", "Alyazia", 50)
    vip_ticket = VIPExperienceTicket(3, expedited_access=True, reserved_seating=True, availability=20)
    group_ticket = GroupTicket(4, group_discount=15.0, group_size_limit=5, availability=30)
    two_day_pass = TwoDayPass(5, "2024-12-02", "2024-12-03", 50)
    child_ticket = ChildTicket(6, age_limit=12, availability=50)

    print(single_day_pass)
    print(annual_pass)
    print(vip_ticket)
    print(group_ticket)
    print(two_day_pass)
    print(child_ticket)

    # Create a Customer instance
    customer = Customer(201, "Mahra", "Mahra@example.com", "0501234567")
    customer.set_password("mahra123")
    print(customer)

    # Create an Order instance with multiple tickets
    order = Order(
        301,
        customer,
        [single_day_pass, annual_pass, vip_ticket, group_ticket, two_day_pass, child_ticket],
        "2024-12-02",
        payment_status="Pending"
    )
    customer.set_order_history([order])  # Add the created order to the customer's order history
    print(order)

    # Create a Payment instance
    payment = Payment(401, order, 2750.0, "Credit Card", "Successful")
    print(payment)

    # Create an Invoice instance
    invoice = Invoice(501, order, payment, "2024-12-02")
    print("\n" + "-" * 30 + " Invoice Details " + "-" * 30 + "\n")
    print(invoice.generate_invoice())
    print("\n" + "-" * 75 + "\n")

    # Save customer data to a file
    save_data("customer_data.pkl", [customer])

    # Load customer data from the file
    loaded_customers = load_data("customer_data.pkl")
    for loaded_customer in loaded_customers:
        print(f"Loaded Customer: {loaded_customer}")

# Entry point for the script
if __name__ == "__main__":
    run_test_cases()
