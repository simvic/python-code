
for buzz in range(1, 101):
    if buzz % 3 == 0 and buzz % 5 == 0:
        print('FizzBuzz')

    elif buzz % 5 == 0:
        print('Buzz')

    elif buzz % 3 == 0:
        print('Fizz')
    else:
        print(buzz)
