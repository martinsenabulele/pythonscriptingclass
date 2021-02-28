# Inheritance is sharing functionalities among multiple classes

from OOP import ApplePhone

class Iphone8(ApplePhone):
    serial_number = 0
    owner = None

    def __init__(self, camera, processor, screen_size):
        self.camera = camera
        self.processor = processor
        self.screen_size = screen_size



    def get_screen_size(self):
        print("the size of screen is %s inches" % self.screen_size)

    def get_processor(self):
        print("the processor of the phone is %s MHz" % self.processor)

    @classmethod
    def update_serial_number(cls):
        cls.serial_number += 1
        cls.owner = "ABC"
        print("The serial number of the is %s" % cls.serial_number)
        print("The owner is %s" % cls.owner)


def f1(): # this is an independent function and what is inside the function should have four spaces gap
    iphone_81= Iphone8(60, 200, 6)
    iphone_81.get_processor()
    iphone_81.get_screen_size()
    iphone_81.can_call()
    iphone_81.click_pic()
    iphone_81.update_serial_number()

    iphone_82 = Iphone8(100, 500, 5)
    iphone_82.get_processor()
    iphone_82.get_screen_size()
    iphone_82.can_call()
    iphone_82.click_pic()
    iphone_82.update_serial_number()


f1()

#types of inheritance
# 1. Single Inheritance = one parent , one child
# 2. Multiple Inheritance = 2 parents, 1 child
# 3. Multilevel Inheritance = 1 parent, 1 child(parent), 1 child
# 4. Hierarchical Inheritance = 1 parent, multiple child
# 5. Hybrid Inheritance = combination of more than one inheritance

#assignment  Implement the above inheritance type with University