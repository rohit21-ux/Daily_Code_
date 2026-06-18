from datetime import datetime

# Function to calculate age
def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year

    # Adjust if the birthday has not occurred yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
        
    return age

# Input birthdate (format: YYYY-MM-DD)
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")

# Convert the string input into a datetime object
birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")

# Calculate and print the age
age = calculate_age(birthdate)
print(f"Your age is: {age} years old.")
