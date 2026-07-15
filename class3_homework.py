# ============================================================
#   CLASS 3 — HOMEWORK QUESTIONS
#   Functions, Loops & OOP
#   Total Questions: 10
# ============================================================
#   Instructions:
#     - Write your answer below each question.
#     - Do NOT delete the question comments.
#     - Run your code after each question to test it.
#     - Questions 1-3  → Functions
#     - Questions 4-6  → Loops
#     - Questions 7-10 → OOP
# ============================================================


# ─────────────────────────────────────────────
# QUESTION 1 — Functions (Basic)
# ─────────────────────────────────────────────
# A mobile phone shop gives discounts based on the price:
#
#   Price >= 100,000  → 15% discount
#   Price >= 50,000   → 10% discount
#   Price >= 20,000   →  5% discount
#   Price <  20,000   →  No discount
#
# Write a function called phone_discount(price) that:
#   1. Figures out the correct discount percentage.
#   2. Calculates the discount amount.
#   3. Calculates the final price after discount.
#   4. RETURNS the final price.
#
# Then call it 3 times with different prices and print results.
#
# Example:
#   phone_discount(120000) → Final price: Rs.102000.0 (15% off)
#   phone_discount(60000)  → Final price: Rs.54000.0  (10% off)
#   phone_discount(15000)  → Final price: Rs.15000.0  (no discount)

# Write your code below:

def phone_discount(price):
    if price >= 100000:
        discount_percent = 15
    elif price >= 50000:
        discount_percent = 10
    elif price >= 20000:
        discount_percent = 5
    else:
        discount_percent = 0

    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount

    return final_price


price1 = 120000
final1 = phone_discount(price1)
print(f"Final price: Rs.{final1} (15% off)")

price2 = 60000
final2 = phone_discount(price2)
print(f"Final price: Rs.{final2} (10% off)")

price3 = 15000
final3 = phone_discount(price3)
print(f"Final price: Rs.{final3} (no discount)")




# ─────────────────────────────────────────────
# QUESTION 2 — Functions (Default Parameters + Return)
# ─────────────────────────────────────────────
# Write a function called pizza_order(size, toppings=1, extra_cheese=False)
# that calculates the total price of a pizza order.
#
# Pricing rules:
#   Size:
#     "small"  → Rs. 400
#     "medium" → Rs. 650
#     "large"  → Rs. 900
#   Each topping costs Rs. 80  (toppings default = 1)
#   Extra cheese adds Rs. 120  (extra_cheese default = False)
#
# The function should:
#   - Calculate and RETURN the total price.
#   - Print a short summary inside the function showing what was ordered.
#
# Call the function at least 3 times with different combinations.
#
# Example:
#   pizza_order("large", toppings=3, extra_cheese=True)
#   → Large pizza | 3 toppings | Extra cheese: Yes | Total: Rs.1260

# Write your code below:
def pizza_order(size, toppings=1, extra_cheese=False):
    if size == "small":
        base_price = 400
    elif size == "medium":
        base_price = 650
    elif size == "large":
        base_price = 900
    else:
        print("Invalid pizza size")
        return 0

    toppings_price = toppings * 80

    if extra_cheese:
        cheese_price = 120
        cheese_text = "Yes"
    else:
        cheese_price = 0
        cheese_text = "No"

    total_price = base_price + toppings_price + cheese_price

    print(f"{size.capitalize()} pizza | {toppings} toppings | Extra cheese: {cheese_text} | Total: Rs.{total_price}")

    return total_price


# Function calls with different combinations
pizza_order("large", toppings=3, extra_cheese=True)
pizza_order("medium", toppings=2)
pizza_order("small", extra_cheese=True)




# ─────────────────────────────────────────────
# QUESTION 3 — Functions (Multiple Return Values + Scope)
# ─────────────────────────────────────────────
# Write a function called analyse_text(sentence) that:
#   1. Counts the total number of words.
#   2. Counts the total number of characters (excluding spaces).
#   3. Finds the longest word.
#   4. Returns ALL THREE values at once.
#
# Then ask the user to enter a sentence and call the function.
# Print the results clearly.
#
# Example:
#   Input   : "Python is an amazing programming language"
#   Output  :
#     Words       : 6
#     Characters  : 36
#     Longest word: programming

