def print_params(msg, *numbers, **pairs):
    print("msg",msg)
    print("numbers",numbers)
    print("pairs",pairs)


print("----------------1--------------")
print_params("hello")


print("----------------2--------------")
print_params("hello",1,2,3,4,"TEST")


print("----------------3--------------")
print_params("hello",name="bob",age=13)


print("----------------4--------------")
print_params("hello",1,2,3,4,"TEST",name="bob",age=13)


"""
OUTPUT:
_______________

----------------1--------------
msg hello
numbers ()
pairs {}
----------------2--------------
msg hello
numbers (1, 2, 3, 4, 'TEST')
pairs {}
----------------3--------------
msg hello
numbers ()
pairs {'name': 'bob', 'age': 13}
----------------4--------------
msg hello
numbers (1, 2, 3, 4, 'TEST')
pairs {'name': 'bob', 'age': 13}
"""
