num = [0,2,3,4,5,6]

for n in num:
    print(n)


# su of elements
num1 = [2,4,6]
sum = 0

for n in num1:
    sum = sum + n

print(sum)

# sqaures of elements

num2 = [2,3,4,5]


for n in num2:
    print("square:",n*n)


num3 = [1,2,3,4,5,6,7,8]

for n in num:
    if n % 2 == 0 :
        print(n)


num4 = [2,4,6,8,9]

largest = num4[0]

for n in num4:
    if n > largest:
        largest = n

print(largest)


# easiest way to find largest element from list is to sort and print last number 

num5 = [23,12,100,34,0,-3,1,2,4]

num5.sort()
print(num5) 
print(num5[-1])  # largest number / element
print(num5[0])   # Smallest number /  element







        

    

