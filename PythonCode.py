# Base Class for ThemePark
class ThemePark:
    # Constructor to initialize the theme park attributes
    def __init__(self, park_id, name, location, opening_hours, attractions):
        self.park_id = park_id  # Unique ID for the theme park
        self.name = name  # Name of the theme park
        self.location = location  # Location of the theme park
        self.opening_hours = opening_hours  # Operating hours of the theme park
        self.attractions = attractions  # List of attractions in the park

    # Getter for park ID
    def get_park_id(self):
        return self.park_id  # Return the unique ID of the theme park

    # Setter for park ID
    def set_park_id(self, park_id):
        self.park_id = park_id  # Update the park ID

    # Getter for park name
    def get_name(self):
        return self.name  # Return the name of the park

    # Setter for park name
    def set_name(self, name):
        self.name = name  # Update the name of the park

    # Getter for park location
    def get_location(self):
        return self.location  # Return the location of the park

    # Setter for park location
    def set_location(self, location):
        self.location = location  # Update the park location

    # Getter for opening hours
    def get_opening_hours(self):
        return self.opening_hours  # Return the park's operating hours

    # Setter for opening hours
    def set_opening_hours(self, hours):
        self.opening_hours = hours  # Update the park's operating hours

    # Getter for attractions
    def get_attractions(self):
        return self.attractions  # Return the list of attractions

    # Setter for attractions
    def set_attractions(self, attractions):
        self.attractions = attractions  # Update the attractions list

    # String representation of the ThemePark object
    def __str__(self):
        return f"{self.name} located in {self.location}, Open: {self.opening_hours}"


# Admin Class
class Admin:
    # Constructor to initialize admin attributes
    def __init__(self, admin_id, name, email, password, access_level, park_capacity):
        self.admin_id = admin_id  # Unique ID for the admin
        self.name = name  # Name of the admin
        self.email = email  # Email address of the admin
        self.__password = password  # Password of the admin (private)
        self.access_level = access_level  # Admin's access level
        self.tickets_sold = {}  # Dictionary to track tickets sold
        self.sales_revenue = 0.0  # Total revenue from ticket sales
        self.park_capacity = park_capacity  # Maximum visitor capacity of the park
        self.current_visitor_count = 0  # Current number of visitors in the park

    # Getter for admin ID
    def get_admin_id(self):
        return self.admin_id  # Return the admin ID

    # Setter for admin ID
    def set_admin_id(self, admin_id):
        self.admin_id = admin_id  # Update the admin ID

    # Getter for admin name
    def get_name(self):
        return self.name  # Return the admin's name

    # Setter for admin name
    def set_name(self, name):
        self.name = name  # Update the admin's name

    # Getter for admin email
    def get_email(self):
        return self.email  # Return the admin's email

    # Setter for admin email
    def set_email(self, email):
        self.email = email  # Update the admin's email

    # Getter for admin password
    def get_password(self):
        return self.__password  # Return the admin's password (private)

    # Setter for admin password
    def set_password(self, password):
        self.__password = password  # Update the admin's password

    # Getter for access level
    def get_access_level(self):
        return self.access_level  # Return the admin's access level

    # Setter for access level
    def set_access_level(self, access_level):
        self.access_level = access_level  # Update the admin's access level

    # Getter for tickets sold
    def get_tickets_sold(self):
        return self.tickets_sold  # Return the tickets sold dictionary

    # Setter for tickets sold
    def set_tickets_sold(self, tickets_sold):
        self.tickets_sold = tickets_sold  # Update the tickets sold dictionary

    # Getter for sales revenue
    def get_sales_revenue(self):
        return self.sales_revenue  # Return the total sales revenue

    # Setter for sales revenue
    def set_sales_revenue(self, revenue):
        self.sales_revenue = revenue  # Update the total sales revenue

    # Getter for park capacity
    def get_park_capacity(self):
        return self.park_capacity  # Return the park's maximum visitor capacity

    # Setter for park capacity
    def set_park_capacity(self, capacity):
        self.park_capacity = capacity  # Update the park's maximum visitor capacity

    # Getter for current visitor count
    def get_current_visitor_count(self):
        return self.current_visitor_count  # Return the current number of visitors

    # Setter for current visitor count
    def set_current_visitor_count(self, count):
        self.current_visitor_count = count  # Update the current visitor count

    # String representation of the Admin object
    def __str__(self):
        return f"Admin: {self.name}, Tickets Sold: {self.tickets_sold}, Revenue: {self.sales_revenue}"


