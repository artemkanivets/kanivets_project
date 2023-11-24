hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
print(f'List:{hat_list}')

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.


hat_list[2] = int(input('Enter a number:'))

# Step 2: write a line of code that removes the last element from the list.

hat_list.pop()

# Step 3: write a line of code that prints the length of the existing list.

print(f'Length of list:{len(hat_list)}')

print(hat_list)


# 1 реалізувати інтерактивне введення елементів масива
arr = []
n = int(input("Enter length of a list: "))
for i in range(0, n):
    element = int(input("arr[" + str(i + 1) + "] = "))
    arr.append(element)
# 2 оптимізувати процедуру сортування

length = len(arr)
for i in range(0, length):
    for j in range(0, length - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print(f'Sorted list:{arr}')


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_numbers = []
for num in my_list:

    if num not in unique_numbers:
        unique_numbers.append(num)
    else:
        continue

print("The list with unique elements only:")
print(unique_numbers)

board = [['_'] * 8 for _ in range(8)]


board[0][0] = '♜'
board[0][7] = '♜'
board[7][0] = '♜'
board[7][7] = '♜'

for row in board:
    print(' '.join(row))
