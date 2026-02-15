username = input("Enter your username:")

with open("user.txt","w") as file:
    file.write(username + "\n")

print("Username saved successfully!")

#Read and display all users
print("All users:")
with open("user.txt","r") as file:
    for line in file:
        print(line.strip())



    