# Ticket Base Class
class Ticket:
    # Constructor to initialize ticket attributes
    def __init__(self, ticket_id, ticket_type, price, validity, discount_rate, limitations, availability):
        self.ticket_id = ticket_id  # Unique identifier for the ticket
        self.ticket_type = ticket_type  # Type of the ticket (e.g., SingleDayPass, VIP)
        self.price = price  # Price of the ticket
        self.validity = validity  # Validity period of the ticket
        self.discount_rate = discount_rate  # Discount rate applied to the ticket
        self.limitations = limitations  # Limitations or restrictions of the ticket
        self.availability = availability  # Availability count for the ticket

    # Getter for ticket ID
    def get_ticket_id(self):
        return self.ticket_id  # Return the unique ticket ID

    # Setter for ticket ID
    def set_ticket_id(self, ticket_id):
        self.ticket_id = ticket_id  # Update the ticket ID

    # Getter for ticket type
    def get_ticket_type(self):
        return self.ticket_type  # Return the ticket type

    # Setter for ticket type
    def set_ticket_type(self, ticket_type):
        self.ticket_type = ticket_type  # Update the ticket type

    # Getter for ticket price
    def get_price(self):
        return self.price  # Return the ticket price

    # Setter for ticket price
    def set_price(self, price):
        self.price = price  # Update the ticket price

    # Getter for validity
    def get_validity(self):
        return self.validity  # Return the ticket's validity period

    # Setter for validity
    def set_validity(self, validity):
        self.validity = validity  # Update the validity period

    # Getter for discount rate
    def get_discount_rate(self):
        return self.discount_rate  # Return the discount rate for the ticket

    # Setter for discount rate
    def set_discount_rate(self, rate):
        self.discount_rate = rate  # Update the discount rate

    # Getter for limitations
    def get_limitations(self):
        return self.limitations  # Return the ticket limitations

    # Setter for limitations
    def set_limitations(self, limitations):
        self.limitations = limitations  # Update the ticket limitations

    # Getter for availability
    def get_availability(self):
        return self.availability  # Return the number of tickets available

    # Setter for availability
    def set_availability(self, availability):
        self.availability = availability  # Update the ticket availability count

    # Method to calculate the discounted price
    def calculate_discount_price(self):
        return self.price * (1 - self.discount_rate / 100)  # Calculate price after discount

    # String representation of the ticket
    def __str__(self):
        return f"Ticket {self.ticket_type}: ${self.price}, Valid: {self.validity}"


# Subclass: SingleDayPass
class SingleDayPass(Ticket):
    # Constructor to initialize SingleDayPass-specific attributes
    def __init__(self, ticket_id, ticket_date, availability=100):
        # Initialize base Ticket class with common attributes
        super().__init__(
            ticket_id,
            "SingleDayPass",  # Ticket type
            price=275.0,  # Fixed price from table
            validity="1 Day",  # Validity of 1 day
            discount_rate=0.0,  # No discounts
            limitations="Valid only on selected date",  # Specific limitation
            availability=availability  # Default availability
        )
        self.ticket_date = ticket_date  # Specific date for the ticket

    # Getter for ticket_date
    def get_ticket_date(self):
        return self.ticket_date  # Return the ticket date

    # Setter for ticket_date
    def set_ticket_date(self, ticket_date):
        self.ticket_date = ticket_date  # Update the ticket date

    # Method to check if the ticket is valid for the current date
    def is_valid(self, current_date):
        return self.ticket_date == current_date  # Check if the ticket date matches the current date

    # String representation of SingleDayPass
    def __str__(self):
        # Add ticket date to the string representation
        return f"{super().__str__()}, Date: {self.ticket_date}"


