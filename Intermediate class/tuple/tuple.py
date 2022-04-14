import sys
import timeit

my_list = [0, 1, 2, 'hello, True']
my_tuple = (0, 1, 2, 'hello, True')

print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))


# with this i will say working with tuple is more effiecient than working with list
