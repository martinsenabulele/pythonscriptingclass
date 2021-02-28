#varaible store one data at a point in time .
#data structures are some structure which store data so that we can manipulate it later .
#data type:
#mutable and immutable
#mutable can be modify while -- type is list, set, Dictionary
#immutable are not modifiable --type is tuple, String, Variable, Integer, Float, boolean

list1 = ['martins', 'martins', 'felicia','martins', 'martins', 'Sagie']
#print(type(list1))
#print(dir(list1))

#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
#list2 =[35,34,36]
#list1.append(list2)
print("append list1  is :", list1)
#list1.extend(list2)
print("extend list1 is :",list1)
list3 = list1.copy()
print("copy list1 to list3 is :",list3)

#append mean adding the list two as one to list one
#extend mean adding both list one and two individually
print(list1.count("martins"))

#index give the data position
print(list1.index("felicia"))
#insert will add a data to the list and you have to give position
list1.insert(3, 'jason')
print(list1)
#pop remove last item
list1.pop()
print(list1)

list1.sort()
print(list1)

#assignment create a the following lists and apply the various method
#list1 ,list2 = strings, list3, list4 =integer , list5 and list6 = float`