# Write your code below:

def analyse_text(sentence):
    words = sentence.split()

    total_words = len(words)
    total_characters = len(sentence.replace(" ", ""))
    longest_word = max(words, key=len)

    return total_words, total_characters, longest_word


user_sentence = input("Enter a sentence: ")

words_count, characters_count, longest = analyse_text(user_sentence)

print(f"Words       : {words_count}")
print(f"Characters  : {characters_count}")
print(f"Longest word: {longest}")


# ─────────────────────────────────────────────
# QUESTION 4 — Loops (for + range + accumulator)
# ─────────────────────────────────────────────
# A factory produces items every day of the week.
# Daily production numbers (Monday to Sunday):
#
#   production = [120, 95, 140, 110, 130, 80, 60]
#
# Write a program using a for loop that:
#   1. Prints each day's production with the day name.
#      (index 0 = Monday, index 1 = Tuesday, ... index 6 = Sunday)
#   2. Tracks and prints the RUNNING TOTAL after each day.
#   3. After the loop, prints:
#        - Total weekly production
#        - Highest single-day production
#        - Lowest single-day production
#        - Average daily production (rounded to 1 decimal)
#        - Number of days that met the target (target = 100 units)
#
# Example output (first 2 lines):
#   Monday    : 120 units | Running Total: 120
#   Tuesday   :  95 units | Running Total: 215

# Write your code below:

production = [120, 95, 140, 110, 130, 80, 60]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

running_total = 0
target_days = 0
target = 100

for i in range(len(production)):
    running_total += production[i]

    if production[i] >= target:
        target_days += 1

    print(f"{days[i]:<9}: {production[i]:>3} units | Running Total: {running_total}")

total_weekly_production = running_total
highest_production = max(production)
lowest_production = min(production)
average_production = total_weekly_production / len(production)

print("\nWeekly Summary")
print(f"Total weekly production     : {total_weekly_production}")
print(f"Highest single-day production: {highest_production}")
print(f"Lowest single-day production : {lowest_production}")
print(f"Average daily production     : {average_production:.1f}")
print(f"Days that met target         : {target_days}")




# ─────────────────────────────────────────────
# QUESTION 5 — Loops (while + break + continue)
# ─────────────────────────────────────────────
# Build a simple QUIZ GAME using a while loop.
#
# Rules:
#   - Store at least 4 questions in a list. Each question is a
#     tuple: (question_text, correct_answer)
#   - Ask each question one by one.
#   - If the answer is correct → print "Correct! ✔" and add 1 point.
#   - If the answer is wrong   → print "Wrong! The answer was X."
#   - If the user types "skip" → use continue to skip that question.
#   - If the user types "quit" → use break to end the game early.
#   - At the end, print the final score out of total questions asked.
#
# Sample questions you can use (or make your own):
#   ("What is the capital of Pakistan?", "islamabad")
#   ("How many days are in a week?", "7")
#   ("What language are we learning?", "python")
#   ("What is 15 + 27?", "42")

# Write your code below:
questions = [
    ("What is the capital of Pakistan?", "islamabad"),
    ("How many days are in a week?", "7"),
    ("What language are we learning?", "python"),
    ("What is 15 + 27?", "42")
]

score = 0
asked = 0
index = 0

while index < len(questions):
    question_text, correct_answer = questions[index]

    answer = input(question_text + " ").lower()

    if answer == "quit":
        print("Game ended early.")
        break

    if answer == "skip":
        index += 1
        continue

    asked += 1

    if answer == correct_answer:
        print("Correct! ✔")
        score += 1
    else:
        print(f"Wrong! The answer was {correct_answer}.")

    index += 1

print(f"Final score: {score} out of {asked}")



# ─────────────────────────────────────────────
# QUESTION 6 — Loops (Nested loops — real-world)
# ─────────────────────────────────────────────
# A school has 3 classes: A, B, C.
# Each class has 4 students with the following marks:
#
#   class_data = {
#       "Class A": [85, 72, 91, 68],
#       "Class B": [55, 78, 63, 90],
#       "Class C": [40, 88, 74, 59],
#   }
#
# Write a program using NESTED LOOPS that:
#   1. Loops through each class.
#   2. Inside, loops through each student's marks.
#   3. Prints each student's mark and whether they Passed (>=50) or Failed.
#   4. After each class, prints the class average.
#   5. After all classes, prints which class had the HIGHEST average.
#
# Example (for Class A):
#   Class A:
#     Student 1: 85 → Pass
#     Student 2: 72 → Pass
#     Student 3: 91 → Pass
#     Student 4: 68 → Pass
#   Class A Average: 79.0

