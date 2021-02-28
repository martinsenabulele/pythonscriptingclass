#Generators
# function-> return output-> another function as input
#return
#f1--> list 1000000 --> f2 > odd and even ----> f3 >> print odd number
#generator
#yield
from datetime import datetime
def print_million():
    output_list =[]
    for i in range(1000000):
        output_list.append(i)
    return output_list


st = datetime.now()
output_list = print_million()
print(output_list)
et = datetime.now()
print(et - st)

def print_million_generator():
    for i in range (100001):
        yield i

output_list = print_million_generator()
for i in output_list:
    print(i)

#st = datetime.now()
#output_list = print_million_generator()
#print(output_list)
#et = datetime.now()
#print(et - st)

#most common used generator in python - range , xrange ( for python 2.7 range is a function and xrange is a generator
#python3  there is no xrange, only range is the generator .

#3 arguments -> ist is start-> inclusive , 2nd one is end point --> exclusive , 3rd --.> steps

for i in range (1, 1000, ):
    print(i)

