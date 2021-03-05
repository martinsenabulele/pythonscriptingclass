def evenNumber(start,end):
    for number in range(start,end):
        if number % 2 == 0:
            print("even number", number)

start=int(input("Enter start range: "))
end=int(input("Enter end range: "))
evenNumber(start,end)

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))


def oddNumber(start,end):
    for number in range(start,end):
        if number % 2 != 0:
            print("odd number", number)


start=int(input("Enter start range: "))
end=int(input("Enter end range: "))
oddNumber(start,end)

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
