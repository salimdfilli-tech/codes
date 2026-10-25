from re import A


my_list = [1, 2, 3, 4, 5]
my_turple = (10, 20, 30, 40, 50)
my_dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(my_list)
print(my_turple)
print(my_dictionary)

my_dictionary = {"name": "wisdom", "age": 18}
my_dictionary["course"] =" python"
print(my_dictionary)

my_list = [10, 20, 30, 40, 50]
print(my_list[0])
print(my_list[-1])


text = "hello"
print(text.isdigit())
print(text.isalnum())
print(text.istitle())
new_text = text.replace("hello", "hi")
print(new_text)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {**dict1, **dict2}

print(merged)

my_turple = (1, 2, 3, 4, 4, 5, 6, 4)
count = my_turple.count(4)
print("occurence of 4:", count)

my_dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}

keys = list(my_dictionary.keys())

del my_dictionary[keys[0]]
del my_dictionary[keys[-1]]

print(my_dictionary)


for i in range(1, 11):
    if i%2 == 0:
        print(i)

for i in range(1,21):
    if i == 6:
        print("six")
    elif i == 10:
        print("ten")
    else: 
        print(i)
        
        letter = A
        letter = B
        letter = input("A").lower()
        if letter in "aeiou":
            print(f"'{A}'is a vowel")
        else: 





    




