from functools import reduce

def main():
    # List to store expenses as (type, amount) tuples
    expenses = []

    print("Enter your monthly expenses. Type 'done' when you're finished.\n")

    # Collect expense entries from the user
    while True:
        expense_type = input("Enter the type of expense (or type 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter the amount for '{expense_type}': $"))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Please enter a valid number for the amount.")

    if not expenses:
        print("No expenses entered.")
        return

    # Use reduce to calculate the total expense
    total = reduce(lambda acc, item: acc + item[1], expenses, 0)

    # Use reduce to find the highest expense (returns the whole (type, amount) tuple)
    highest = reduce(lambda a, b: a if a[1] > b[1] else b, expenses)

    # Use reduce to find the lowest expense
    lowest = reduce(lambda a, b: a if a[1] < b[1] else b, expenses)

    # Output the results
    print("\nExpense Summary:")
    print(f"Total Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} (${highest[1]:.2f})")
    print(f"Lowest Expense: {lowest[0]} (${lowest[1]:.2f})")

# Run the program
if __name__ == "__main__":
    main()