#single line comment 
letter = 'a'   # a string could be single character or bunch of texts 
print(letter)
print(len(letter)) # 1,length function to count no of characters in string 

greetings = 'Hello , World!' #string could be a single or double qoutes , "Hello,World!"
print(greetings)
print(len(greetings))

sentence = "I hope you are enjoying learning python "
print(sentence)
print(len(sentence))

# multiline string 
multiline_string = ''' I am a student and want to be a good programmer '''
print(multiline_string)

#Anothere way
multiline_string2 = """I am a student and want to be a good programmer"""
print(multiline_string2)

#string concatination
first_name = "Rohit"
last_name  = "Jagave"
space = " "
full_name = first_name + space + last_name 
print(full_name)

#checking length of strings using len() function 
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

#unpacking characters 
language  = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables 
print(a) #P
print(b) #y
print(c) #t
print(d) #h       
print(e) #o
print(f) #n

# Accessing characters in strings by index 
language  = 'Python'
first_letter  = language[0] #P
print(first_letter)

second_letter =  language[1] #y
print(second_letter)

third_letter = language[2]  #t
print(third_letter)

fourth_letter = language[3]  #h
print(fourth_letter)

last_index = len(language) - 1
last_letter = language[last_index]  #n
print(last_letter)

# If we want to start from right end we can use negative indexing .-1 is the last index character 
language = 'Python'
last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)

#SLICING STRINGS 

language ='Python'
first_four = language[0:4] #starts from index 0 to index 4 but not including index 4 
print(first_four)

last_four = language[2:6]
print(last_four)

#Another way of slicing
language = 'Python'
last_three = language[-3:]
print(last_three)
first_three = language[:3]
print(first_three)
all_characters  = language[:]

#skipping characters while splitting Python strings 
language =  'Python'
pto  = language[0:6:2] #start : end : step
print(pto)

#Escape sequence
#print = ('Hello \n World') #line break pr new line
#print = ('Days\tTopics\tExercises')
#print = ('Day 1\t3\t5')
#print = ('Day 2\t3\t5')

#String Methods
# Capitalize() : converts the first character of the string to capital letter 
#string = 'thirty days of python'
#print(string.capitalize()) # Thirty days of python 


#Count() : returns the number of occurences of substring ,count(substring , start =.., end =..)

string = 'hello everyone good morning'
print(string.count('o')) #3
print(string.count('e')) #5
print(string.count('g',0,20)) #2
print(string.count('ll')) #1

# endswith() : checks if the string ends with the specified ending 

string = 'thirty days of python'
print(string.endswith('on')) #True
print(string.endswith('ion')) #false
print(string.endswith('python')) #True


#expandtabs(): Replace tab characters with spaces , default tab size is 8.It takes tab size argument

expanded_string = 'Hello\tWorld\tPython'
print(expanded_string.expandtabs()) #hello   World   Python
print(expanded_string.expandtabs(5)) #Hello     world    python

#find(): searches the string for a specified value and returns the position of where it was found

string = 'thirty days of python'
print(string.find('y')) 
print(string.find('on'))

#index(): Returns the index of substring 
string = 'thirty days of python '
print(string.index('r')) 
print(string.index('s')) 
#print(string.index('z)) #Value error substring not found

#isalnum(): checks if all character in the string are alphanumetic
string = 'SixtyChocolates'
print(string.isalnum()) #True

string2 = '60Chocolates'
print(string2.isalnum()) #True

string3 = 'Sixty Chocolates'
print(string3.isalnum() ) #False because there is a space 


#isalpha(): checks if all characters in the string are alphabetic 
string =  'Ten Days'
print(string.isalpha())  #False cause of space 

num = '123'
print(num.isalpha()) # False 

word  = 'Python'
print(word.isalpha) #True 

#isdecimal(): checks the decimal characters 

num =  '100'
print('isdecimal:',num.isdecimal())

num = '100.55'
print('isdecimal:',num.isdecimal())

#isdigit(): checks the digit characters
string = 'Four'
print('isdigit:',string.isdigit())

#replace(): replace substring inside 
string = 'six days of week'
print(string.replace('six','seven'))



#-----------------------------END------------------------------------


