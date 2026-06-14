# ============================================================
#   CLASS 1 — HOMEWORK QUESTIONS
#   Python Foundations
#   Total Questions: 10
# ============================================================
#   Instructions:
#     - Write your answer below each question.
#     - Do NOT delete the question comments.
#     - Run your code after each question to test it.
#     - Use only what was covered in Class 1.
# ============================================================


# ─────────────────────────────────────────────
# QUESTION 1 — Variables & print()
# ─────────────────────────────────────────────
# Create three variables:
#   - your_name  → your full name (string)
#   - your_age   → your age (integer)
#   - your_city  → the city you live in (string)
#
# Then print the following sentence using those variables:
#   "My name is Ali, I am 20 years old and I live in Karachi."
#
# (Replace Ali, 20, and Karachi with your own variable values.)

# Write your code below:
# Create three variables
my_name = "Summan Deedar"
age = 30
city = "Karachi"

# Print :
print(f"Hello! My name is {my_name}, I am {age} year old, and I live in {city}.")

# === Code Execution Successful ===
# Hello! My name is Summan Deedar, I am 30 year old, and I live in Karachi.





# ─────────────────────────────────────────────
# QUESTION 2 — Arithmetic Operations
# ─────────────────────────────────────────────
# A shopkeeper sells 3 items:
#   - Rice bag    → Rs. 350
#   - Cooking oil → Rs. 480
#   - Sugar bag   → Rs. 120
#
# Write a program that:
#   1. Stores each price in a variable.
#   2. Calculates the total cost.
#   3. Calculates a 10% discount on the total.
#   4. Calculates the final price after the discount.
#   5. Prints the total, discount amount, and final price.

# Write your code below:
# 1. Store each price in a variable
price_rice = 350
price_oil = 480
price_sugar = 120

# 2. Calculate the total cost
total_cost = price_rice + price_oil + price_sugar

# 3. Calculate a 10% discount on the total
discount_percentage = 10
discount_amount = (discount_percentage / 100) * total_cost

# 4. Calculate the final price after the discount
final_price = total_cost - discount_amount

# 5. Print the total, discount amount, and final price
print(f"Total Cost: Rs. {total_cost}")
print(f"Discount Amount ({discount_percentage}%): Rs. {discount_amount:.2f}")
print(f"Final Price after Discount: Rs. {final_price:.2f}")

# === Code Execution Successful ===
# Total Cost: Rs. 950
# Discount Amount (10%): Rs. 95.00
# Final Price after Discount: Rs. 855.00


# ─────────────────────────────────────────────
# QUESTION 3 — Type Conversion & Input
# ─────────────────────────────────────────────
# Write a program that:
#   1. Asks the user to enter their birth year.
#   2. Calculates their approximate age (use current year = 2024).
#   3. Prints: "You are approximately X years old."
#
# Remember: input() returns a string — convert it to int first!

# Write your code below:

# 1. Ask the user to enter their birth year and convert it to an integer
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)

# 2. Calculate their approximate age (using current year = 2024 as requested)
current_year = 2024
age = current_year - birth_year

# 3. Print the final result
print(f"You are approximately {age} years old.")

# === Code Execution Successful ===
# Enter your birth year: 1994
# You are approximately 30 years old.



# ─────────────────────────────────────────────
# QUESTION 4 — if / elif / else
# ─────────────────────────────────────────────
# Write a program that asks the user to enter the current temperature
# (in Celsius) and then prints a clothing suggestion:
#
#   temperature > 35  → "It's very hot! Wear light clothes."
#   temperature 25-35 → "It's warm. A t-shirt is fine."
#   temperature 15-24 → "It's a bit cool. Consider a jacket."
#   temperature < 15  → "It's cold! Wear a warm coat."

# Write your code below:

# Ask the user to enter the current temperature and convert it to a float
temperature = float(input("Enter the current temperature in Celsius: "))

# Conditional logic for clothing suggestions
if temperature > 35:
    print("It's very hot! Wear light clothes.")
elif temperature >= 25:  # This covers 25 to 35
    print("It's warm. A t-shirt is fine.")
elif temperature >= 15:  # This covers 15 to 24
    print("It's a bit cool. Consider a jacket.")
else:                    # This covers anything less than 15
    print("It's cold! Wear a warm coat.")

# === Code Execution Successful ===
#     Enter the current temperature in Celsius: 34
# It's warm. A t-shirt is fine.



# ─────────────────────────────────────────────
# QUESTION 5 — if / elif / else (Grade Calculator)
# ─────────────────────────────────────────────
# Write a program that:
#   1. Asks the user to enter marks out of 100.
#   2. Prints the grade based on these rules:
#        90 – 100  → Grade A  (Excellent)
#        75 –  89  → Grade B  (Good)
#        60 –  74  → Grade C  (Average)
#        50 –  59  → Grade D  (Below Average)
#         0 –  49  → Grade F  (Fail)
#   3. Also print "Congratulations!" if the student passed (marks >= 50).
#      Print "Better luck next time." if the student failed.

