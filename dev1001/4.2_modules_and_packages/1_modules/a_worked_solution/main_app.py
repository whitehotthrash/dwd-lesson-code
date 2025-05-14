# main_app.py
# SUBGOAL 3: Import the entire string_utils module.
import string_utils

# SUBGOAL 4: Import a specific function from the string_utils module using an alias.
from string_utils import reverse_string as rev_str

def process_user_input(user_text):
    # SUBGOAL 5: Use the imported module's function.
    capitalized = string_utils.capitalize_words(user_text)
    print(f"Capitalized: {capitalized}")

    # SUBGOAL 6: Use the specifically imported function with an alias.
    reversed_text = rev_str(user_text)
    print(f"Reversed: {reversed_text}")

# This check ensures this file has not been imported as a module
# We don't want to run the main program if it has
if __name__ == "__main__":
    sample_text = "this is a test sentence."
    process_user_input(sample_text)

    another_sample = "madam"
    print(f"Is '{another_sample}' a palindrome? {another_sample == string_utils.reverse_string(another_sample)}")
