# Dictionaries
#
# A dictionary stores data as **key-value pairs**. Think of a real-world dictionary:
# the 'word' is the key, the 'definition' is the value.
# Key characteristics: **Mutable**, **Unordered**, Keys must be **unique** and
#                      **immutable** (like strings, numbers, or tuples)."
# Syntax: Uses curly braces `{}` with `key: value` pairs.
# Use cases: Representing structured data (like a database record),
#            configuration settings, quick lookups by a unique identifier.

# Creating dictionaries
# Values can be any data type or structure you want.
student = {
    "name": "Bob",
    "major": "Physics",
    "student_id": 9876,
    "courses": ["PHYS101", "MATH200", "CS101"], # Value can be a list!
    "address": { # Value can also be another dictionary.
        street: "1 Sunset Blvd",
        city: "Brisbane",
        postcode: 4000
    }
}
print(f"Student data: {student}")

empty_dict = {}

'''
# Accessing values by key
print(f"Student Name: {student['name']}")
# print(student['gpa']) # Accessing non-existent key -> KeyError!

# Safer access with .get()
print(f"Student GPA: {student.get('gpa')}") # Returns None if key not found
print(f"Student GPA (with default): {student.get('gpa', 'Not Available')}")

# Getting keys, values, items
print(f"Keys: {student.keys()}") # Returns a view object
print(f"Values: {student.values()}") # Returns a view object
print(f"Items (key-value pairs): {student.items()}") # Returns a view object

# Checking for key existence
print(f"Does student have 'major' key? {'major' in student}")
print(f"Does student have 'phone' key? {'phone' in student}")

# Common functions
print(f"Number of key-value pairs: {len(student)}")


# --- MODIFY ---

print(f"Original student: {student}")

# Add/Update key-value pairs
student['email'] = "bob.physics@university.edu" # Add new key-value
print(f"Added email: {student}")
student['major'] = "Astrophysics" # Update existing key's value
print(f"Updated major: {student}")

# Removing items
removed_value = student.pop("student_id") # Removes key and returns value
print(f"Popped student ID ({removed_value}), dict is now: {student}")
# del student['courses'] # Another way to remove by key
# print(f"Deleted courses: {student}")

# Merging dictionaries with .update()
more_info = {"grad_year": 2025, "minor": "Mathematics"}
student.update(more_info) # Adds/updates pairs from another dict
print(f"Updated with more info: {student}")


'''