# Write your code below:
class_data = {
    "Class A": [85, 72, 91, 68],
    "Class B": [55, 78, 63, 90],
    "Class C": [40, 88, 74, 59],
}


highest_average = 0
highest_class = ""

for class_name, marks in class_data.items():
    print(f"{class_name}:")

    total_marks = 0

    for i in range(len(marks)):
        mark = marks[i]
        total_marks += mark

        if mark >= 50:
            result = "Pass"
        else:
            result = "Fail"

        print(f"  Student {i + 1}: {mark} → {result}")

    class_average = total_marks / len(marks)
    print(f"{class_name} Average: {class_average:.1f}")
    print()

    if class_average > highest_average:
        highest_average = class_average
        highest_class = class_name

print(f"Highest average: {highest_class} with {highest_average:.1f}")



# ─────────────────────────────────────────────
# QUESTION 7 — OOP (Class + __init__ + Methods)
# ─────────────────────────────────────────────
# Create a class called MobilePhone with:
#
#   Attributes (set in __init__):
#     brand       → e.g. "Samsung"
#     model       → e.g. "Galaxy S24"
#     battery     → starts at 100 (always, regardless of input)
#     is_on       → starts as False (phone is off by default)
#
#   Methods:
#     power_on()        → if already on, print "Already on."
#                         otherwise set is_on = True and print a message.
#     power_off()       → if already off, print "Already off."
#                         otherwise set is_on = False and print a message.
#     make_call(mins)   → if phone is off, print "Turn on the phone first."
#                         otherwise reduce battery by (mins * 2).
#                         If battery drops below 0, set it to 0 and
#                         print "Battery died during the call!"
#                         Otherwise print call duration and remaining battery.
#     charge(percent)   → increase battery by percent, max 100.
#                         Print the new battery level.
#     status()          → print brand, model, battery %, and on/off state.
#
# Create TWO phones and test all methods on each.

# Write your code below:

class MobilePhone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery = 100
        self.is_on = False

    def power_on(self):
        if self.is_on:
            print("Already on.")
        else:
            self.is_on = True
            print(f"{self.brand} {self.model} is now on.")

    def power_off(self):
        if not self.is_on:
            print("Already off.")
        else:
            self.is_on = False
            print(f"{self.brand} {self.model} is now off.")

    def make_call(self, mins):
        if not self.is_on:
            print("Turn on the phone first.")
        else:
            self.battery -= mins * 2

            if self.battery <= 0:
                self.battery = 0
                print("Battery died during the call!")
            else:
                print(f"Call duration: {mins} minutes")
                print(f"Remaining battery: {self.battery}%")

    def charge(self, percent):
        self.battery += percent

        if self.battery > 100:
            self.battery = 100

        print(f"Battery level: {self.battery}%")

    def status(self):
        if self.is_on:
            state = "On"
        else:
            state = "Off"

        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery: {self.battery}%")
        print(f"State: {state}")


# Create TWO phones
phone1 = MobilePhone("Samsung", "Galaxy S24")
phone2 = MobilePhone("Apple", "iPhone 15")

# Test phone1
print("Phone 1 Test:")
phone1.status()
phone1.make_call(5)
phone1.power_on()
phone1.power_on()
phone1.make_call(10)
phone1.charge(15)
phone1.power_off()
phone1.power_off()
phone1.status()

print("\nPhone 2 Test:")
phone2.status()
phone2.power_on()
phone2.make_call(60)
phone2.charge(50)
phone2.power_off()
phone2.status()




