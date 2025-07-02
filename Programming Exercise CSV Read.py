import csv


def read_grades():
    """
    Reads and displays student grade data from the grades.csv file
    in a tabular format.
    """
    filename = 'grades.csv'
    print("Displaying contents of grades.csv:\n")

    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)

            # Read the header and print it
            header = next(reader)
            print(f"{header[0]:<15} {header[1]:<15} {header[2]:<8} {header[3]:<8} {header[4]:<8}")
            print("-" * 60)

            # Print each student record
            for row in reader:
                print(f"{row[0]:<15} {row[1]:<15} {row[2]:<8} {row[3]:<8} {row[4]:<8}")
    except FileNotFoundError:
        print("Error: grades.csv file not found. Please run the write_grades() program first.")


# Run the program
if __name__ == "__main__":
    read_grades()