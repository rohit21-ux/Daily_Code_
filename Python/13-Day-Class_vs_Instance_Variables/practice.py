class Company:
    company_name = "Google" # class variable (shared by all objects)


    def __init__(self, emp_name):
        self.emp_name = emp_name  # instance variable (unique per object)


c1 = Company("Rohit")
c2 = Company("Akash")

print(c1.company_name)
print(c2.company_name)

print(c1.emp_name)
print(c2.emp_name)

#change class variable 
Company.company_name = "TCS"
print(c1.company_name)

#change in instance variable
c1.emp_name = "Shree"
c2.emp_name= "Ram"

print(c1.emp_name)
print(c2.emp_name)

print(c1.__dict__)
print(c2.__dict__)
