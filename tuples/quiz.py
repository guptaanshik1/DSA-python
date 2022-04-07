# 1.

init_tuple = ()
print(init_tuple.__len__())

# 2.

ini_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')
print(ini_tuple_a == init_tuple_b)

# 3.

init_tuple_c = '1', '2'
init_tuple_d = ('3', '4')
print(init_tuple_c + init_tuple_d)

# 4.

init_tuple_e = 1, 2
init_tuple_f = (3, 4)
[print(sum(x)) for x in [init_tuple_e + init_tuple_f]]

# 5.

init_tuple_g = [(0, 1), (1, 2), (2, 3)]
result = sum(n for _, n in init_tuple_g)
print(result)