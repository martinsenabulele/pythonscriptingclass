#Conditional Statement
#IF, else,elif
#if --it is used for decision making
#if expression
#   statement
#else
#   statement
#odd  - number which is not divisible by 2
#even - number which is divisible by 2

#num=4
#if num % 2 == 0:
 #   print("{0} is even number".format(num))
#else:
  #  print("{0} is odd number".format(num))

# write a function which will take input as a given number and check if the number is odd or even
def evenOddFunction(num):
    if num %2 ==0:
        return 'Even Number'
    else:
        return 'Odd Number'

evenOddFunction(4)

evenOddFunction(5)

evenOddFunction(6)

def greaterLessFunction(num1, num2):
    if num1 > num2:
        return 'Greater'
    else:
        return 'Less'

def gradeChecker(score):
    if score >=90:
        return 'Grade A'
    if score >=80:
        return 'Grade B'
    if score >=70:
        return 'Grade C'
    if score >=60:
        return 'Grade D'
    if score >=40:
        return 'Grade E'
    else:
        return 'Fail'
#gradeChecker(int(input("Enter your score: ")))

gradeChecker(80)


