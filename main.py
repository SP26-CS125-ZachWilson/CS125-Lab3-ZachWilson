"""
Project Name: CS 125 Programming for Everyone II Lab 3 Demo
Author: Zach Wilson
Date: 1/27/2026
"""

# Exercise 1 - Text File Operations
# Demos basic file reading, writing, and appending operations.

# Step 1: Create and write data to a text file
print("=== Step 1. Writing to file ===")
with open('sample.txt', 'w') as file:
    file.write("Line 1: Welcome to CS 125!\n")
    file.write("Line 2: This is a demonstration of file operations in Python.\n")
    file.write("Line 3: Python makes file handling very easy.\n")
    file.write("Line 4. Always use 'with' statements.\n")
    file.write("Line 5. They automatically close files.\n")
    # Students should go ahead and write two more file.write lines for a total of 7 lines appended/added to the file.
print("File created and written to successfully!")

# Step 2: Read and print entire file contents
print("=== Step 2. Reading from file ===")
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)

# Step 3: Read file line by line with added line numbers
print("=== Step 3. Reading from file line by line with numbers added ===")
with open('sample.txt', 'r') as file:
    for line_number, line in enumerate(file, start=1):
        print(f"{line_number}: {line}", end='')
print("\n")

# Step 4: Append additional text to the file
print("=== Step 4. Appending to the file ===")
with open('sample.txt', 'a') as file:
    file.write("Line 6: This line was appended later on.\n")
    file.write("Line 7: File operations are fundamental.\n")
print("Text appended successfully!\n")

# Step 5: Read the updated file to show the appended content
print("=== Step 5. Reading updated file contents ===")
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)

print("Exercise 1 Complete!")



# Exercise 2 - CSV File Operations
# Demos basics of working with csv files while using the csv module.

import csv

# Step 1: Create CSV file and write student record data to it using csv.writer
print("=== Step 1. Writing data to CSV file ===")
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write header row
    writer.writerow(['name', 'student_id', 'gpa', 'major'])

    # Write student records
    writer.writerow(['Alice Johnson', 'S001', '3.8', 'Computer Science'])
    writer.writerow(['Bob Smith', 'S002', '3.2', 'Business'])
    writer.writerow(['Charlie Brown', 'S003', '3.9', 'Computer Science'])
    writer.writerow(['Diana Prince', 'S004', '3.6', 'Engineering'])
    writer.writerow(['Eve Davis', 'S005', '3.4', 'Mathematics'])

print("students.csv created successfully!\n")

# Step 2: Read CSV file using csv.reader
print("=== Step 2: Reading CSV with csv.reader ===")
with open('students.csv', 'r') as file:
    reader = csv.reader(file)

    # Read and print all rows
    for row in reader:
        print(row)
print()

# Step 3: Use csv.DictReader to find students with GPA > 3.5
print("=== Step 3: Students with GPA > 3.5 (using DictReader) ===")
with open('students.csv', 'r') as file:
    dict_reader = csv.DictReader(file)

    for student in dict_reader:
        if float(student['gpa']) > 3.5:
            print(f"{student['name']}: GPA {student['gpa']}")
print()

# Step 4: Use csv.DictWriter to create file with only CS majors
print("=== Step 4: Creating file with CS majors only ===")
cs_students = []

# First, read all students and filter CS majors
with open('students.csv', 'r') as file:
    dict_reader = csv.DictReader(file)
    for student in dict_reader:
        if student['major'] == 'Computer Science':
            cs_students.append(student)

# Write CS students to new file
with open('cs_students.csv', 'w', newline='') as file:
    fieldnames = ['name', 'student_id', 'gpa', 'major']
    dict_writer = csv.DictWriter(file, fieldnames=fieldnames)

    dict_writer.writeheader()
    dict_writer.writerows(cs_students)

print(f"cs_students.csv created with {len(cs_students)} CS majors!\n")

# Display the CS students file
print("=== CS Students File Contents ===")
with open('cs_students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("\nExercise 2 Complete!")