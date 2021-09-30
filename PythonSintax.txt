print("   /|")
print("  / |")
print(" /  |")
print("/___|")

character_name = "John"
character_age = 50.65555556
is_Male = True

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")

character_name = "Loof"

print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age)

print("Test\"f")
print("Test\nf")
print("Test\f")

phrase = "Giraffe Ac "
code = "Jorge is cool"
print(phrase.replace("Ac" , "Academy"))


***********Numeros****************

my_num = 5

print(str(my_num) + "L")
print(3 * (4 + 5) )
print(10 % 3)

from math import *

my_num = -5

print(str(my_num) + "L")
print(3 * (4 + 5) )
print(10 % 3)
print(abs(my_num))
print(pow(my_num, 80))
print(max(my_num, 80))
print(round(3.5))
print(floor(3.5))
print(ceil(3.3))
print(sqrt(36))


*******INput From User*********

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hi " + name + "!")
print("Age " + age + "!")


********Calculator************

num1 = input("Enter number: ")
num2 = input("Enter another number: ")
operator = input("Enter the operator : ")
result = float(num1) + float(num2)

print(result)


********Mad libs Game**********

color = input("Enter a color : ")
plural_noun = input("Enter a plural noun : ")
celebrity = input("Enter a celebrity : ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)


********Lists***************


friends = ["Kevin" , "Karen" , "Jim" , 4 , True]

friends[1] = "Mike"

print(friends[1])
print(friends[-1])
print(friends[1:])
print(friends[1:3])
friends.clear()

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin" , "Karen" , "Jim" , "Jim" , "Jorge" , "Caro"]
friends.count("Jim")
friends.append("Creed")
friends.insert(2, "Jesus")
friends.remove("Jim")

friends.extend(lucky_numbers)
friends.pop()
print(friends)
print(friends.index(15))

lucky_numbers = [4, 8, 15, 1, 2, 42]
friends = ["Kevin" , "Karen" , "Jim" , "Jim" , "Jorge" , "Caro"]

print(friends.count("Jim"))
lucky_numbers.sort()
friends.sort()

print(friends)
print(lucky_numbers)

lucky_numbers.reverse()
friends.reverse()

print(friends)
print(lucky_numbers)

friends2 = friends.copy()

print(friends2)


**********Tuplas************

Es un tipo de data structure , container es como una lista y se guardan mucha informacion 

Son inmutables = no cambian o se modifican


*******Funciones***********

def say_hi(name, age):
    print("Hello User: " + name + str(age))


say_hi("Jorge ", 32)
say_hi("Caro ", 33)

********return***********



def cube(num1):

    return num1*num1*num1


result = cube(4)
print(result)


***********IF / ELSE **************

is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are not a male and not tall")


def max_num(num1,num2,num3):

    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(355, 4222, 58))



**********Better calculator****************




















