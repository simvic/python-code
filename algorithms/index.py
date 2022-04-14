import sys

# write a function that will take n number and return the sum from n to 1


def sum1(n):
    final_sum = 0
    for n in range(n+1):
        final_sum += n

    return final_sum


# print(sum1(1000))
# print(sys.getsizeof(sum1(1000)))


def sum2(n):
    return(n*(n+1))/2


# print(sum2(1000))
# print(sys.getsizeof(sum2(1000)))

# BigO examples

# O(1) constant


def func_constant(values):
    '''
    print first item in a list 
    '''
    print(values[0])


# func_constant([1, 4, 6, 7, 4, 1])


def func_linear(lst):
    """
    Takes a list and prints out all its value
    """
    for val in lst:
        print(val)


# func_linear([3, 5, 6, 7, 4, 2, 4, 5])

def func_quad(lst_q):
    """
    prints pairs for every item in a list
    """
    for x in lst_q:
        for y in lst_q:
            print(x, y)


# lst_q = [2, 3, 5]
# func_quad(lst_q)

def comp(lst):
    """
    This function prints the first item in a list O(1) it is a constant
    Then it prints the first 1/2 of the list O(n/2)
    Then it print a string 10 times O(10) it is a constant
    """
    print(lst[0])
    midpoint = len(lst)//2

    for val in lst[:midpoint]:
        print(val)

    for x in range(10):
        print('number')


figure = [2, 1, 3, 4, 5, 1, 3, 5]
comp(figure)
