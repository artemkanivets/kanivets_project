#Task1

n = int(input('Enter a number:'))
print(n >= 100)

#Task2

a = int(input('Enter a number а:'))
b = int(input('Enter a number b:'))
if a > b:
    print(f'{a} is larger then {b}')
else:
    print(f'{b} is larger then {a}')

#Task3

flower = input('Plant:')
if flower == 'spathiphyllum':
    print('No, I want a big Spathiphyllum!')
elif flower == 'pelargonium':
    print('Spathiphyllum! Not pelargonium!')
elif flower == 'Spathiphyllum':
    print('Yes - Spathiphyllum is the best plant ever!')
else:
    print('Wrong input')

#Task4

income = float(input("Enter the annual income: "))
surplus = income - 85528
if income <= 85528:
    tax = income * 0.18 - 556.2
else:
    tax = 14839.2 + (surplus * 0.32)
if tax <= 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

#Task 5

year = int(input('Enter a year:'))
if year < 1582:
    print('Not within the Gregorian calendar period.')
elif (year % 4) != 0:
    print('Common year')
elif (year % 100) != 0:
    print('Leap year')
elif (year % 400) != 0:
    print('Common year')
else:
    print('Leap year')

#Task6

secret_number = 777

print(
"""
+================================+
| Welcome to my game, Muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
guess_number = int(input())
while guess_number != secret_number:
    print("Ha-ha! You're stuck in my loop!")
    guess_number = int(input('Try again:'))
else:
    print("Well done, Muggle. You're free to go.")

#Task 7

import time

for second in range(1,6):
    print(f'{second} Mississippi')
    time.sleep(1)

print('Ready or not, here I come!')

#Task 8

secret_word = 'chupacabra'
while True:
    guess_word=input('Enter a word:')
    if guess_word == secret_word:
        print("You've successfully left the loop.")
        break

#Task 9

user_word = input('Enter a word:').upper()
for letter in user_word:
    if letter in 'AEIOU':
        continue
    else:
        print(letter)

#Task10

word_without_vowels = ""

user_word = input('Enter a word:').upper()


for letter in user_word:
    if letter in 'AEIOU':
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels)

#Task11


blocks = int(input("Enter the number of blocks: "))

height = 0
current_layer_blocks = 1
while blocks >= current_layer_blocks:
    height += 1
    blocks -= current_layer_blocks
    current_layer_blocks += 1

pyramid_height = height
print("The height of the pyramid:", pyramid_height)

#Task12

c0 = int(input('Enter a non-negative and non-zero integer:'))
steps = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
        steps += 1
        print(int(c0))
    elif c0 % 2 == 1:
        c0 = 3 * c0 + 1
        steps += 1
        print(int(c0))
    elif c0 != 1:
        continue
print('Steps:', steps)










