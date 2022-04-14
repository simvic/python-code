# a turple is created by parentesis and they are immutable which means they can't be change

fruit = ('banna', 'mango', 'cherry', 'lemon')
x = len(fruit)
print(x)
print(fruit.index('banna'))

new_list = list(fruit)
print(new_list)

new_tuple = tuple(new_list)

print(new_tuple)

# slicing with tuple
a = (1, 2, 4, 563, 3, 2, 1, 3, 5, 3)

b = a[::-1]
print(b)
c = sorted(a)
print(c)