# Subclass: AnnualPass
class AnnualPass(Ticket):
    # Constructor to initialize AnnualPass-specific attributes
    def __init__(self, ticket_id, renewal_discount, expiry_date, member_name, availability=50):  # Initialize base Ticket class with common attributes
        super().__init__(
            ticket_id,
            "AnnualPass",  # Ticket type
            price=1840.0,  # Fixed price for AnnualPass
            validity="1 Year",  # Validity of 1 year
            discount_rate=renewal_discount,  # Discount rate for renewals
            limitations="Valid for one year, non-transferable",  # Specific limitations
            availability=availability  # Availability count
        )
        self.renewal_discount = renewal_discount  # Discount applied during renewal
        self.expiry_date = expiry_date  # Expiry date of the annual pass
        self.member_name = member_name

    # Getter for renewal discount
    def get_renewal_discount(self):
        return self.renewal_discount  # Return the renewal discount

    # Setter for renewal discount
    def set_renewal_discount(self, renewal_discount):
        self.renewal_discount = renewal_discount  # Update the renewal discount

    # Getter for expiry date
    def get_expiry_date(self):
        return self.expiry_date  # Return the expiry date

    # Setter for expiry date
    def set_expiry_date(self, expiry_date):
        self.expiry_date = expiry_date  # Update the expiry date

    # Getter for member_name
    def get_member_name(self):
        return self.member_name #  Returns the value of the member's name

    # Setter for member_name
    def set_member_name(self, member_name):
        self.member_name = member_name # Update the value of the member's name

    # String representation of AnnualPass
    def __str__(self):
        # Add renewal discount and expiry date to the string representation
        return f"{super().__str__()}, Renewal Discount: {self.renewal_discount}%, Expiry Date: {self.expiry_date}"


# Subclass: VIPExperienceTicket
class VIPExperienceTicket(Ticket):
    # Constructor to initialize VIPExperienceTicket-specific attributes
    def __init__(self, ticket_id, expedited_access, reserved_seating, availability=20):
        # Initialize base Ticket class with common attributes
        super().__init__(
            ticket_id,
            "VIPExperienceTicket",  # Ticket type
            price=550.0,  # Fixed price for VIPExperienceTicket
            validity="1 Day",  # Validity of 1 day
            discount_rate=0.0,  # No discounts
            limitations="Limited availability, must be purchased in advance",  # Specific limitations
            availability=availability  # Availability count
        )
        self.expedited_access = expedited_access  # Whether expedited access is included
        self.reserved_seating = reserved_seating  # Whether reserved seating is included

    # Getter for expedited access
    def get_expedited_access(self):
        return self.expedited_access  # Return expedited access status

    # Setter for expedited access
    def set_expedited_access(self, expedited_access):
        self.expedited_access = expedited_access  # Update expedited access status

    # Getter for reserved seating
    def get_reserved_seating(self):
        return self.reserved_seating  # Return reserved seating status

    # Setter for reserved seating
    def set_reserved_seating(self, reserved_seating):
        self.reserved_seating = reserved_seating  # Update reserved seating status

    # String representation of VIPExperienceTicket
    def __str__(self):
        # Add expedited access and reserved seating details to string representation
        return f"{super().__str__()}, Expedited Access: {self.expedited_access}, Reserved Seating: {self.reserved_seating}"


# Subclass: GroupTicket
class GroupTicket(Ticket):
    # Constructor to initialize GroupTicket-specific attributes
    def __init__(self, ticket_id, group_discount, group_size_limit, availability=30):
        # Initialize base Ticket class with common attributes
        super().__init__(
            ticket_id,
            "GroupTicket",  # Ticket type
            price=220.0,  # Fixed price per person for GroupTicket
            validity="1 Day",  # Validity of 1 day
            discount_rate=group_discount,  # Discount rate for group purchases
            limitations="Must be booked in advance",  # Specific limitations
            availability=availability  # Availability count
        )
        self.group_size_limit = group_size_limit  # Maximum group size eligible for a discount

    # Getter for group size limit
    def get_group_size_limit(self):
        return self.group_size_limit  # Return the group size limit

    # Setter for group size limit
    def set_group_size_limit(self, group_size_limit):
        self.group_size_limit = group_size_limit  # Update the group size limit

    # Method to calculate total price with group discount based on group size
    def calculate_group_discount(self, group_size):
        if group_size >= self.group_size_limit:  # Check if group size qualifies for discount
            return self.price * (1 - self.discount_rate / 100) * group_size  # Discounted price
        return self.price * group_size  # Regular price if group size does not qualify

    # String representation of GroupTicket
    def __str__(self):
        # Add group size limit to the string representation
        return f"{super().__str__()}, Group Size Limit: {self.group_size_limit}"


