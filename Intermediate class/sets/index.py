# sets are mutable datatype and does not accepts duplicate
mySet = {1, 2, 4, 5, 3, 5, 6}
# print(mySet)

mySet1 = set()

mySet1.add(1)
mySet1.add(2)
mySet1.add(3)
mySet1.add(4)
mySet1.add(5)

mySet1.discard(5)
# print(mySet1)

mySet2 = set()
value = len(mySet2)
print(value)

if len(mySet2) == 0:
    mySet2.add(1)
    print(mySet2)
