# ðĻ Don't change the code below ð
row1 = ["ðĨ° ","ðĨģ","ð"]
row2 = ["ð","ðĪŠ","ðĪ"]
row3 = ["ð","ð","ðĐ"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# ðĻ Don't change the code above ð

#Write your code below this row ð

Horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[Horizontal - 1] = "ð"



#Write your code above this row ð

# ðĻ Don't change the code below ð
print(f"{row1}\n{row2}\n{row3}")