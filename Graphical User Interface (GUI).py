import tkinter as tk  # Importing the Tkinter library for GUI functionality
from tkinter import ttk, messagebox  # Importing ttk for themed widgets and messagebox for dialog boxes
import pickle  # Importing pickle for data serialization and deserialization

# Mock Data
customers = {}  # Dictionary to store customer information
tickets = [  # A list of dictionaries to store ticket types and details
    {"id": 1, "type": "Single Day Pass", "price": 275.0, "validity": "1 Day", "discount": "0.0"},
    {"id": 2, "type": "Two Day Pass", "price": 480.0, "validity": "2 Days", "discount": "0.10"},
    {"id": 3, "type": "Group Ticket", "price": 220.0, "validity": "1 Day (per person)", "discount": "0.20 (for group of 20 or more)"},
    {"id": 4, "type": "Child Ticket", "price": 185.0, "validity": "1 Day", "discount": "0.0"},
    {"id": 5, "type": "VIP Experience Ticket", "price": 550.0, "validity": "1 Day", "discount": "0.0"},
    {"id": 6, "type": "Annual Membership", "price": 1840.0, "validity": "1 Year (up to 5 people)", "discount": "0.15(on renewal)"},
]
orders = []  # A list to store orders

# Data Persistence
def save_data(filename, data):  # Function to save data to a file
    # Open the specified file in write-binary ('wb') mode
    with open(filename, 'wb') as file:
        pickle.dump(data, file)  # Serialize the data using pickle and save it to the file

def load_data(filename):  # Function to load data from a file
    try:
        # Attempt to open the specified file in read-binary ('rb') mode
        with open(filename, 'rb') as file:
            return pickle.load(file)  # Deserialize the data using pickle and return it
    except FileNotFoundError:  # Handle the case where the file is not found
        return {}  # Return an empty dictionary if the file does not exist