# Subclass: TwoDayPass
class TwoDayPass(Ticket):
    # Constructor to initialize TwoDayPass-specific attributes
    def __init__(self, ticket_id, start_date, end_date, availability=50):
        # Initialize base Ticket class with common attributes
        super().__init__(
            ticket_id,
            "TwoDayPass",  # Ticket type
            price=480.0,  # Fixed price for TwoDayPass
            validity="2 Days",  # Validity of 2 days
            discount_rate=10.0,  # Discount for online purchases
            limitations="Cannot be split over multiple trips",  # Specific limitations
            availability=availability  # Availability count
        )
        self.start_date = start_date  # Start date of the pass
        self.end_date = end_date  # End date of the pass

    # Getter for start date
    def get_start_date(self):
        return self.start_date  # Return the start date

    # Setter for start date
    def set_start_date(self, start_date):
        self.start_date = start_date  # Update the start date

    # Getter for end date
    def get_end_date(self):
        return self.end_date  # Return the end date

    # Setter for end date
    def set_end_date(self, end_date):
        self.end_date = end_date  # Update the end date

    # Method to check if the pass is valid for the current date
    def is_valid(self, current_date):
        return self.start_date <= current_date <= self.end_date  # Check if within range

    # String representation of TwoDayPass
    def __str__(self):
        # Add start and end dates to the string representation
        return f"{super().__str__()}, Start Date: {self.start_date}, End Date: {self.end_date}"


# Subclass: ChildTicket
class ChildTicket(Ticket):
    # Constructor to initialize ChildTicket-specific attributes
    def __init__(self, ticket_id, age_limit, availability=100):
        # Initialize base Ticket class with common attributes
        super().__init__(
            ticket_id,
            "ChildTicket",  # Ticket type
            price=185.0,  # Fixed price for ChildTicket
            validity="1 Day",  # Validity of 1 day
            discount_rate=0.0,  # No discounts
            limitations="Valid only on selected date, must be accompanied by an adult",  # Specific limitations
            availability=availability  # Availability count
        )
        self.age_limit = age_limit  # Maximum age for eligibility

    # Getter for age limit
    def get_age_limit(self):
        return self.age_limit  # Return the age limit

    # Setter for age limit
    def set_age_limit(self, age_limit):
        self.age_limit = age_limit  # Update the age limit

    # Method to check if a child's age is within the eligible range
    def is_valid_for_child(self, child_age):
        return child_age <= self.age_limit  # Check if child age is valid

    # String representation of ChildTicket
    def __str__(self):
        # Add age limit to the string representation
        return f"{super().__str__()}, Age Limit: {self.age_limit}"

