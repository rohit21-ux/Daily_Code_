# An exception is an error that happens during program execution.
# when error  happenes python will stop the program and generate an error message .

# To handle exceptions we can use try and except block .

#syntax: try:  // code that may raise an exception 
#        except:  // code to handle the exception

# Example 1: zero division error

try:
    num =(int(input("Enter a Number: ")))
    print(20/0)
except ZeroDivisionError:
    print("You can not divide a number by zero!")

# Example 2: Value error
except ValueError:
    print("Please enter a valid value!")


