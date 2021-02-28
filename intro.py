
# python is a high level language -Devops, Web dev, Games, Desktop, Data science
# python executes - compiler, interpreter
#compiler take the programing language process it into machine readable format, interpreter does the same thing but compiler read
#read the complete py file and convert while interpreter take it one by one.
#why python? Easy to learn syntax and clean, less amount of code , a lot of different developers are working in it
#Python- everything is an object.
#python 2+, 3+
#program is a set of instruction
#Variables - variable is ability to vary
#bugs are errors in the system. to reduce the bugs , the role is less code less bug. code re-use is very important
#Two ways to reuse your code: I functions and 2 Objects (OOPS Concepts)
# how to create function
# function only execute when the function name is called .
# We functions we can reuse the code multiple time.
#def meaning define .
def abc():
    a = 5 + 2
    b = a - 3
    c= b * 4
    d  = c/5

    print(a)
    print(b)
    print(c)
    print(d)
    return d

result = abc()
print("==========")
print(result)

# result was used as a variable to store functions.


# when you define a function to add any line you must give four spaces before adding any line

# Types of Data
# 1. Integer = 1,2,3,4,5
# 2. Float  = 1.2, 2.3 , 3.4
# 3. String = "abe" "apple" "Martins" whatever is inside a quote is considered as a string
#
def fruits():
    g = "apple"
    h = "orange"
    i = "mango"
    j = "watermelon"
    print(g)
    print(h)
    print(i)
    print(j)
    return g

name = fruits()
print(name)

#Assignment: write a function that calculate area and perimeter of a rectangle
# it will print the perimeter of the rectangle and return the value of the area of rectangle .
# Do similar thing for square.

man = 76
def rectangle():
    l = 45    # where l = length
    w = 95  # where w = width
    area  = l * w
    perimeter = 2 * (l + w)
    print(perimeter)
    print(man)
    return area
math = rectangle()
print(math)
print(man)
def square():
    l = 45    # where l = length
    w = 45  # where w = width
    area  = l * w
    perimeter = 2 * (l + w)
    print(perimeter)
    return area
maths = square()
print(maths)

def rect():
    l=int(input("length :"))
    w=int(input("width :"))
    area = l * w
    perimeter = 2 *(l+w)
    print("Area of Rectangle : ", area)
    print("Perimeter of a Rectangle : " , perimeter)
    return area

expectation = rect()
print(expectation)

# Variable lifetime is called scope and they of two type local and global variables.
# local variable are variable that can only be access in the python files, while global can be access
# anywhere from anywhere and it is declared outside the function , but for clean code, use it less frequently .

def xyz(x, y): # parameter
    a = x + y
    b = a- 3
    c = b * 5
    d = c/5
    return d,a
results1, results2 =xyz(5,3) #argumment
print(results1)
print(results2)

def rectangle1(l, w):
    area = l * w
    perimeter = 2 * (l + w)
    return area, perimeter

answer1, answer2 = rectangle1(180, 95)
print("Area of Rectangle is : ", answer1)
print("Perimeter of a Rectangle is : ", answer2)

# this is based on positional arguments
# two types of passing arguments: Positional Argument , arg based on position and the second is keyword arg.

# Fibonacci series
# create a function which will take marks for three subject : English Maths and Biology - calculate total marks,
#average and percentage  for 5 student make denominator of the average global variable.

# Solution
#let e = English, m = Maths, b = Biology.
# parameters : total mark, Average and percentage
Average = 3

def score(e, m, b):
    total_mark = e + m + b
    percentage = (total_mark/300)*100
    average_score = total_mark/Average
    return total_mark, percentage, average_score

John_total_mark, John_percentage, John_average_score =score(70,80,85)
print("John's Total Mark is :", John_total_mark)
print("John's Percentage score is :", John_percentage)
print("John's average score is :", John_average_score)

Peter_total_mark, Peter_percentage, Peter_average_score  =score(65,90,95)
print("Peter's Total Mark is :", Peter_total_mark)
print("Peter's Percentage score is :", Peter_percentage)
print("Peter's average score is :", Peter_average_score)

Paul_total_mark, Paul_percentage, Paul_average_score  =score(75,70,80)
print("Paul's Total Mark is :", Paul_total_mark)
print("Paul's Percentage score is :", Paul_percentage)
print("Paul's average score is :", Paul_average_score)

Jason_total_mark, Jason_percentage, Jason_average_score  =score(90,85,92)
print("Jason's Total Mark is :", Jason_total_mark)
print("Jason's Percentage score is :", Jason_percentage)
print("Jason's average score is :", Jason_average_score)

Matt_total_mark, Matt_percentage, Matt_average_score  =score(88,87,92)
print("Matt's Total Mark is :", Matt_total_mark)
print("Matt's Percentage score is :", Matt_percentage)
print("Matt's average score is :", Matt_average_score)