# Customer Class to represent a customer in the system
class Customer:
    def __init__(self, user_id, name, email, phone_number, discount_eligibility=False, account_balance=0.0, total_price=0.0): # Initialize the customer object with the provided attributes
        self.user_id = user_id  # Customer's unique ID
        self.name = name  # Customer's name
        self.email = email  # Customer's email address
        self._password = ""  # Protected attribute to store the customer's password
        self.phone_number = phone_number  # Customer's phone number
        self._order_history = []  # Protected attribute to store the customer's order history
        self.discount_eligibility = discount_eligibility  # Whether the customer is eligible for a discount
        self.account_balance = account_balance  # Customer's current account balance
        self._selected_tickets = []  # Protected attribute to store the customer's selected tickets
        self.total_price = total_price  # Total price of the customer's purchases

    # Getter for user_id
    def get_user_id(self):
        return self.user_id  # Return the customer's unique ID

    # Setter for user_id
    def set_user_id(self, user_id):
        self.user_id = user_id  # Update the customer's unique ID

    # Getter for name
    def get_name(self):
        return self.name  # Return the customer's name

    # Setter for name
    def set_name(self, name):
        self.name = name  # Update the customer's name

    # Getter for email
    def get_email(self):
        return self.email  # Return the customer's email address

    # Setter for email
    def set_email(self, email):
        self.email = email  # Update the customer's email address

    # Getter for password (protected)
    def get_password(self):
        return self._password  # Return the customer's password (protected attribute)

    # Setter for password (protected)
    def set_password(self, password):
        self._password = password  # Update the customer's password

    # Getter for phone_number
    def get_phone_number(self):
        return self.phone_number  # Return the customer's phone number

    # Setter for phone_number
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number  # Update the customer's phone number

    # Getter for order_history (protected)
    def get_order_history(self):
        return self._order_history  # Return the customer's order history

    # Setter for order_history (protected)
    def set_order_history(self, orders):
        self._order_history = orders  # Update the customer's order history

    # Getter for discount_eligibility
    def get_discount_eligibility(self):
        return self.discount_eligibility  # Return whether the customer is eligible for discounts

    # Setter for discount_eligibility
    def set_discount_eligibility(self, eligible):
        self.discount_eligibility = eligible  # Update the customer's discount eligibility

    # Getter for account_balance
    def get_account_balance(self):
        return self.account_balance  # Return the customer's current account balance

    # Setter for account_balance
    def set_account_balance(self, balance):
        self.account_balance = balance  # Update the customer's account balance

    # Getter for selected_tickets (protected)
    def get_selected_tickets(self):
        return self._selected_tickets  # Return the list of tickets selected by the customer

    # Setter for selected_tickets (protected)
    def set_selected_tickets(self, tickets):
        self._selected_tickets = tickets  # Update the list of tickets selected by the customer

    # Getter for total_price
    def get_total_price(self):
        return self.total_price  # Return the total price of the customer's purchases

    # Setter for total_price
    def set_total_price(self, price):
        self.total_price = price  # Update the total price of the customer's purchases

    # Method to calculate the total price based on order history and selected tickets
    def calculate_total_price(self):
        # Calculate the total price based on the sum of the prices of orders and selected tickets
        order_total = sum(order.price for order in self._order_history)  # Sum prices of all orders
        ticket_total = sum(ticket.price for ticket in self._selected_tickets)  # Sum prices of all selected tickets
        self.total_price = order_total + ticket_total  # Update the total price
        return self.total_price  # Return the calculated total price

    # String representation of the Customer class
    def __str__(self):
        return f"Customer {self.name} (ID: {self.user_id}), Email: {self.email}, Total Price: {self.total_price}"  # Return a formatted string with the customer's details

# Order Class to represent an order placed by a customer
class Order:
    # Constructor to initialize Order attributes
    def __init__(self, order_id, customer, tickets, order_date, payment_status):
        self.order_id = order_id  # Unique ID for the order
        self.customer = customer  # Reference to the Customer object who placed the order
        self.tickets = tickets  # List of Ticket objects included in the order
        self.order_date = order_date  # Date when the order was placed
        self.total_price = sum(ticket.price for ticket in tickets) # Calculate the total price by summing up the prices of all tickets
        self.__payment_status = payment_status  # Private attribute

    # Getter for order_id
    def get_order_id(self):
        return self.order_id  # Return the order's ID

    # Setter for order_id
    def set_order_id(self, order_id):
        self.order_id = order_id  # Update the order's ID

    # Getter for customer
    def get_customer(self):
        return self.customer  # Return the Customer object associated with the order

    # Setter for customer
    def set_customer(self, customer):
        self.customer = customer  # Update the Customer object associated with the order

    # Getter for tickets
    def get_tickets(self):
        return self.tickets  # Return the list of Ticket objects in the order

    # Setter for tickets
    def set_tickets(self, tickets):
        self.tickets = tickets  # Update the list of Ticket objects in the order

    # Getter for order_date
    def get_order_date(self):
        return self.order_date  # Return the date of the order

    # Setter for order_date
    def set_order_date(self, order_date):
        self.order_date = order_date  # Update the date of the order

    # Getter for total_price
    def get_total_price(self):
        return self.total_price  # Return the total price of the order

    # Getter for payment_status
    def get_payment_status(self):
        return self.__payment_status  # Return the private payment status

    # Setter for payment_status
    def set_payment_status(self, payment_status):
        self.__payment_status = payment_status  # Update the payment status

    # String representation of the Order class
    def __str__(self):
        # Return a formatted string with the order ID and total price
        return f"Order ID: {self.order_id}, Total Price: ${self.total_price}"

