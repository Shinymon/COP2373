"""
This program simulates and visualizes population changes in 10 Florida cities.
It includes:
1. A function to create an SQLite database and populate it with 2023 population data.
2. A function to simulate population changes for the next 20 years with varied growth/decline rates.
3. A function to allow the user to select a city and visualize its population trend using matplotlib.
"""

import sqlite3
import random
import matplotlib.pyplot as plt


# Function 1: Create database and table
def create_population_db():
    """Creates a database 'population_DT' and inserts 2023 data for 10 Florida cities."""
    conn = sqlite3.connect("population_DT.db")  # Connect to SQLite database
    c = conn.cursor()

    # Create table named 'population'
    c.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    # 10 Florida cities with the 2023 populations
    florida_cities = {
        "Miami": 449514,
        "Orlando": 316081,
        "Tampa": 403364,
        "Jacksonville": 971319,
        "Tallahassee": 201731,
        "St. Petersburg": 261256,
        "Fort Lauderdale": 182247,
        "Hialeah": 218202,
        "Gainesville": 145214,
        "Sarasota": 57638
    }

    # Insert 2023 data
    for city, pop in florida_cities.items():
        c.execute("INSERT INTO population VALUES (?, ?, ?)", (city, 2023, pop))

    conn.commit()
    conn.close()



# Function 2: Simulate population growth/decline for 20 more years
def simulate_population_growth():
    """Simulates random annual population changes for each city from 2024 to 2043."""
    conn = sqlite3.connect("population_DT.db")
    c = conn.cursor()

    # Get all distinct cities in the table
    c.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in c.fetchall()]

    for city in cities:
        # Get the population from 2023 to start simulation
        c.execute("SELECT population FROM population WHERE city = ? AND year = 2023", (city,))
        population = c.fetchone()[0]

        # Simulate population changes for the next 20 years
        for year in range(2024, 2044):
            growth_rate = random.uniform(-0.01, 0.03)  # Simulate decline or growth between -1% and +3%
            population = int(population * (1 + growth_rate))  # Apply growth rate
            c.execute("INSERT INTO population VALUES (?, ?, ?)", (city, year, population))

    conn.commit()
    conn.close()



# Function 3: Plot population for a user-selected city
def plot_population_trend():
    """Prompts user to choose a city and displays its population trend over time."""
    conn = sqlite3.connect("population_DT.db")
    c = conn.cursor()

    # List all cities in database
    c.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in c.fetchall()]

    # Print city options
    print("\nChoose a city from the following list to visualize its population growth:")
    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city}")

    # Get user choice with basic input validation
    try:
        choice = int(input("\nEnter the number corresponding to the city: "))
        if choice < 1 or choice > len(cities):
            raise ValueError("Invalid choice number.")
    except ValueError:
        print("Invalid input. Please enter a number from the list.")
        conn.close()
        return

    city_name = cities[choice - 1]

    # Get population data for selected city
    c.execute("SELECT year, population FROM population WHERE city = ? ORDER BY year", (city_name,))
    data = c.fetchall()
    years = [row[0] for row in data]
    pops = [row[1] for row in data]

    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.plot(years, pops, marker='o', linestyle='-', color='blue')
    plt.title(f"Population Growth of {city_name} (2023-2043)")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    conn.close()



# Main execution logic
if __name__ == "__main__":
    print("Creating database and inserting initial data...")
    create_population_db()

    print("Simulating 20 years of population growth...")
    simulate_population_growth()

    plot_population_trend()