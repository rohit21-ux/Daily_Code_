# File handling is mainly used for:
# 1. storing and saving user data
# 2. Log files
# 3. Projects
# 4. Backend systems
# 5. storing results of program

# 1. Open a file

file =  open("file.txt","w")
file.write("Hello Rohit!") 
file.close()

# Diffrent modes of opening a file:
# 1. "r"  - read mode only
# 2. "w"  - write mode (overwrie existing content)
# 3. "a"  - Append mode (add content to the end of file)
# 4. "x"  - create file if it does not exist,else raise error


with open("file.txt","w") as file:
    file.write("Python day 20")

# 2. Read a file
with open("file.txt","r") as file:
    content = file.read()
    print(content)

# other methods to read a file:
file.readline() # one line only
file.readlines() # list of lines


# Appending to a file
with open("file.txt","a") as file:
    file.write("\n New line added")

# Handling file errors

try:
    with open("file.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exists.")


