def add(x, *y):
    for v in y:
        x += v
    return(x)

print(add(1, 4, 3, 10,20))