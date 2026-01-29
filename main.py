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

# Exercise 3 - Data Validation
# Demos validating user input before writing to CSV file.

print("\n=== Exercise 3: Data Validation ===\n")


# Step 1: Function to validate and collect product information
def get_validated_product():
    """Collect and validate product information from user."""

    # Get product name (no validation needed)
    name = input("Enter product name: ")

    # Validate price (must be positive number)
    while True:
        try:
            price = float(input("Enter product price: $"))
            if price > 0:
                break
            else:
                print("Error: Price must be a positive number. Try again.")
        except ValueError:
            print("Error: Price must be a valid number. Try again.")

    # Validate quantity (must be positive integer)
    while True:
        try:
            quantity = int(input("Enter product quantity: "))
            if quantity > 0:
                break
            else:
                print("Error: Quantity must be a positive integer. Try again.")
        except ValueError:
            print("Error: Quantity must be a valid integer. Try again.")

    return {'name': name, 'price': price, 'quantity': quantity}


# Step 2: Collect product information with validation
print("=== Step 1: Enter product information ===")
product = get_validated_product()
print(f"\nValidated Product: {product['name']}, ${product['price']:.2f}, Qty: {product['quantity']}")

# Step 3: Write validated data to CSV file with error handling
print("\n=== Step 2: Writing to inventory.csv ===")
try:
    with open('inventory.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'price', 'quantity'])
        writer.writeheader()
        writer.writerow(product)
    print("Product successfully written to inventory.csv!")
except IOError as e:
    print(f"Error writing to file: {e}")

# Step 4: Read and display the inventory file
print("\n=== Step 3: Reading inventory.csv ===")
try:
    with open('inventory.csv', 'r') as file:
        reader = csv.DictReader(file)
        for item in reader:
            print(f"Product: {item['name']}, Price: ${item['price']}, Quantity: {item['quantity']}")
except FileNotFoundError:
    print("Error: inventory.csv not found!")

print("\nExercise 3 Complete!")

# Exercise 4 - Error Handling
# Demos robust error handling for various file operation scenarios.

print("\n=== Exercise 4: Error Handling ===\n")


# Step 1: Create a function with comprehensive error handling
def read_file_safely(filename):
    """
    Attempt to read a file with proper error handling.
    Returns file contents if successful, None otherwise.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except PermissionError:
        print(f"Error: You don't have permission to access '{filename}'.")
        return None
    except IOError as e:
        print(f"Error: An I/O error occurred while reading '{filename}': {e}")
        return None


# Step 2: Test with existing file (should succeed)
print("=== Scenario 1: Reading an existing file ===")
content = read_file_safely('sample.txt')
if content:
    print("File read successfully!")
    print(f"First 50 characters: {content[:50]}...")
print()

# Step 3: Test with non-existent file (FileNotFoundError)
print("=== Scenario 2: Reading a non-existent file ===")
content = read_file_safely('nonexistent_file.txt')
print()

# Step 4: Test with directory instead of file (IOError/IsADirectoryError)
print("=== Scenario 3: Attempting to read a directory ===")
content = read_file_safely('.')
print()

# Step 5: Demonstrate try-except-else-finally structure
print("=== Step 4: Complete error handling with finally ===")
filename = 'students.csv'
try:
    file = open(filename, 'r')
    lines = file.readlines()
    print(f"Successfully read {len(lines)} lines from {filename}")
except FileNotFoundError:
    print(f"Error: '{filename}' not found")
except IOError as e:
    print(f"I/O Error: {e}")
else:
    print("File operation completed without errors")
finally:
    try:
        file.close()
        print("File closed properly")
    except:
        print("No file to close")

print("\nExercise 4 Complete!")
print("\n" + "=" * 50)
print("All Lab 3 Exercises Complete!")
print("=" * 50)