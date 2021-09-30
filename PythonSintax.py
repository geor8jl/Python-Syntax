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


num1 = float(input("Enter the first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")


**********Dictionaries************
Valores en parejas con keys atached to them


monthConversions = {
    0: "January",
    1: "February",
    2: "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthConversions.get("Luv", "Not a valid key"))
print(monthConversions[2])



**********While************


i = 1

while i <= 10:
    print(i)
    i += 1
print("Done")


*********Juego de adivinanzas **************




secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You Win")



*************For***************

friends = ["Jim", "Karen", "Kevin"]

for friend in friends:
    print(friend)

for index in range(3, 10):
    print(index)

for index in range(len(friends)):
    print(friends[index])

for letter in "friends":
    print(letter)



*********Exponent Function**************



base_num = int(input("Your Number: "))
pow_num = int(input("Power: "))


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(base_num, pow_num))
print(2**3)


**********Lista 2D o Matriz*******************

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0],
]

print(number_grid[2][2])

for row in number_grid:
    print(row)
    for col in row:
        print(col)


********** Translator *********************


def translate(phrase):
    translation = ""

    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter

    return translation


print(translate(input("Enter your phrase: ")))



























