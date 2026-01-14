'''Dictionary is a collection of unordered ,modifiable data type and  we store key-paires values 
to create a dictionary we use cur;y brackets {} or the dict() built in function 

'''
# creating empty dictionary 
empty_dict  = {}

# Dictionary with data values 
dict1 = {'key1':'value1','key2':'value2','key3':'value3'}

# creating dictionary using dict() function 
dict2 = dict(key1 ='value',key2 ='value2',key ='value3')
print("Dictionary:",dict2)

#creating dictionary with mixed data types 
person  = {'Name':'Rohit','Last-Name':'Jagave','Age':21,'Is_student':True,'Country':'India','Skills':['Basic -C','HTML-CSS','Python'],'Address':{'City':'Latur','State:':'Maharashtra'}}
print("Person Dictionary with Mixed Data Types:",person)

'''Above dictionary contains various data types like string,integer,boolean,list and another dictionary '''

#Length of dictionary 
print('Length of person dictionary:',len(person)) #7

#Accessing items from dictionary 
person  = {'Name':'Rohit','Last-Name':'Jagave','Age':21,'Is_student':True,'Country':'India','Skills':['Basic -C','HTML-CSS','Python'],'Address':{'City':'Latur','State:':'Maharashtra'}}
print("Person Dictionary with Mixed Data Types:",person)

#Accessing using key 
print("Name:",person['Name'])  #Rohit
print("Last-Name:",person['Last-Name']) #Jagave
print("Age:",person['Age'])    #21
print("IS_student:",person['Is_student'])  #True

''' accessing an item with a non-existing key will raise a keyerror .'''

# To avoid this error we can use get() method .
person  = {'Name':'Rohit','Last-Name':'Jagave','Age':21,'Is_student':True,'Country':'India','Skills':['Basic -C','HTML-CSS','Python'],'Address':{'City':'Latur','State:':'Maharashtra'}}
print("Person Dictionary with Mixed Data Types:",person)

print("Name:",person.get('Name')) #Rohit
print("Middle-name:",person.get('Middle-name')) #None
print("Skills:",person.get('Skills')) #['Basic -C', 'HTML-CSS', 'Python']

#Adding items to dictionary
person = {'Name':'Rohit','Last-Name':'Jagave','Age':21}
print("Original dictionary:",person)

#Adding 'Middle-Name':'Ramkishan' key-value pair to dictionary 
person['Middle-Name:' ] = 'Ramkishan'
print("Dictionary after adding Middle-Name:",person)

#Updating or changing value in dictionary 
person ={'Name':'Rohit','Last-Name':'Jagave','Age':25}
print("Original Dictionary:",person)

#updating age value to 21
person['Age'] = 21
print("After updating Age value:",person )

#udating multiple values using update() method
person ={'Name':'Rohit','Last-Name':'Jagave','Age':25}
print("Original Dictionary:",person)
person.update({'Age':21,'country':'India'})
print("After updating multiple values :",person)

#Checking if keys exists in dictionary
person ={'Name':'Rohit','Last-Name':'Jagave','Age':25}
print("Original Dictionary:",person )
#'Name' in person 
print("Is 'Name'key exists in dictionary?:",'Name' in person) #true

'''
   Removing key and value pairs from a dictionary 
   pop(key) : removes the item with the specified key name
   popitem(): removes the last value
   del: removes an item withh specified key name
'''
dict1 = {'key1':'value1','key2':'value2','key3':'value3'}
print("Original Dictionary:",dict1)

#using the pop(key) method 
dict1.pop('key2')
print("after using pop():",dict1)

#using the popitem() mehtod 
dict1.popitem()
print("after using popitem();",dict1)

#using the del keyword
del dict1['key1']
print("after using del keyword:",dict1) #empty dictionary

#if we dont want the items in dictionary we can use clear() method ,not for permanent deletion 
dict1 = {'key1':'value1','key2':'value2','key3':'value3'}
print("Original dictionary:",dict1)
dict1.clear()
print("after ussing clear() mehtod :",dict1) #empty dictionary 

#Deleting a dictionary 
dict1 = {'key1':'value1','key2':'value2','key3':'value3'}
del dict1
#print(dict1) this will raise error

#copying a dictionary 
dict1 = {'key1':'value1','key2':'value2','key3':'value3'}
dict1_copy = dict1.copy()
print(dict1_copy)

#changing dictionary to a list of items
dict1 = {'key1':'value1','key2':'value2','key3':'value3'}
print(dict1.items()) 

#Getting dictionary keys as a list
dict1 = {'key1':'value1','key2':'value2','key3':'value3'}
keys = dict1.keys()
print("Dicionary keys :",keys)

#getting dictionary values as a list
dict1 = {'key1':'value1','key2':'value2','key3':'value3'}
values = dict1.values()
print("Dicitonary values:",values)

#looping through a dictionary
dict1 = {'key1':'value1','key2':'value2','key3':'value3'}
for key in dict1:
    print(key,':',dict1[key])

for key,value in dict1.items():
    print(key,':',value)