import numpy as np
import csv

def load_grades(filename):
    """
    Load grades from a CSV file into a NumPy array.
    Skips the header row, and excludes first and last names.
    Returns a NumPy array of shape (num_students, num_exams).
    """
    grades_list = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # skip header
        for row in reader:
            # row: [FirstName, LastName, Exam1, Exam2, Exam3]
            # convert exam scores to int and store
            grades_list.append(list(map(int, row[2:])))
    grades = np.array(grades_list)
    return grades

def print_basic_stats(grades):
    """
    Print the first few rows and calculate stats per exam and overall.
    """
    print("\nFirst 5 rows of grades:")
    print(grades[:5])

    # Stats per exam (axis=0 = columns)
    means = np.mean(grades, axis=0)
    medians = np.median(grades, axis=0)
    std_devs = np.std(grades, axis=0)
    minimums = np.min(grades, axis=0)
    maximums = np.max(grades, axis=0)

    print("\nStatistics per exam:")
    for i in range(grades.shape[1]):
        print(f"Exam {i+1}: Mean={means[i]:.2f}, Median={medians[i]}, Std={std_devs[i]:.2f}, Min={minimums[i]}, Max={maximums[i]}")

    # Overall stats for all exams combined (flattened)
    all_grades = grades.flatten()
    overall_mean = np.mean(all_grades)
    overall_median = np.median(all_grades)
    overall_std = np.std(all_grades)
    overall_min = np.min(all_grades)
    overall_max = np.max(all_grades)

    print("\nOverall statistics for all exams combined:")
    print(f"Mean = {overall_mean:.2f}")
    print(f"Median = {overall_median}")
    print(f"Standard Deviation = {overall_std:.2f}")
    print(f"Minimum = {overall_min}")
    print(f"Maximum = {overall_max}")

def analyze_pass_fail(grades, passing_score=60):
    """
    Calculate and print number of students who passed and failed each exam,
    plus overall pass percentage.
    """
    num_students, num_exams = grades.shape
    passed_counts = np.sum(grades >= passing_score, axis=0)
    failed_counts = num_students - passed_counts

    print("\nPass/Fail per exam:")
    for i in range(num_exams):
        print(f"Exam {i+1}: Passed = {passed_counts[i]}, Failed = {failed_counts[i]}")

    # Overall pass percentage across all exams (count all passing grades over total grades)
    total_grades = num_students * num_exams
    total_passed = np.sum(grades >= passing_score)
    pass_percentage = (total_passed / total_grades) * 100

    print(f"\nOverall pass percentage across all exams: {pass_percentage:.2f}%")

def main():
    filename = 'grades.csv'  # your CSV file from your existing exercise
    grades = load_grades(filename)
    print_basic_stats(grades)
    analyze_pass_fail(grades)

if __name__ == "__main__":
    main()