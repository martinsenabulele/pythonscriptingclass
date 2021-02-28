#Dictionary has two type of date key, laue
# we fetch date using key
#key should be always immutable data type

# dict1 = {"key" "value"}
dict1 = {
    "a": 1,
    "b":2,
    "c": 3
}
#print(dict1['c'])

dict1.update({
    "d":4,
    "e": 5,
})

#print(dict1)

dict2 = {
    1: "apple",
    2:  "orange",
    3: "pear",
    4: "banana",
    5: "plum",
    6: "strawberries",
    7:  "watermelon",
    8: "Blackberries",
    9: "lemon",
    10: "Grapefruit",

}

print(dict2[1])
print(dict2[5])
print(dict2[6])

dict2.update({
    9:"Lilies",
    10: "Gerbera_Daisie",
})
print(dict2)

