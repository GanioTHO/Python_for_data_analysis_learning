# https://realpython.com/ref/builtin-types/int/

# integer is a whole number
# (no decimal places)
# they are good for calculation to avoid
# float rounding errors

number = 1

print(number)
# 1

print(type(number))
# <class 'int'>

# you can sepcify the base of numeric system
print(int("10001110", 2))
# 142
print(int("543546",12))
# 1333062