# Write your code below:
# 1. Ask the user to enter marks out of 100
marks = float(input("Enter your marks (0-100): "))

# 2. Determine and print the grade based on the rules
if marks >= 90 and marks <= 100:
    print("Grade A (Excellent)")
elif marks >= 75:
    print("Grade B (Good)")
elif marks >= 60:
    print("Grade C (Average)")
elif marks >= 50:
    print("Grade D (Below Average)")
else:
    print("Grade F (Fail)")

# 3. Print a final message based on pass/fail status
if marks >= 50:
    print("Congratulations!")
else:
    print("Better luck next time.")

# === Code Execution Successful ===
#     Enter your marks (0-100): 90
# Grade A (Excellent)
# Congratulations!





# ─────────────────────────────────────────────
# QUESTION 6 — for Loop
# ─────────────────────────────────────────────
# Write a program that prints the multiplication table
# for any number entered by the user.
#
# Example output (if user enters 7):
#   7 x 1  =  7
#   7 x 2  = 14
#   7 x 3  = 21
#   ...
#   7 x 10 = 70

# Write your code below:
# Ask the user to enter a number for the table
num = int(input("Enter a number to print its multiplication table: "))

print(f"\nMultiplication Table for {num}:")
print("───────────────────────────────")

# Use a for loop to iterate from 1 to 10
# Note: range(1, 11) starts at 1 and stops before 11
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")

# === Code Execution Successful ===
#     Enter a number to print its multiplication table: 7

# Multiplication Table for 7:
# ───────────────────────────────
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70




# ─────────────────────────────────────────────
# QUESTION 7 — for Loop + List
# ─────────────────────────────────────────────
# You are given this list of exam scores:
#   scores = [72, 88, 45, 95, 60, 53, 78, 91, 40, 85]
#
# Write a program that loops through the list and:
#   1. Prints each score.
#   2. Prints "Pass" next to the score if it is >= 50.
#      Prints "Fail" next to the score if it is < 50.
#
# Example output:
#   72 → Pass
#   88 → Pass
#   45 → Fail
#   ...

# Write your code below:


scores = [72, 88, 45, 95, 60, 53, 78, 91, 40, 85]

print("Exam Results:")
print("─────────────")

# Loop through each score in the list
for score in scores:
    # Check the pass/fail condition
    if score >= 50:
        print(f"{score} → Pass")
    else:
        print(f"{score} → Fail")


# === Code Execution Successful ===
# Exam Results:
# ─────────────
# 72 → Pass
# 88 → Pass
# 45 → Fail
# 95 → Pass
# 60 → Pass
# 53 → Pass
# 78 → Pass
# 91 → Pass
# 40 → Fail
# 85 → Pass




# ─────────────────────────────────────────────
# QUESTION 8 — while Loop
# ─────────────────────────────────────────────
# Write a number guessing game:
#   1. Set a secret number (you choose it, e.g. 7).
#   2. Ask the user to guess the number.
#   3. Keep asking until they guess correctly.
#   4. Each wrong guess should print one of these hints:
#        "Too high! Try again." — if their guess is too big
#        "Too low! Try again."  — if their guess is too small
#   5. When they get it right, print:
#        "Correct! You got it in X tries."
#      (where X is how many attempts they made)

# Write your code below:
# 1. Set the secret number and initialize the attempt counter
secret_number = 7
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number. Can you guess it?")
print("─────────────────────────────────────────")

# 3. Keep asking until they guess correctly
while True:
    # 2. Ask the user to guess the number
    guess = int(input("Enter your guess: "))
    attempts += 1  # Increment the attempt count by 1

    # Check the user's guess against the secret number
    if guess == secret_number:
        # 5. Correct guess handling
        print(f"Correct! You got it in {attempts} tries.")
        break  # Exit the loop since they guessed correctly
    elif guess > secret_number:
        # 4. Hint for a guess that is too high
        print("Too high! Try again.\n")
    else:
        # 4. Hint for a guess that is too low
        print("Too low! Try again.\n")

# === Code Execution Successful ===
# ***************************************
#         Welcome to the Number Guessing Game!
# I'm thinking of a number. Can you guess it?
# ─────────────────────────────────────────
# Enter your guess: 4
# Too low! Try again.

# Enter your guess: 7
# Correct! You got it in 2 tries.




