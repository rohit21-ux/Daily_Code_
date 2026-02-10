# issubclass() - is used to check if a class is a subclass of another class
#syntax : issubclass(class,classinfo) class - the class you want to test ,classinfo - another class or a tuple of class

class Art:
    pass

class Music(Art):
    pass

class Flute(Art):
    pass

class Running:
    pass

print(issubclass(Music,Art)) #True 
print(issubclass(Flute,Art)) # True - because of inheritance
print(issubclass(Running,Art)) #False