# Payment Class to represent payment details for an order
class Payment:
    def __init__(self, payment_id, order, amount_paid, payment_method, transaction_status): # Constructor to initialize Payment attributes
        self.payment_id = payment_id  # Unique ID for the payment
        self.order = order  # Reference to the associated Order object
        self.amount_paid = amount_paid  # Amount paid for the order
        self.payment_method = payment_method  # Payment method used (e.g., Credit Card, Cash)
        self.transaction_status = transaction_status  # Status of the transaction (e.g., Successful, Pending)

    # Getter for payment_id
    def get_payment_id(self):
        return self.payment_id  # Return the payment ID

    # Setter for payment_id
    def set_payment_id(self, payment_id):
        self.payment_id = payment_id  # Update the payment ID

    # Getter for order
    def get_order(self):
        return self.order  # Return the associated Order object

    # Setter for order
    def set_order(self, order):
        self.order = order  # Update the associated Order object

    # Getter for amount_paid
    def get_amount_paid(self):
        return self.amount_paid  # Return the amount paid for the order

    # Setter for amount_paid
    def set_amount_paid(self, amount_paid):
        self.amount_paid = amount_paid  # Update the amount paid

    # Getter for payment_method
    def get_payment_method(self):
        return self.payment_method  # Return the payment method used

    # Setter for payment_method
    def set_payment_method(self, payment_method):
        self.payment_method = payment_method  # Update the payment method

    # Getter for transaction_status
    def get_transaction_status(self):
        return self.transaction_status  # Return the transaction status

    # Setter for transaction_status
    def set_transaction_status(self, status):
        self.transaction_status = status  # Update the transaction status

    # String representation of the Payment class
    def __str__(self):
        # Return a formatted string with payment details
        return (f"Payment ID: {self.payment_id}, Amount Paid: ${self.amount_paid}, "
                f"Method: {self.payment_method}, Status: {self.transaction_status}")


class Invoice:
    # Constructor to initialize Invoice attributes
    def __init__(self, invoice_id, order, payment, issue_date):
        self.invoice_id = invoice_id  # Unique ID for the invoice
        self.order = order  # Reference to the associated Order object
        self.payment = payment  # Reference to the associated Payment object
        self.issue_date = issue_date  # Date the invoice was issued

    # Getter for invoice_id
    def get_invoice_id(self):
        return self.invoice_id  # Return the invoice ID

    # Setter for invoice_id
    def set_invoice_id(self, invoice_id):
        self.invoice_id = invoice_id  # Update the invoice ID

    # Getter for order
    def get_order(self):
        return self.order  # Return the associated Order object

    # Setter for order
    def set_order(self, order):
        self.order = order  # Update the associated Order object

    # Getter for payment
    def get_payment(self):
        return self.payment  # Return the associated Payment object

    # Setter for payment
    def set_payment(self, payment):
        self.payment = payment  # Update the associated Payment object

    # Getter for issue_date
    def get_issue_date(self):
        return self.issue_date  # Return the issue date of the invoice

    # Setter for issue_date
    def set_issue_date(self, issue_date):
        self.issue_date = issue_date  # Update the issue date of the invoice

    # Method to generate the invoice details
    def generate_invoice(self):
        # Return a detailed string representation of the invoice
        return (f"Invoice ID: {self.invoice_id}\n"
                f"Order ID: {self.order.get_order_id()}\n"
                f"Payment ID: {self.payment.get_payment_id()}\n"
                f"Issue Date: {self.issue_date}\n"
                f"Total Price: ${self.order.get_total_price()}\n"
                f"Amount Paid: ${self.payment.get_amount_paid()}\n"
                f"Transaction Status: {self.payment.get_transaction_status()}")

    # String representation of the Invoice class
    def __str__(self):
        # Return a formatted string with invoice summary
        return (f"Invoice ID: {self.invoice_id}, Order ID: {self.order.get_order_id()}, "
                f"Payment ID: {self.payment.get_payment_id()}, Issue Date: {self.issue_date}")