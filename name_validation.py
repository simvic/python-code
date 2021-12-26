username = input('input your name: ')

if len(username) < 3:
    print('name must be at least three characters long')
elif len(username) > 50:
    print('name can be a maximum of 50 characters long')
else:
    print('name looks good');
