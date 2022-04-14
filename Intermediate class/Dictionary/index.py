my_dict = {"name": "belema", "age": 31, "city": "port harcourt"}
# print(my_dict)


my_dict2 = dict(name="ibiso", age=27, city="port harcourt")
# print(my_dict2)

my_dict["email"] = "mail.belema@gmail.com"
# print(my_dict)


# common way to delete in dictionaries
del my_dict["name"]
# print(my_dict)

my_dict2.pop("age")
# print(my_dict2)

my_dict.popitem()
# print(my_dict)

length1 = len(my_dict)
# print(length1)


# how to update a dictionary
dict1 = {"name": "ibiso", "age": 27, "email": "mail@xyz.com"}
dict2 = dict(name="green", age=27, city="port harcourt")

dict1.update(dict2)
print(dict1)
