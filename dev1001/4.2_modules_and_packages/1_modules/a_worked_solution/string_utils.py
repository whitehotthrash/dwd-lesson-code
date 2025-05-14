# string_utils.py

# SUBGOAL 1: Define a reusable function to capitalize words in a string.
def capitalize_words(text):
    """Capitalizes each word in a given string."""
    if not isinstance(text, str):
        return "Input must be a string"
    return ' '.join(word.capitalize() for word in text.split())

# SUBGOAL 2: Define another reusable function to reverse a string.
def reverse_string(text):
    """Reverses a given string."""
    if not isinstance(text, str):
        return "Input must be a string"
    return text[::-1]

# This part allows testing the module directly
# If we run this directly with the `python3` command, the below code will run
# If we import it into another module, the two print statements won't run
if __name__ == "__main__":
    print(f"Testing capitalize_words: {capitalize_words('hello world')}")
    print(f"Testing reverse_string: {reverse_string('python')}")
