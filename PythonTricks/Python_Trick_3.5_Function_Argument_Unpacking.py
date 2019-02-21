# A really cool but slightly arcane feature is the ability to "unpack"
# function arguments from sequences and dictionaries with * and ** operators.

def print_vector(x, y, z):
    print(x, y, z)


tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]
dict_vec = {'x': 0, 'y': 1, 'z': 1}

print_vector(*tuple_vec)
print_vector(*list_vec)
print_vector(**dict_vec)
