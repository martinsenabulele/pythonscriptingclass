# OOP ==  object oriented programing
#Inheritance, polymorphism, variable scopes
# Variable == stores data
# functions == Stores instruction

# class == date and instruction
# every class have attribute and functionalities
# function created inside a class is called method.
#__init__ ==initialise == assign memory to the object -- constructor
#class which will be inherited is known as parent class and class which will inherit is child class

class ApplePhone: #parent class
    def __init__(self, camera, logo):
        self.camera = camera #atributes. the variable of class is called attribute
        self.logo = logo #atribute

    def can_call(self): #method
        print("Yes I can call.")
        self.color('black')

    def click_pic(self): #method
        print("Yes i can click pics using %s Megapixel camera." % self.camera)

    def color(self, color):
        print(color)


class Iphone8(ApplePhone):
    def __init__(self, camera, processor, screen_size):
        self.camera = camera
        self.processor = processor
        self.screen_size = screen_size

    def get_screen_size(self):
        print("the size of screen is %s inches" % self.screen_size)

    def get_processor(self):
        print("the processor of the phone is %s MHz" % self.processor)

#iphone_81= Iphone8(60, 200, 6)
#iphone_81.get_processor()
#iphone_81.get_screen_size()
#iphone_81.can_call()
#iphone_81.click_pic()



#iphone = ApplePhone(50, "apple_logo")
#iphone.camera
#iphone.can_call()
#iphone.color("yellow")
#print(dir(iphone))
#iphone.click_pic()

iphone12 = ApplePhone(32, "apple_logo")

#destructor __del__ == delete free up the memory

class ToyotaCamry:
    def __init__(self, gear, brake):
        self.gear = gear
        self.brake = brake

    def can_move(self):
        print("Yes I can move.")

    def press_stop(self):
        print("Yes i can stop.")


#camry = ToyotaCamry(6, "awd")
#camry.can_move()
#camry.press_stop()

#self is the instance of the object
#attribute are object properties

#assignment: create a class for student- 10 attributes and 5 methods
#defining the class
class Student:
    #defining the init
    def __init__(self, name, age, phone, email, registration_number, course, address, level, sex ):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email
        self.registration_number = registration_number
        self.address = address
        self.sex = sex
        self.level =level
        self.course= course
    #creating the method
    def full_name(self, name):
            print("my name is John Paul")
            print(name)

    def my_age(self):
        print("I'm 25 years old")

    def my_phone(self):
        print("my my mobile phone number is +12046981007")

    def my_email(self):
        print("my email address is john_paul@gmail.com")

    def my_course(self):
        print("I'm a medical final year at the university of Chicago")

#creating the object
details = Student("john", 38, "+120469810007", "john_paul@gmail.com", 35894, "Medicine", "708 martins street","Final year", "male")
#calling the method
#details.full_name("John Paul")
#details.my_age()
#details.my_phone()
#details.my_email()
#details.my_course()

# interface
class Iphone8_ultra:
    def __init__(self, camera, screen, logo):
        self.camera = camera
        self.screen = screen
        self.logo =logo

        self.apple_phone =ApplePhone(self.camera, self.logo)

def f3():
    iphone_8ui = Iphone8_ultra(60, 6, 'logo')
    iphone_8ui.apple_phone.click_pic()

f3()


#Polymorphism --> poly== multiple, morphism = forms
#compile time polymorphism --> method overloading (python doesn't supports) operator overload
#Run time polymorphism --> method overriding
#