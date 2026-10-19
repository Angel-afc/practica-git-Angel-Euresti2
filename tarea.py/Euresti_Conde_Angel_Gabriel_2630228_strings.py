# ==============================================================================
# COVER PAGE
# ==============================================================================
# Student name: Angel Gabriel Euresti Conde
# Student ID: 2630228
# Group: I.M 1-2
# Assignment: String Manipulation, Formatting, and Validation
# ==============================================================================

# ==============================================================================
# EXECUTIVE SUMMARY
# ==============================================================================
# Strings in Python are immutable sequences of characters representing text data.
# Basic operations include concatenation, length measurement, slicing, and searching.
# Validating and normalizing input data prevents errors and cleans up user typos.
# This program covers six practical everyday problems using string methods.
# Problems include user name formatting, email validation, palindrome checking,
# text message analysis, password security classification, and store label formatting.
# Each problem includes descriptions, inputs, outputs, validations, and test cases.
# ==============================================================================

# ==============================================================================
# GOOD PRACTICES
# ==============================================================================
# - Strings are immutable: any change creates a brand new string object.
# - Always normalize text input using strip() and lower() before text comparisons.
# - Avoid magic numbers in string slicing; document what each slice does.
# - Use built-in string methods instead of writing complex custom logic.
# - Design clear validation flows: first check if empty, then check format.
# - Write clean, readable code with descriptive variable names and error messages.
# ==============================================================================


# ==============================================================================
# PROBLEM 1: FULL NAME FORMATTER (NAME + INITIALS)
# ==============================================================================
# Description:
# Formats a user's full name into Title Case and generates capital initials separated 
# by periods for a company directory or badge.
#
# Inputs:
# - full_name (string): User full name with random spaces or mixed casing.
#
# Outputs:
# - Formatted name in Title Case.
# - Initials in X.X.X. format.
#
# Validations:
# - full_name not empty after strip().
# - Must contain at least two words (first name and surname).
#
# Test cases:
# 1) Normal: "juan carlos perez" -> Formatted: Juan Carlos Perez, Initials: J.C.P.
# 2) Border: "maria  jose" -> Formatted: Maria Jose, Initials: M.J.
# 3) Error: "   " -> Error: invalid input

def problem_1():
    full_name = input("Enter full name: ")

    if not full_name or not full_name.strip():
        print("Error: invalid input")
        return

    words = full_name.strip().split()
    if len(words) < 2:
        print("Error: invalid input")
        return

    # Capitalize each word and join them
    formatted_words = []
    for word in words:
        formatted_words.append(word.capitalize())
    formatted_name = " ".join(formatted_words)

    # Extract initials
    initials_parts = []
    for word in words:
        initials_parts.append(word[0].upper() + ".")
    initials = "".join(initials_parts)

    print("Formatted name:", formatted_name)
    print("Initials:", initials)


# ==============================================================================
# PROBLEM 2: SIMPLE EMAIL VALIDATOR (STRUCTURE + DOMAIN)
# ==============================================================================
# Description:
# Validates a user's personal or school email address format for a registration form 
# by checking for spaces, the '@' symbol, and a dot in the domain part.
#
# Inputs:
# - email_text (string): Email address to check.
#
# Outputs:
# - Valid email: true/false
# - Domain part (if valid)
#
# Validations:
# - email_text not empty.
# - Exactly one '@' and no whitespace characters.
# - At least one '.' after '@'.
#
# Test cases:
# 1) Normal: "angel.euresti@gmail.com" -> Valid email: true, Domain: gmail.com
# 2) Border: "user@domain.co" -> Valid email: true, Domain: domain.co
# 3) Error: "userexample.com" -> Valid email: false

def problem_2():
    email_text = input("Enter email address: ")

    if not email_text or not email_text.strip():
        print("Error: invalid input")
        return

    cleaned_email = email_text.strip()

    if " " in cleaned_email:
        print("Valid email: false")
        return

    if cleaned_email.count("@") != 1:
        print("Valid email: false")
        return

    at_index = cleaned_email.find("@")
    domain_part = cleaned_email[at_index + 1:]

    if "." not in domain_part or domain_part.startswith(".") or domain_part.endswith("."):
        print("Valid email: false")
        return

    print("Valid email: true")
    print("Domain:", domain_part)


# ==============================================================================
# PROBLEM 3: PALINDROME CHECKER (IGNORING SPACES AND CASE)
# ==============================================================================
# Description:
# Checks if a funny phrase or text message sent by a friend reads the exact same 
# forwards and backwards (ignoring spaces and capital letters).
#
# Inputs:
# - phrase (string): Text sentence to evaluate.
#
# Outputs:
# - Is palindrome: true/false
# - Normalized phrase version.
#
# Validations:
# - phrase not empty after strip().
# - Minimum length of 3 characters after cleaning spaces.
#
# Test cases:
# 1) Normal: "Anita lava la tina" -> Is palindrome: true
# 2) Border: "A man a plan a canal Panama" -> Is palindrome: true
# 3) Error: "hi" -> Error: invalid input

def problem_3():
    phrase = input("Enter a phrase or sentence to check: ")

    if not phrase or not phrase.strip():
        print("Error: invalid input")
        return

    normalized = phrase.strip().lower().replace(" ", "")

    if len(normalized) < 3:
        print("Error: invalid input")
        return

    reversed_text = normalized[::-1]
    is_pal = (normalized == reversed_text)

    print("Is palindrome:", str(is_pal).lower())
    print("Normalized phrase:", normalized)


