string_1 = "Hey, I am string."
num_1 = 123
my_array = [1, 2, 3, 4, 5, 6, 7]
my_dictionary = {"Jordan": "31", "Chase": "26", "Tiffany": "25"}
print(type(num_1))

if type(string_1) == str:
    print(string_1)

if type(num_1) == int:
    print(num_1)

if type(my_array) == list:
    for i in my_array:
        print(i)

if type(my_dictionary) == dict:
    for key, value in my_dictionary.items():
        print(key+":"+value)

print('----PRINT ID.---- \n')
print(id(my_array))
print('----What would happen if we do not use introspection.---- \n')
my_dictionary1 = [1, 2, 3, 4, 5, 6, 7]
my_array1 = {"Jordan": "31", "Chase": "26", "Tiffany": "25"}

for key, value in my_dictionary1.items():
    print(key+":"+value)

for i in my_array1:
    print(i)
