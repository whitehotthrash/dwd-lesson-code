# Modules - Create Solution - Problem Statement

You are building a user authentication system.

Create a module named `auth_utils.py` that contains two functions:

1.  `is_password_strong(password)`:
        Returns `True` if the password is at least 8 characters long and contains at least one number, `False` otherwise.

2.  `generate_username(first_name, last_name)`:
        Returns a username by taking the first 3 letters of the first name and the first 3 letters of the last name, all lowercase. If names are shorter than 3 letters, use the full name part. (e.g., "Alice", "Wonderland" -> "aliwon"; "Bo", "Li" -> "boli").
    
Then, create a `user_setup.py` script that imports and uses these functions to check a sample password and generate a username for a sample user.
