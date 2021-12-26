import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# ========================================================================
# Option 1
# ========================================================================

# count = len(names)

# rand_choice = (random.randint(0, count - 1))
# person_who_will_pay = names[rand_choice]

# print(f"the person who is to pay for this bill is {person_who_will_pay}")

# =========================================================================
# Option 2
# =========================================================================

next_choice = random.choice(names)
print(next_choice + 'is going to pay for the bill thank you')