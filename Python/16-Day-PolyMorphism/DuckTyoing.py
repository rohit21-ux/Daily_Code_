# python doesnt care about clas type 
# it only cares about behavior

# it walks like a duck
# it quacks like a duck
# I dont care what class you are ,If you can do the job , I'll let you do it .

class Human:
    def speak(self):
        print("Human says Hello")

class Robot:
    def speak(self):
        print("Robot say Hello")

def talk(who):
    who.speak()

talk(Human())
talk(Robot())