# ─────────────────────────────────────────────
# QUESTION 8 — OOP (Class with a list + methods)
# ─────────────────────────────────────────────
# Create a class called ShoppingCart that models an
# online shopping cart.
#
#   Attributes (set in __init__):
#     customer_name  → name of the customer
#     items          → empty list (will store dictionaries)
#
#   Each item in the list is a dictionary:
#     { "name": "Milk", "price": 120, "qty": 2 }
#
#   Methods:
#     add_item(name, price, qty=1)
#       → Add the item to the list. If the item already exists,
#         increase its quantity instead.
#
#     remove_item(name)
#       → Remove the item by name. If not found, print a message.
#
#     get_total()
#       → Return the total cost (price × qty for all items).
#
#     view_cart()
#       → Print a formatted receipt showing all items,
#         their quantities, prices, and the grand total.
#
# Create a cart, add 4 items, remove 1, then print the receipt.

# Write your code below:

class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, name, price, qty=1):
        for item in self.items:
            if item["name"] == name:
                item["qty"] += qty
                print(f"{name} quantity updated.")
                return

        new_item = {
            "name": name,
            "price": price,
            "qty": qty
        }

        self.items.append(new_item)
        print(f"{name} added to cart.")

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                print(f"{name} removed from cart.")
                return

        print(f"{name} not found in cart.")

    def get_total(self):
        total = 0

        for item in self.items:
            total += item["price"] * item["qty"]

        return total

    def view_cart(self):
        print("─────────────────────────────")
        print(f"Receipt for {self.customer_name}")
        print("─────────────────────────────")

        if len(self.items) == 0:
            print("Cart is empty.")
        else:
            for item in self.items:
                item_total = item["price"] * item["qty"]
                print(f"{item['name']} | Qty: {item['qty']} | Price: Rs.{item['price']} | Total: Rs.{item_total}")

            print("─────────────────────────────")
            print(f"Grand Total: Rs.{self.get_total()}")
            print("─────────────────────────────")


cart = ShoppingCart("Sara")

cart.add_item("Milk", 120, 2)
cart.add_item("Bread", 100, 1)
cart.add_item("Eggs", 300, 1)
cart.add_item("Rice", 250, 2)

cart.remove_item("Bread")

cart.view_cart()


# ─────────────────────────────────────────────
# QUESTION 9 — OOP (Inheritance)
# ─────────────────────────────────────────────
# Create a base class called Employee with:
#   Attributes: name, employee_id, base_salary
#   Methods:
#     get_info()     → print name, ID, and base salary
#     get_salary()   → return base_salary
#
# Then create TWO child classes that inherit from Employee:
#
#   class FullTimeEmployee(Employee):
#     Extra attribute: department
#     Overrides get_salary() → adds a monthly bonus of Rs. 5,000
#     Overrides get_info()   → also shows department + final salary
#
#   class PartTimeEmployee(Employee):
#     Extra attribute: hours_per_week
#     Overrides get_salary() → salary = base_salary × (hours_per_week / 40)
#     Overrides get_info()   → also shows hours per week + final salary
#
# Create at least 2 full-time and 2 part-time employees.
# Store all 4 in a single list.
# Loop through the list and call get_info() on each.
# At the end, print who earns the most.

# Write your code below:
class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Base Salary: Rs.{self.base_salary}")

    def get_salary(self):
        return self.base_salary


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, department):
        super().__init__(name, employee_id, base_salary)
        self.department = department

    def get_salary(self):
        return self.base_salary + 5000

    def get_info(self):
        print("Full-Time Employee")
        print(f"Name: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Base Salary: Rs.{self.base_salary}")
        print(f"Final Salary: Rs.{self.get_salary()}")
        print()


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, hours_per_week):
        super().__init__(name, employee_id, base_salary)
        self.hours_per_week = hours_per_week

    def get_salary(self):
        return self.base_salary * (self.hours_per_week / 40)

    def get_info(self):
        print("Part-Time Employee")
        print(f"Name: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Hours per week: {self.hours_per_week}")
        print(f"Base Salary: Rs.{self.base_salary}")
        print(f"Final Salary: Rs.{self.get_salary()}")
        print()


employees = [
    FullTimeEmployee("Sara", 101, 60000, "IT"),
    FullTimeEmployee("Ali", 102, 55000, "HR"),
    PartTimeEmployee("Ahmed", 201, 40000, 20),
    PartTimeEmployee("Ayesha", 202, 50000, 25)
]

