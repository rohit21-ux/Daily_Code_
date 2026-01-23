#Class_vs_Instance_Variables
#Class variables describe the group
#Instance variables describe the individual
class Vehicle :
     Type = "Car"  # Type is a class variable

     def __init__(self,name):
        self.name = name

p1 = Vehicle("BMW")  #p1 is instance variable 
p2 = Vehicle("Audi")  # instance variable belong to ONE object only

#brand = "Suzuki"
#print(Type)

print("---printing class variable---")
print(p1.Type)
print(p2.Type)

print("---printing instance variable---")
print(p1.name)
print(p2.name)

#changing class variable
#---Class variables are shared, so change them using the class name — not objects.
Vehicle.Type = "Bike"
print("--changed class variable---")
print(p1.Type)
print(p2.Type)




        