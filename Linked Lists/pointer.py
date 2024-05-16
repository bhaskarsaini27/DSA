

'''
num1 = 11
num2 = num1

print("Before num2 value is updated:")
print("num1 = ", num1)
print("num2 = ", num2)

print("\nnum1 is pointed to :", id(num1))
print("num2 is pointed to: ", id(num2))

num2 = 22
print("\nAfter num2 value is updated:")
print("num1 = ", num1)
print("num2 = ", num2)
print("\nnum1 is pointed to :", id(num1))
print("num2 is pointed to: ", id(num2))

'''

dict1 = {'value': 11}
dict2 = dict1
print("Before dict2 value is updated:")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("\ndict1 is pointed to :", id(dict1))
print("dict2 is pointed to: ", id(dict2))

dict2['value'] = 22 

print("\nAfter dict2 value is updated:")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("\ndict1 is pointed to :", id(dict1))
print("dict2 is pointed to: ", id(dict2))

dict3 = {'value': 33}
print("\ndict1 is pointed to :", id(dict1))
print("dict2 is pointed to: ", id(dict2))
print("dict3 is pointed to: ", id(dict3))

dict2 = dict3

print("After dict2 = dict3")
print("\ndict1 is pointed to :", id(dict1))
print("dict2 is pointed to: ", id(dict2))
print("dict3 is pointed to: ", id(dict3))

dict1 = dict2
print("Again After dict1 = dict2")
print("\ndict1 is pointed to :", id(dict1))
print("dict2 is pointed to: ", id(dict2))
print("dict3 is pointed to: ", id(dict3))