class AccountManagement:  # Class to handle account management functionality
    def __init__(self, root, app):  # Constructor to initialize the AccountManagement interface
        self.root = root  # Reference to the root Tkinter window
        self.app = app  # Reference to the main application instance

        # Create a labeled frame titled "Account Management" with padding
        self.frame = ttk.LabelFrame(root, text="Account Management", padding=10)

        # Place the labeled frame in the root window using grid layout
        self.frame.grid(row=0, column=0, padx=20, pady=20)

        self.create_widgets()  # Call the method to create and arrange widgets within the frame

    def create_widgets(self):  # Method to create and layout widgets for account management

        # Create a label for "User ID" and place it in the grid layout
        ttk.Label(self.frame, text="User ID:").grid(row=0, column=0, padx=5, pady=5)
        self.user_id_entry = ttk.Entry(self.frame)  # Create an entry field for "User ID"
        self.user_id_entry.grid(row=0, column=1, padx=5, pady=5)  # Place the entry field in the grid layout

        # Create a label for "Name" and place it in the grid layout
        ttk.Label(self.frame, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.frame)  # Create an entry field for "Name"
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)  # Place the entry field in the grid layout

        # Create a label for "Email" and place it in the grid layout
        ttk.Label(self.frame, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = ttk.Entry(self.frame)  # Create an entry field for "Email"
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)  # Place the entry field in the grid layout

        # Create a label for "Phone Number" and place it in the grid layout
        ttk.Label(self.frame, text="Phone Number:").grid(row=3, column=0, padx=5, pady=5)  # Phone Number Label
        self.phone_number_entry = ttk.Entry(self.frame)  # Create an entry field for "Phone Number"
        self.phone_number_entry.grid(row=3, column=1, padx=5, pady=5)  # Place the entry field in the grid layout

        # Create a label for "Password" and place it in the grid layout
        ttk.Label(self.frame, text="Password:").grid(row=4, column=0, padx=5, pady=5)
        self.password_entry = ttk.Entry(self.frame, show="*")  # Create a masked entry field for "Password"
        self.password_entry.grid(row=4, column=1, padx=5, pady=5)  # Place the entry field in the grid layout

        # Create a button for adding a customer and place it in the grid layout
        ttk.Button(self.frame, text="Add Customer", command=self.add_customer).grid(row=5, column=0, pady=10)

        # Create a button for logging in a customer and place it in the grid layout
        ttk.Button(self.frame, text="Login", command=self.login_customer).grid(row=5, column=1, pady=10)

        # Create a button for modifying customer details and place it in the grid layout
        ttk.Button(self.frame, text="Modify Customer", command=self.modify_customer).grid(row=6, column=0, pady=10)

        # Create a button for deleting a customer and place it in the grid layout
        ttk.Button(self.frame, text="Delete Customer", command=self.delete_customer).grid(row=6, column=1, pady=10)

        # Create a button for viewing all customers and place it in the grid layout
        ttk.Button(self.frame, text="View Customers", command=self.view_customers).grid(row=7, column=0, columnspan=2,
                                                                                        pady=10)
    def add_customer(self):  # Method to add a new customer
        user_id = self.user_id_entry.get()  # Retrieve the entered User ID from the input field
        name = self.name_entry.get()  # Retrieve the entered Name from the input field
        email = self.email_entry.get()  # Retrieve the entered Email from the input field
        phone_number = self.phone_number_entry.get()  # Retrieve the entered Phone Number from the input field
        password = self.password_entry.get()  # Retrieve the entered Password from the input field

        # Check if the User ID already exists in the `customers` dictionary
        if user_id in customers:
            # Display an error message if the User ID already exists
            messagebox.showerror("Error", "User ID already exists.")
        else:
            # Add the new customer details to the `customers` dictionary
            customers[user_id] = {
                "name": name,  # Store the customer's Name
                "email": email,  # Store the customer's Email
                "phone_number": phone_number,  # Store the customer's Phone Number
                "password": password,  # Store the customer's Password
            }
            save_data("customers.pkl", customers)  # Save the updated customer data to the file
            # Display a success message indicating the customer was added
            messagebox.showinfo("Success", "Customer added successfully!")

    def modify_customer(self):  # Method to modify an existing customer's details
        user_id = self.user_id_entry.get()  # Retrieve the entered User ID from the input field
        name = self.name_entry.get()  # Retrieve the entered Name from the input field
        email = self.email_entry.get()  # Retrieve the entered Email from the input field
        phone_number = self.phone_number_entry.get()  # Retrieve the entered Phone Number from the input field
        password = self.password_entry.get()  # Retrieve the entered Password from the input field

        # Check if the User ID exists in the `customers` dictionary
        if user_id in customers:
            # Update the customer's details in the `customers` dictionary
            customers[user_id] = {
                "name": name,  # Update the Name
                "email": email,  # Update the Email
                "phone_number": phone_number,  # Update the Phone Number
                "password": password,  # Update the Password
            }
            save_data("customers.pkl", customers)  # Save the updated customer data to the file
            # Display a success message indicating the customer details were updated
            messagebox.showinfo("Success", "Customer details updated successfully!")
        else:
            # Show an error message if the User ID is not found in the `customers` dictionary
            messagebox.showerror("Error", "User ID not found.")

    def delete_customer(self):  # Method to delete a customer's information
        user_id = self.user_id_entry.get()  # Retrieve the entered User ID from the input field

        # Check if the User ID exists in the `customers` dictionary
        if user_id in customers:
            del customers[user_id]  # Delete the customer from the `customers` dictionary
            save_data("customers.pkl", customers)  # Save the updated customer data to the file
            # Display a success message indicating the customer was deleted
            messagebox.showinfo("Success", "Customer deleted successfully!")
        else:
            # Show an error message if the User ID is not found in the `customers` dictionary
            messagebox.showerror("Error", "User ID not found.")

    def login_customer(self):  # Method to handle customer login
        user_id = self.user_id_entry.get()  # Get the entered User ID from the input field
        password = self.password_entry.get()  # Get the entered Password from the input field

        # Check if the entered User ID exists in the `customers` dictionary and the password matches
        if user_id in customers and customers[user_id]["password"] == password:
            # Set the current customer details in the main application context
            self.app.current_customer = {
                "id": user_id,  # Store the customer's User ID
                "name": customers[user_id]["name"]  # Store the customer's name
            }
            self.app.show_ticket_purchasing()  # Navigate to the Ticket Purchasing tab
        else:
            # Show an error message if the User ID or Password is invalid
            messagebox.showerror("Error", "Invalid User ID or Password.")

    def view_customers(self):  # Method to display a list of all customers
        display_window = tk.Toplevel(self.root)  # Create a new top-level window for displaying customer details
        display_window.title("Customer List")  # Set the title of the new window

        # Create a Treeview widget to display customer information in a tabular format
        tree = ttk.Treeview(
            display_window,
            columns=("User ID", "Name", "Email", "Phone Number"),  # Define the columns for the Treeview
            show="headings"  # Display only the headings (no default column)
        )

        # Define the column headers for the Treeview
        tree.heading("User ID", text="User ID")  # Add a header for the "User ID" column
        tree.heading("Name", text="Name")  # Add a header for the "Name" column
        tree.heading("Email", text="Email")  # Add a header for the "Email" column
        tree.heading("Phone Number", text="Phone Number")  # Add a header for the "Phone Number" column

        # Place the Treeview widget on the grid with padding
        tree.grid(row=0, column=0, padx=10, pady=10)

        # Loop through all customer entries in the `customers` dictionary
        for user_id, info in customers.items():
            # Insert each customer's information into the Treeview, including phone number (default to "N/A" if missing)
            tree.insert(
                "",  # Parent item (empty string for top-level entries)
                tk.END,  # Insert at the end of the Treeview
                values=(user_id, info["name"], info["email"], info.get("phone_number", "N/A"))  # Customer details
            )

