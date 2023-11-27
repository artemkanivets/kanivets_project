#Example 1

def ispalindrom(text):
    text = text.replace(" ", "").lower()
    if text == text[::-1]:
        print("It's a palindrom")
    else:
        print("It's not a palindrom")

text = input("Введіть текст:")
ispalindrom(text)

text = input("Введіть текст:")
ispalindrom(text)


# #Example 2

# Пеервірка на анаграму

text1 = input("Введіть перше слово:")
text2 = input("Введіть друге слово:")

text1 = list(text1.replace(" ", "").lower())
text2 = list(text2.replace(" ", "").lower())

if sorted(text1) == sorted(text2):
    print("Анаграми")
else:
    print("Не анаграми")

# #Example 3

# ПЕРШИЙ варіант

#Обчислює число "життя": суму цифр повної дати народження
date = input("Введіть дату народження у форматі YYYYMMDD:")

while True:
    sum = 0
    for simbol in date:
        sum += int(simbol)

    date = str(sum)

    if len(date) == 1:
        break

print(sum)

# ДРУГИЙ варіант

def calculate_life_number(date):
    # видалення всіх символів, окрім цифрр
    digits = ''.join(filter(str.isdigit, date))

    # вычисление суммы цифр
    digit_sum = sum(int(d) for d in digits)

    # повторне додавання, якщо результат містить більше однієї цифри
    while digit_sum > 9:
        digit_sum = sum(int(d) for d in str(digit_sum))

    return digit_sum


# Запит дати народження користувача
date = input("Введіть дату народження у форматі РРРРММДД, РРРРДДММ или ММДДРРРР: ")

# Обчислення цифри життя та виведення результату
life_number = calculate_life_number(date)
print("Цифра життя для дати {}: {}".format(date, life_number))

#Task 1

def are_letters_in(word, string):
    word_index = 0

    for char in string:
        if char == word[word_index]:
            word_index += 1
            if word_index == len(word):
                return True

    return False


word_input = "dog"
string_input_1 = "vcxzxduybfdsobywuefgas"
string_input_2 = "vcxzxdcybfdstbywuefsas"

result_1 = are_letters_in(word_input, string_input_1)
result_2 = are_letters_in(word_input, string_input_2)


print(f"Is {word_input} in {string_input_1}", "Yes" if result_1 else "No")
print(f"Is {word_input} in {string_input_2}", "Yes" if result_2 else "No")

#Example 4


while True:
    try:
        number = int(input(" Введіть ціле число: "))
        print(number/2)
        break
    except:
        print("Введене значення не є допустимим числом. Повторіть спробу...")

#Task 2



while True:
    try:
        date = input("Введіть дату народження у форматі YYYYMMDD:")

        while True:
            sum = 0
            for symbol in date:
                sum += int(symbol)

            date = str(sum)

            if len(date) == 1:
                break

        print(sum)

        break
    except ValueError:
        print("Введене значення не є допустимим. Повторіть спробу...")

#Task 3



def check_range(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value or value > max_value:
                raise ValueError(f"Error: the value is not within permitted range ({min_value}..{max_value})")
            return value
        except ValueError:
            print("Error: wrong input. Please enter an integer value.")


min_limit = 10
max_limit = 50
user_input = check_range(f"Enter a number between {min_limit} and {max_limit}: ", min_limit, max_limit)
print("Valid input:", user_input)











