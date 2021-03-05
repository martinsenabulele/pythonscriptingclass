def halfPyramid():
    for i in range(5):
        for j in range(i + 1):
            print(end="* ")
        print()


def invertedHalfPyramid():
    for i in range(5):
        for j in range(i, 4):
            print(end="* ")
        print()


halfPyramid()
invertedHalfPyramid()