class TicketPurchasing:  # Class to manage ticket purchasing functionality
    def __init__(self, root, app):  # Constructor to initialize the TicketPurchasing interface
        self.root = root  # Root Tkinter window
        self.app = app  # Reference to the main application

        # Creating a labeled frame for ticket purchasing
        self.frame = ttk.LabelFrame(root, text="Purchase Tickets", padding=10)
        self.frame.grid(row=0, column=0, padx=20, pady=20)  # Placing the frame on the grid

        self.create_widgets()  # Call the method to create widgets

    def create_widgets(self):  # Method to create the widgets for ticket purchasing
        self.customer_label = ttk.Label(self.frame, text="")  # Label to display the current customer
        self.customer_label.grid(row=0, column=0, columnspan=2, pady=5)  # Place the label on the grid

        # Ticket selection
        ttk.Label(self.frame, text="Select Ticket:").grid(row=1, column=0, padx=5, pady=5)
        self.selected_ticket = tk.StringVar()
        ticket_types = [ticket["type"] for ticket in tickets]
        self.ticket_dropdown = ttk.Combobox(self.frame, textvariable=self.selected_ticket, values=ticket_types)
        self.ticket_dropdown.grid(row=1, column=1, padx=5, pady=5)
        self.ticket_dropdown.bind("<<ComboboxSelected>>", self.update_discount_options)  # Bind event to update discounts

        # Quantity
        ttk.Label(self.frame, text="Quantity:").grid(row=2, column=0, padx=5, pady=5)
        self.quantity_entry = ttk.Entry(self.frame)
        self.quantity_entry.grid(row=2, column=1, padx=5, pady=5)

        # Discount dropdown
        ttk.Label(self.frame, text="Select Discount:").grid(row=3, column=0, padx=5, pady=5)
        self.discount_option = tk.StringVar()
        self.discount_dropdown = ttk.Combobox(self.frame, textvariable=self.discount_option)
        self.discount_dropdown.grid(row=3, column=1, padx=5, pady=5)

        # Payment method
        ttk.Label(self.frame, text="Payment Method:").grid(row=4, column=0, padx=5, pady=5)
        self.payment_method = tk.StringVar()
        payment_methods = ["Cash", "Credit Card", "Digital Wallet"]
        self.payment_method_dropdown = ttk.Combobox(self.frame, textvariable=self.payment_method, values=payment_methods)
        self.payment_method_dropdown.grid(row=4, column=1, padx=5, pady=5)

        # Total
        self.total_label = ttk.Label(self.frame, text="Total: 0 AED")
        self.total_label.grid(row=5, column=0, columnspan=2, pady=10)

        # Buttons
        ttk.Button(self.frame, text="Calculate Total", command=self.calculate_total).grid(row=6, column=0, pady=10)
        ttk.Button(self.frame, text="Print Invoice", command=self.print_invoice).grid(row=6, column=1, pady=10)

    def update_customer_label(
            self):  # Method to update the label displaying the currently logged-in customer's information
        customer = self.app.current_customer  # Retrieve the currently logged-in customer's details from the main application
        # Update the text of the customer label to show the customer's name and ID
        self.customer_label.config(text=f"Logged in as: {customer['name']} (ID: {customer['id']})")

    def update_discount_options(self, event):  # Method to update discount options based on the selected ticket
        # Retrieve the currently selected ticket type from the dropdown
        selected_ticket = self.selected_ticket.get()

        # Find the corresponding ticket details from the list of tickets based on the selected ticket type
        ticket = next((t for t in tickets if t["type"] == selected_ticket), None)

        # If a matching ticket is found, proceed to update the discount options
        if ticket:
            # Retrieve the discount options available for the ticket, defaulting to "No discounts available" if not set
            discount_options = ticket.get("discount", "No discounts available")

            # Update the discount dropdown menu with the retrieved discount options
            self.discount_dropdown["values"] = [discount_options]

            # Set the currently selected discount option to the first (or only) available discount option
            self.discount_option.set(discount_options)

    def calculate_total(self):  # Method to calculate the total price for the selected ticket and quantity
        try:
            # Retrieve the selected ticket type from the dropdown
            selected_ticket = self.selected_ticket.get()

            # Retrieve the quantity entered by the user and convert it to an integer
            quantity = int(self.quantity_entry.get())

            # Find the matching ticket details from the list of tickets based on the selected ticket type
            ticket = next((t for t in tickets if t["type"] == selected_ticket), None)

            # If no valid ticket is selected, display an error message and exit the function
            if not ticket:
                messagebox.showerror("Error", "Please select a valid ticket.")
                return

            # Calculate the initial total price by multiplying the ticket price by the quantity
            total_price = ticket["price"] * quantity

            # Retrieve the discount associated with the ticket, defaulting to "0" if not set
            discount = ticket.get("discount", "0")

            # If the discount is a percentage (e.g., "10%"), extract the numeric value and apply the discount
            if "%" in discount:
                discount_value = float(discount.split("%")[0])  # Extract the numeric value of the discount
                total_price -= total_price * (discount_value / 100)  # Subtract the discount from the total price

            # Update the label displaying the total price with the calculated total
            self.total_label.config(text=f"Total: {total_price:.2f} AED")

            # Store the selected ticket information and calculated total for later use
            self.selected_ticket_info = {
                "ticket": ticket,  # Store ticket details
                "quantity": quantity,  # Store the quantity of tickets
                "total": total_price,  # Store the calculated total price
                "discount": discount,  # Store the applied discount
                "payment_method": self.payment_method.get(),  # Store the selected payment method
            }
        except ValueError:  # Handle invalid inputs (e.g., non-numeric values for quantity)
            # Display an error message if the quantity entered is not a valid number
            messagebox.showerror("Error", "Invalid input. Enter numbers for quantity.")

    def print_invoice(self):  # Method to generate and display the invoice
        try:
            # Retrieve the currently logged-in customer's details
            customer = self.app.current_customer

            # Retrieve the selected ticket's details and associated purchase information
            ticket_info = self.selected_ticket_info

            # Extract specific details about the selected ticket
            ticket = ticket_info["ticket"]

            # Extract the quantity of tickets purchased
            quantity = ticket_info["quantity"]

            # Extract the total price for the selected ticket and quantity
            total = ticket_info["total"]

            # Retrieve the discount applied to the purchase, default to "0" if not set
            discount = ticket_info.get("discount", "0")

            # Retrieve the payment method used for the purchase
            payment_method = ticket_info["payment_method"]

            # Format the invoice details into a readable string
            invoice = f"""
            ******** INVOICE ********
            Customer: {customer['name']} (ID: {customer['id']})
            Ticket Type: {ticket['type']}
            Price per Ticket: {ticket['price']} AED
            Quantity: {quantity}
            Discount: {discount}
            Payment Method: {payment_method}
            Total Price: {total:.2f} AED
            *************************
            """

            # Display the generated invoice in a popup message box
            messagebox.showinfo("Invoice", invoice)

            # Append the purchase details to the orders list for record-keeping
            orders.append({
                "customer": customer,  # Store customer details
                "ticket": ticket,  # Store ticket details
                "quantity": quantity,  # Store the quantity of tickets purchased
                "discount": discount,  # Store the applied discount
                "payment_method": payment_method,  # Store the payment method
                "total": total,  # Store the total price
            })
        except AttributeError:  # Handle the case where required data (e.g., total) is missing
            # Display an error message if the total has not been calculated before printing the invoice
            messagebox.showerror("Error", "Calculate total before printing the invoice.")

