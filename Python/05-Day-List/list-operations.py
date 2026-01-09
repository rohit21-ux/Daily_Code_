#empty list with no elements 
empty_list = list()
print(len(empty_list)) #0

# lists is collection of ordered elements and its mutable means changable .

fruits = ['Mango','Apple','Orange']
vegetables =  ['Tomato', 'Potato','Cabbage','carrot']

print('Fruits:',fruits)
print(len(fruits))

print('Vegetables:',vegetables)
print(len(vegetables))

#lists can have different data types 
list = ['Rohit',233,True,{'country':'India','City':'Pune'}]
print(type(list))
print(len(list))
print(list.index(True))


# accessing elements using positive indexing 
car_brand = ['BMW','TATA','TOYOTA','AUDI']

first_car_brand = car_brand[0]
print(first_car_brand)
print(len(first_car_brand))

last_car_brand = car_brand[-1]
print(last_car_brand)
print(len(last_car_brand))

# accessing elements using negatuive indexing 
names  = ['rohit','sam','ram','john']
first_name = names[-4]
second_name = names[-3]
last_name = names[-1]

print(first_name)  #rohit
print(second_name) #sam
print(last_name)   #john

#Unpacking List Items 

car_brand = ['BMW','TATA','TOYOTA','AUDI','MAHINDRA']
first_car_brand, second_car_brand,third_car_brand, *rest = car_brand

print(first_car_brand)
print(second_car_brand)
print(third_car_brand)
print(rest)


#Slicing 
car_brand = ['BMW','TATA','TOYOTA','AUDI']
#0 is starting and 4 is where it stops 
all_cars = car_brand[0:4]
print(all_cars)

#it doesnt set where to stop it takes all elements 
all_cars2 = car_brand[0:]
print(all_cars2)

BMW_AUDI = all_cars[0::3]
print(BMW_AUDI)

TATA_AUDI = all_cars[1::2] #here list becomes ['TATA','TOYOTA','AUDI'] where 0 index is TATA and 2 index is AUDI
print(TATA_AUDI)


#Modifying lists 
car_brand = ['BMW','TATA','TOYOTA','AUDI']
car_brand[0] = 'MAHINDRA'
print(car_brand) #['MAHINDRA','TATA','TOYOTA','AUDI']

car_brand[1] = 'FARRARI'
print(car_brand)  #['MAHINDRA','FARRARI','TOYOTA','AUDI'] 

#checking items in list 
car_brand = ['BMW','TATA','TOYOTA','AUDI']
doest_exist = 'BMW' in car_brand
print(doest_exist)

#Adding items to a list 

car_brand = ['BMW','TATA','TOYOTA','AUDI']
car_brand.append('MAHINDRA')
print(car_brand)

#INSERT
car_brand.insert(2,'FARRARI') #list.insert(index,'item')
print(car_brand)

#REMOVE
car_brand.remove('FARRARI')
print(car_brand)

#REMOVING using pop
car_brand.pop(0)
print(car_brand)

#REMOVING using del
car_brand = ['BMW','TATA','TOYOTA','AUDI']
del car_brand[-1]
print(car_brand)

del car_brand[1]
print(car_brand)

#clear function 
car_brand =  ['BMW','TATA','TOYOTA','AUDI']
car_brand.clear()  # removes all elements from list []
print(car_brand)

#copying a list
car_brand =  ['BMW','TATA','TOYOTA','AUDI']
car_brand_copy = car_brand.copy()
print(car_brand_copy)

# join 
num1 = [1,2,3,4]
num2 = [-1,-2,-3,-4]
num1.extend(num2)
print('After Joining Numbers:',num1)

#count
car_brand =  ['BMW','TATA','TOYOTA','AUDI']
print(car_brand.count('BMW'))  #1

ages =[12,23,23,45,46,87]
print(ages.count(23))

#index 
car_brand= ['BMW','TATA','TOYOTA','AUDI']
print(car_brand.index('BMW')) #index = 0

ages =[12,22,23,45,46,87]
print(ages.index(45)) #index  = 3

#Reverse 
car_brand =  ['BMW','TATA','TOYOTA','AUDI']
car_brand.reverse()
print(car_brand)

ages =[12,45,67,54,23,45,46,87] 
ages.sort()
print(ages)    #[12, 23, 45, 45, 46, 54, 67, 87]

ages.sort(reverse=True) 
print(ages)   # [87, 67, 54, 46, 45, 45, 23, 12]