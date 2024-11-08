immutable_var =( 1, 2, 'a', 'b')
print(immutable_var)
#immutable_var[3] = 15          содержимое кортежа неизменяемый объект(за исключением списка внутри кортежа)
#print(immutable_var)
mutable_list = [1, 2, 'a', 'b', 'Modified']
print(mutable_list)
mutable_list[1] = 35
print(mutable_list)