class AdminDashboard:
    def __init__(self, root):  # Constructor to initialize Admin Dashboard
        self.root = root  # Root Tkinter window

        # Create a labeled frame for the admin dashboard
        self.frame = ttk.LabelFrame(root, text="Admin Dashboard", padding=10)
        self.frame.grid(row=0, column=0, padx=20, pady=20)

        self.create_widgets()  # Call the method to create widgets

    def create_widgets(self):  # Method to create the widgets for admin dashboard
        ttk.Button(self.frame, text="View Purchases", command=self.view_purchases).grid(row=0, column=0, pady=10)

    def view_purchases(self):  # Method to view all purchases
        purchase_window = tk.Toplevel(self.root)  # Create a new window
        purchase_window.title("All Purchases")  # Set the title of the window

        # Create a Treeview widget to display purchases
        tree = ttk.Treeview(
            purchase_window, # The parent window where the Treeview will be placed
            columns=("Customer ID", "Name", "Ticket", "Quantity", "Discount", "Total", "Payment Method"), # Define the columns for the Treeview widget
            show="headings" # Only display the column headers, not a default column for row numbers
        )

        # Define column headings for vlear visual
        tree.heading("Customer ID", text="Customer ID")
        tree.heading("Name", text="Name")
        tree.heading("Ticket", text="Ticket")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Discount", text="Discount (%)")
        tree.heading("Total", text="Total (AED)")
        tree.heading("Payment Method", text="Payment Method")

        # Define column widths for better readability
        tree.column("Customer ID", width=100)
        tree.column("Name", width=150)
        tree.column("Ticket", width=200)
        tree.column("Quantity", width=100)
        tree.column("Discount", width=120)
        tree.column("Total", width=100)
        tree.column("Payment Method", width=150)

        tree.grid(row=0, column=0, padx=10, pady=10)  # Place the Treeview widget in the window

        # Insert orders into the Treeview
        for order in orders:
            customer = order["customer"]
            tree.insert(
                "",
                tk.END,
                values=(
                    customer["id"],  # Customer ID
                    customer["name"],  # Customer Name
                    order["ticket"]["type"],  # Ticket Type
                    order["quantity"],  # Quantity
                    order.get("discount", "0%"),  # Discount Applied
                    f"{order['total']:.2f} AED",  # Total Price
                    order["payment_method"]  # Payment Method
                )
            )