# ==============================================================================
# PROBLEM 4: SENTENCE WORD STATS (LENGTHS AND FIRST/LAST WORD)
# ==============================================================================
# Description:
# Analyzes a text status update or tweet written by a user, showing total word count, 
# the first word, the last word, and the shortest and longest words.
#
# Inputs:
# - sentence (string): Text message to analyze.
#
# Outputs:
# - Word count, First word, Last word, Shortest word, Longest word.
#
# Validations:
# - sentence not empty.
# - Must contain at least one valid word after split.
#
# Test cases:
# 1) Normal: "Learning Python programming is very fun" -> Count: 6, First: Learning, Last: fun
# 2) Border: "Hello" -> Count: 1, First: Hello, Last: Hello, Shortest: Hello, Longest: Hello
# 3) Error: "   " -> Error: invalid input

def problem_4():
    sentence = input("Enter a sentence or status message: ")

    if not sentence or not sentence.strip():
        print("Error: invalid input")
        return

    words = sentence.strip().split()
    if not words:
        print("Error: invalid input")
        return

    word_count = len(words)
    first_word = words[0]
    last_word = words[-1]

    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)

    print("Word count:", word_count)
    print("First word:", first_word)
    print("Last word:", last_word)
    print("Shortest word:", shortest_word)
    print("Longest word:", longest_word)


# ==============================================================================
# PROBLEM 5: PASSWORD STRENGTH CLASSIFIER
# ==============================================================================
# Description:
# Evaluates a user's account password during sign-up and classifies its security 
# strength as "weak", "medium", or "strong" based on length and character types.
#
# Inputs:
# - password_input (string): Password string to evaluate.
#
# Outputs:
# - Password strength: weak | medium | strong
#
# Validations:
# - password_input not empty.
#
# Test cases:
# 1) Normal: "MySecure123!" -> Password strength: strong
# 2) Border: "mypassword1" -> Password strength: medium
# 3) Error: "" -> Error: invalid input

def problem_5():
    password_input = input("Enter your new password: ")

    if not password_input or not password_input.strip():
        print("Error: invalid input")
        return

    pwd = password_input.strip()
    length = len(pwd)

    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_symbol = any(not c.isalnum() for c in pwd)

    if length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    elif length >= 8 and ((has_upper and has_lower) or has_digit):
        strength = "medium"
    else:
        strength = "weak"

    print("Password strength:", strength)


# ==============================================================================
# PROBLEM 6: PRODUCT LABEL FORMATTER (FIXED-WIDTH TEXT)
# ==============================================================================
# Description:
# Generates a clean, fixed-width shelf price label for a retail store item in a 
# single line, guaranteeing it takes up exactly 30 characters by padding or slicing.
#
# Inputs:
# - product_name (string): Name of the store item.
# - price_value (string or number): Cost of the item.
#
# Outputs:
# - Label text formatted to exactly 30 characters.
#
# Validations:
# - product_name not empty.
# - price_value must be convertible to a positive number.
#
# Test cases:
# 1) Normal: product="Notebook", price="45.50" -> Formatted 30 char label
# 2) Border: product="Pen", price="1.00" -> Formatted 30 char label
# 3) Error: product="", price="-5" -> Error: invalid input

def problem_6():
    product_name = input("Enter product name: ")
    price_value = input("Enter product price: ")

    if not product_name or not product_name.strip():
        print("Error: invalid input")
        return

    try:
        price = float(price_value)
        if price < 0:
            print("Error: invalid input")
            return
    except ValueError:
        print("Error: invalid input")
        return

    name = product_name.strip().upper()
    price_str = f"{price:.2f}"

    base_label = f"Product: {name} | Price: ${price_str}"

    if len(base_label) < 30:
        label = base_label.ljust(30)
    else:
        label = base_label[:30]

    print(f'Label: "{label}" (Length: {len(label)})')


# ==============================================================================
# MAIN MENU
# ==============================================================================

def main():
    while True:
        print("\nSTRING MANIPULATION AND VALIDATION TASKS")
        print("1. Full name formatter")
        print("2. Simple email validator")
        print("3. Palindrome checker")
        print("4. Sentence word stats")
        print("5. Password strength classifier")
        print("6. Product label formatter")
        print("0. Exit")

        option = input("Select a problem: ").strip()

        if option == "1":
            problem_1()
        elif option == "2":
            problem_2()
        elif option == "3":
            problem_3()
        elif option == "4":
            problem_4()
        elif option == "5":
            problem_5()
        elif option == "6":
            problem_6()
        elif option == "0":
            print("Goodbye!")
            break
        else:
            print("Error: invalid input")


if __name__ == "__main__":
    main()


# ==============================================================================
# CONCLUSIONS
# ==============================================================================
# String manipulation is essential for processing user inputs and cleaning data.
# Methods like lower(), strip(), and split() make text parsing easy and reliable.
# Normalizing inputs prevents comparison bugs caused by casing or extra spaces.
# Proper validation checks protect programs against bad data and crashes.
# Understanding string immutability and slicing gives precise control over output text.
# ==============================================================================

# ==============================================================================
# REFERENCES
# ==============================================================================
# 1) Python Software Foundation. Python Documentation - Built-in Types: Text Sequence Type — str.
# 2) Lutz, Mark. Learning Python. 5th Edition, O'Reilly Media, 2013.
# 3) Matthes, Eric. Python Crash Course. 3rd Edition, No Starch Press, 2022.
# 4) Ramalho, Luciano. Fluent Python. 2nd Edition, O'Reilly Media, 2022.
# 5) Official Python String Methods Tutorial - Python 3 Documentation.
# ==============================================================================