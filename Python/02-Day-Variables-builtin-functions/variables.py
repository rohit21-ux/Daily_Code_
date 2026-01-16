#variables in python 

first_name = "Rohit "
last_name = "Jagave"
country = "India"
city = "pune"
age = 21
is_married = False
skills = ['python', 'c++','c','Win32','Django']
person_info = {
    'first_name': "Rohit",
    'last_name': "Jagave",
    'country': "India",
    'city': "pune"
}

#printing the values stored inside the variables 

print('First Name:', first_name)
print('First Name length:', len(first_name))

print('Last Name:', last_name)
print('Last Name length:', len(last_name))

print('Country:', country)
print('City:',city)
print('Age:',age)
print('Is married:', is_married)
print('Skills:',skills)
print('Person Info:',person_info)

#declaring multiple variables in one line
first_name,last_name,country,age,is_married = 'Rohit','Jagave','India',21,False

print(first_name,last_name,country,age,is_married)
print('First Name:', first_name)
print('Last Name:', last_name)
print('Country:', country)
print('Age:', age)
print('Is Married:', is_married)