# Main Application
class ThemeParkApp:  # Main application class to manage the entire system
    def __init__(self, root):  # Constructor to initialize the main application
        self.root = root  # Root Tkinter window
        self.root.title("Theme Park Management System")  # Set the title of the application

        self.current_customer = None  # Initialize the current customer as None

        tab_control = ttk.Notebook(root)  # Create a tabbed interface

        # Create separate tabs for each functionality
        account_tab = ttk.Frame(tab_control)  # Tab for account management
        ticket_tab = ttk.Frame(tab_control)  # Tab for ticket purchasing
        admin_tab = ttk.Frame(tab_control)  # Tab for admin dashboard

        # Add the tabs to the tab control
        tab_control.add(account_tab, text="Account Management")  # Add account management tab
        tab_control.add(ticket_tab, text="Ticket Purchasing")  # Add ticket purchasing tab
        tab_control.add(admin_tab, text="Admin Dashboard")  # Add admin dashboard tab

        tab_control.pack(expand=1, fill="both")  # Expand and fill the tabs in the window

        # Initialize individual components
        self.account_management = AccountManagement(account_tab, self)  # Initialize AccountManagement
        self.ticket_purchasing = TicketPurchasing(ticket_tab, self)  # Initialize TicketPurchasing
        self.admin_dashboard = AdminDashboard(admin_tab)  # Initialize AdminDashboard

        self.tab_control = tab_control  # Save the tab control for switching tabs

    def show_account_management(self):  # Method to display the account management tab
        self.tab_control.select(0)  # Switch to the "Account Management" tab

    def show_ticket_purchasing(self):  # Method to display the ticket purchasing tab
        self.ticket_purchasing.update_customer_label()  # Update the customer label
        self.tab_control.select(1)  # Switch to the "Ticket Purchasing" tab

    def show_admin_dashboard(self):  # Method to display the admin dashboard tab
        self.tab_control.select(2)  # Switch to the "Admin Dashboard" tab


def main():  # Main function to run the application
    root = tk.Tk()  # Create the main Tkinter window
    app = ThemeParkApp(root)  # Initialize the ThemeParkApp with the root window
    root.mainloop()  # Start the Tkinter event loop


if __name__ == "__main__":  # Check if the script is run directly
    customers = load_data("customers.pkl") or {}  # Load customer data if available, else use an empty dictionary
    main()  # Call the main function