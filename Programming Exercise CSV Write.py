import csv


def write_grades():
    """
    Prompts the instructor for student information and writes it to a CSV file.
    Each record contains: First Name, Last Name, Exam 1, Exam 2, Exam 3
    """
    filename = 'grades.csv'
    print("Welcome to the Grade Entry Program")

    num_students = 0

    # Ask how many students to enter
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Open CSV file for writing
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # Collect and write each student's data
        for i in range(1, num_students + 1):
            print(f"\nEntering data for student {i}:")
            first_name = input("  First name: ").strip()
            last_name = input("  Last name: ").strip()

            # Collect three valid exam scores
            exam_scores = []
            for j in range(1, 4):
                while True:
                    try:
                        score = int(input(f"  Exam {j} score: "))
                        exam_scores.append(score)
                        break
                    except ValueError:
                        print("    Please enter a valid integer score.")

            # Write the student's record
            writer.writerow([first_name, last_name] + exam_scores)

    print(f"\nData successfully written to {filename}.")


# Run the program
if __name__ == "__main__":
    write_grades()