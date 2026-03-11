num = [21,34,60,31,7,9,0,56,78]

print(num[3])
print(num[-1])

print(num[0:4])
num_greater_than_30 = num[1:4]
print(num_greater_than_30)



#num.sort()
#print(num)

num.reverse()
print(num)

num.remove(21)
print(num)

num.append(22)
print(num)

num.extend([30,4,89])
print(num)

num.sort()
print(num)



print(id(num))

print(num.append(33))
print(num)

print(type(num))

tuple1 = tuple(num)
print(id(tuple1))
print(type(tuple1))
print(tuple1)


# Joining two lists 
num1 = [1,2,3,4]
num2 = [-1,-2,-3,-4]
num1.extend(num2)
print('After Joining Numbers:',num1)

# finding largest and smallest from the joined lits  using sort method cause its easy
print('--Using sorting method---') 
num1.sort()
print(num1)
print("Largest number",num1[-1])

print("Smallest number:",num1[0])

print("--Using max() and min()---")
print("Largest:",max(num1))
print("Smallest:",min(num1))


