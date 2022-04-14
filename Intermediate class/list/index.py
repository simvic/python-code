from __future__ import print_function


fruitList = ['banna', 'cherry', 'orange', 'apple', 'cherry']
numbers = [2, 3, 4, 5, -3, 0, -1, -8]
print(len(fruitList))

fruitList.insert(2, 'star fruit')

clean = fruitList.clear()
num_list = sorted(numbers)
print(num_list)

# list slising

testCase = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(testCase[::-2])
