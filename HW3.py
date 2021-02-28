int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a),id(str_b),id(set_c),id(lst_d),id(dict_e))
lst_d.append(4)
lst_d.append(5)
print(lst_d)
print(type(int_a),type(str_b),type(set_c),type(lst_d),type(dict_e))
print(isinstance(int_a, str), isinstance(str_b, str), isinstance(set_c, list), isinstance(lst_d, list), isinstance(dict_e, dict))

print("Anna has {1} apples and {0} peaches.". format(12, 7))
print("Anna has {} apples and {} peaches.". format(12, 7))
print("Anna has {apples} apples and {peaches} peaches.". format(apples=12, peaches=7))
print("Anna has {apples:.5} apples and {peaches:.3} peaches.". format(apples = "twelwe", peaches = "seven"))

a = 5
b = "apples"
c = "peaches"
print(f"Anna has {a} {b} and {a} {c}.")

e = 12
d = 7
print("Anna has %d apples and %d peaches." %(e, d))

dict = {"a": 12, "b": 7}
print("Anna has %(a)d apples and %(b)d peaches." % dict)

lst_comp_1 = [x ** 2 if x % 2 == 1 else x ** 4 for x in range(10)]
print(lst_comp_1)

lst_1 = []
for i in range(10):
     if i % 2 == 0:
      lst_1.append(i // 2)
     else:
       lst_1.append(i * 10)
print(lst_1)

dict_2 = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dict_2)

dict_3 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_3)

dict_1 = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        dict_1[num] = num ** 3
print(dict_1)

dict_4 = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        dict_4[num] = (num ** 3)
    else:
        dict_4[num] = (num)
print(dict_4)

foo = lambda x, y: x if x < y else y
print(foo(5, 7))

def foo_1(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo_1 (5, 6, 7))

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
print(sorted(lst_to_sort, reverse=True))
new_list = list(map(lambda x: x * 2, lst_to_sort))
print(new_list)

list_A = [2, 3, 4]
list_B = [5, 6, 7]
new_list_1 = list(map(lambda x: x + 3, list_A))
print(new_list_1)

from functools import reduce
sum_lst = reduce(lambda A, B: A + B, lst_to_sort)
print(sum_lst)

lst_to_sortB = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(lst_to_sortB)

b = range(-10, 10)
b_1 = list(filter(lambda x : x<0, b))
print(b_1)

list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
print(list(filter(lambda x: x in list_1, list_2)))
