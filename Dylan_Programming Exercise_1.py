# This program pre-sells a limited number of cinema tickets.
# Each buyer can purchase up to 4 tickets.
# A maximum of 20 tickets will be sold in total.
# The program continues prompting users until all tickets are sold
# and displays the number of remaining tickets after each sale.
# At the end, it displays the total number of buyers.

# CONSTANT for the maximum number of tickets available
MAX_TICKETS = 20

# CONSTANT for the maximum number of tickets each buyer can purchase
MAX_PER_BUYER = 4


# Function to get the number of tickets the user wants to buy
def get_tickets_request(remaining_tickets):
    # Prompt the user for the number of tickets
    print(f"\nThere are {remaining_tickets} tickets remaining.")

    num_requested = int(input("How many tickets would you like to buy (1-4)? "))

    # Input validation using if statements
    if num_requested < 1:
        print("You must purchase at least 1 ticket.")
        return 0

    elif num_requested > MAX_PER_BUYER:
        print(f"You cannot buy more than {MAX_PER_BUYER} tickets at a time.")
        return 0

    elif num_requested > remaining_tickets:
        print("Not enough tickets remaining to fulfill your request.")
        return 0

    else:
        return num_requested


# Function to run the ticket sales application
def run_ticket_sales():
    # Initialize variables
    tickets_sold = 0
    buyer_count = 0

    # Loop until all tickets are sold
    while tickets_sold < MAX_TICKETS:

        # Calculate remaining tickets
        remaining = MAX_TICKETS - tickets_sold

        # Get the number of tickets requested
        num = get_tickets_request(remaining)

        # If a valid number of tickets was entered, process the sale
        if num > 0:
            tickets_sold += num
            buyer_count += 1
            print(f"You have successfully purchased {num} ticket(s).")
            print(f"{MAX_TICKETS - tickets_sold} ticket(s) remaining.")

    # Once all tickets are sold, display the number of buyers
    print("\nAll tickets are sold out!")
    print(f"Total number of buyers: {buyer_count}")


# Run the application
run_ticket_sales()