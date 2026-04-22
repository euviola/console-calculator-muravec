from calculator import add, subtract
from validator import is_integer

a = 5
b = 3

if is_integer(a) and is_integer(b):
    print(add(a, b))
    print(subtract(a,b))
else:
    print("Exception: Invalid input")