highest_employee = employees[0]

for employee in employees:
    employee.get_info()

    if employee.get_salary() > highest_employee.get_salary():
        highest_employee = employee

print(f"Highest earner: {highest_employee.name} with Rs.{highest_employee.get_salary()}")



# ─────────────────────────────────────────────
# QUESTION 10 — OOP (Full Mini Project)
# ─────────────────────────────────────────────
# Build a HOSPITAL APPOINTMENT SYSTEM using OOP.
#
# Create a class called Doctor with:
#   Attributes: name, specialization, fee
#   Method: get_info() → print doctor details
#
# Create a class called Appointment with:
#   Attributes:
#     patient_name
#     doctor         → a Doctor OBJECT (not just a name)
#     date
#     is_confirmed   → starts as False
#   Methods:
#     confirm()      → set is_confirmed = True, print confirmation
#     cancel()       → set is_confirmed = False, print cancellation
#     summary()      → print full details of the appointment
#
# Create a class called Hospital with:
#   Attributes:
#     hospital_name
#     appointments   → empty list
#   Methods:
#     book_appointment(patient_name, doctor, date)
#       → create an Appointment object and add to the list
#     view_all()     → print summary of every appointment
#     count_confirmed() → return how many appointments are confirmed
#
# Demo:
#   1. Create 2 or 3 Doctor objects.
#   2. Create a Hospital object.
#   3. Book 3 or 4 appointments using different doctors.
#   4. Confirm some, cancel some.
#   5. Call view_all() and count_confirmed().

# Write your code below:

class Doctor:
    def __init__(self, name, specialization, fee):
        self.name = name
        self.specialization = specialization
        self.fee = fee

    def get_info(self):
        print(f"Doctor Name: {self.name}")
        print(f"Specialization: {self.specialization}")
        print(f"Fee: Rs.{self.fee}")


class Appointment:
    def __init__(self, patient_name, doctor, date):
        self.patient_name = patient_name
        self.doctor = doctor
        self.date = date
        self.is_confirmed = False

    def confirm(self):
        self.is_confirmed = True
        print(f"Appointment for {self.patient_name} has been confirmed.")

    def cancel(self):
        self.is_confirmed = False
        print(f"Appointment for {self.patient_name} has been cancelled.")

    def summary(self):
        if self.is_confirmed:
            status = "Confirmed"
        else:
            status = "Not Confirmed"

        print("─────────────────────────────")
        print(f"Patient Name: {self.patient_name}")
        print(f"Doctor: {self.doctor.name}")
        print(f"Specialization: {self.doctor.specialization}")
        print(f"Fee: Rs.{self.doctor.fee}")
        print(f"Date: {self.date}")
        print(f"Status: {status}")


class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.appointments = []

    def book_appointment(self, patient_name, doctor, date):
        appointment = Appointment(patient_name, doctor, date)
        self.appointments.append(appointment)
        print(f"Appointment booked for {patient_name} with Dr. {doctor.name}.")
        return appointment

    def view_all(self):
        print(f"\nAppointments at {self.hospital_name}")
        for appointment in self.appointments:
            appointment.summary()

    def count_confirmed(self):
        count = 0

        for appointment in self.appointments:
            if appointment.is_confirmed:
                count += 1

        return count


# Demo

doctor1 = Doctor("Ali Khan", "Cardiologist", 3000)
doctor2 = Doctor("Sara Ahmed", "Dermatologist", 2500)
doctor3 = Doctor("Hamza Malik", "Neurologist", 4000)

hospital = Hospital("City Care Hospital")

appointment1 = hospital.book_appointment("Ahmed", doctor1, "20 July 2026")
appointment2 = hospital.book_appointment("Ayesha", doctor2, "21 July 2026")
appointment3 = hospital.book_appointment("Bilal", doctor3, "22 July 2026")
appointment4 = hospital.book_appointment("Fatima", doctor1, "23 July 2026")

appointment1.confirm()
appointment2.confirm()
appointment3.cancel()
appointment4.confirm()

hospital.view_all()

print(f"\nConfirmed appointments: {hospital.count_confirmed()}")


# ============================================================
#   END OF CLASS 3 HOMEWORK
#   Submit your completed file to your instructor.
# ============================================================