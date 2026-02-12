try:
    num = int(input("Enter a number:"))
    result = 20 /num
except ZeroDivisionError:
    print("You can not divide a number by zrro!")
except ValueError:
    print("Invalid input")
else:
    print("Result is:",result)
# The else block will be executes if no exception is raised in the try block.

finally:
    print("Execution completed")

# try : main code
# except : error handling code
# else : runs if no error occurs
# finally: always runs no matter what happens
