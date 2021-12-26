try:
    chance = 0
    guess_limit = 3
    secreat_value = 10

    while chance <= guess_limit:
        guess = int(input("guess a number: "))  
        chance += 1
        if guess == secreat_value:
            print("You won")
            break
    else:
        print("Game over")
except:
    ValueError
    print('incorrect input');
