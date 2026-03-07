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