# ─────────────────────────────────────────────
# QUESTION 9 — Functions
# ─────────────────────────────────────────────
# Write the following two functions and then call both of them:
#
# Function 1: is_even(number)
#   - Takes one number as input.
#   - Returns True if the number is even, False if it is odd.
#
# Function 2: celsius_to_fahrenheit(celsius)
#   - Takes a temperature in Celsius.
#   - Returns the temperature in Fahrenheit.
#   - Formula: F = (C × 9/5) + 32
#
# After defining both functions:
#   - Ask the user to enter a number and print whether it is even or odd.
#   - Ask the user to enter a Celsius temperature and print the Fahrenheit value.

# Write your code below:
# ─────────────────────────────────────────────
# FUNCTION DEFINITIONS
# ─────────────────────────────────────────────

def is_even(number):
    """
    Takes one number as input.
    Returns True if the number is even, False if it is odd.
    """
    # An even number leaves a remainder of 0 when divided by 2
    if number % 2 == 0:
        return True
    else:
        return False


def celsius_to_fahrenheit(celsius):
    """
    Takes a temperature in Celsius.
    Returns the temperature in Fahrenheit.
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# ─────────────────────────────────────────────
# FUNCTION CALLS & USER INTERACTION
# ─────────────────────────────────────────────

print("--- Testing Function 1: Even/Odd Checker ---")
user_num = int(input("Enter an integer to check: "))

# Call the is_even function and check its boolean return value
if is_even(user_num):
    print(f"{user_num} is an Even number.\n")
else:
    print(f"{user_num} is an Odd number.\n")


print("--- Testing Function 2: Temperature Converter ---")
user_celsius = float(input("Enter temperature in Celsius: "))

# Call the celsius_to_fahrenheit function and store the result
converted_f = celsius_to_fahrenheit(user_celsius)
print(f"{user_celsius}°C is equal to {converted_f:.2f}°F")

# === Code Execution Successful ===
# *****************************************
# --- Testing Function 1: Even/Odd Checker ---
# Enter an integer to check: 55
# 55 is an Odd number.

# --- Testing Function 2: Temperature Converter ---
# Enter temperature in Celsius: 34
# 34.0°C is equal to 93.20°F





# ─────────────────────────────────────────────
# QUESTION 10 — Lists + Functions (Putting it all together)
# ─────────────────────────────────────────────
# Write a function called analyse_scores(scores) that:
#   - Takes a list of numbers (scores) as input.
#   - Calculates and RETURNS a dictionary with:
#       "highest"  → the highest score
#       "lowest"   → the lowest score
#       "average"  → the average score (rounded to 2 decimal places)
#       "passed"   → count of scores that are >= 50
#       "failed"   → count of scores that are < 50
#
# Then call the function with this list:
#   scores = [72, 88, 45, 95, 60, 53, 78, 91, 40, 85]
#
# Print each result clearly. Example output:
#   Highest Score : 95
#   Lowest Score  : 40
#   Average Score : 70.7
#   Passed        : 8
#   Failed        : 2

# Write your code below:
def analyse_scores(scores):
    """
    Takes a list of numbers and returns a dictionary with key metrics:
    highest, lowest, average, passed count, and failed count.
    """
    # 1. Use built-in functions for max, min, and sum
    highest = max(scores)
    lowest = min(scores)
    
    # Calculate the average (sum of elements / number of elements)
    average = sum(scores) / len(scores)
    average_rounded = round(average, 2)
    
    # 2. Initialize counters for pass/fail
    passed_count = 0
    failed_count = 0
    
    # Loop through the scores to update counters
    for score in scores:
        if score >= 50:
            passed_count += 1
        else:
            failed_count += 1
            
    # 3. Construct and return the dictionary
    analysis_result = {
        "highest": highest,
        "lowest": lowest,
        "average": average_rounded,
        "passed": passed_count,
        "failed": failed_count
    }
    
    return analysis_result


# ─────────────────────────────────────────────
# CALLING THE FUNCTION
# ─────────────────────────────────────────────

# The provided dataset
exam_scores = [72, 88, 45, 95, 60, 53, 78, 91, 40, 85]

# Pass the list to our function and store the returned dictionary
result = analyse_scores(exam_scores)

# Print each result clearly by pulling the values using their keys
print("Exam Analysis Summary:")
print("───────────────────────")
print(f"Highest Score : {result['highest']}")
print(f"Lowest Score  : {result['lowest']}")
print(f"Average Score : {result['average']}")
print(f"Passed        : {result['passed']}")
print(f"Failed        : {result['failed']}")

# === Code Execution Successful ===
# ***********************************
# Exam Analysis Summary:
# ───────────────────────
# Highest Score : 95
# Lowest Score  : 40
# Average Score : 70.7
# Passed        : 8
# Failed        : 2

# ============================================================
#   END OF CLASS 1 HOMEWORK
#   Submit your completed file to your instructor.
# ============================================================