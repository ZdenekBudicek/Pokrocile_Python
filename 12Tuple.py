# Tuple
# Chová se stejně jak list, jen nejdou měnit hodnoty.

my_tuple = (1, 5, 8)

print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

# nejde
# my_tuple[0] = 12

# Tuple změníme na list
tuple_to_list = list(my_tuple)
print(tuple_to_list)
tuple_to_list[1] = 12
print(tuple_to_list)
