
#Task 1

n = int(input('Enter a number n:'))


numbers_list = [3, 10, 15, 7, 2, 18, 9, 27]
numbers_tuple = tuple(numbers_list)

result = [num for num in numbers_tuple if num < n]


print(result)


#Task 2

t = ('Artem', 'Peter', 'Vicky')

js = ','.join(t)

print(f'Tuple: {js}')


#Task 3

books = {
    'Starship Sakira' : 'Author:Bob Blanton\nYear of publication:2019\nNumber of pages:236',
'The Enceladus Mission' : 'Author: Brandon Q. Morris\nYear of publication:2018\nNumber of pages:448',
'The Gemini Prophecy ' : 'Author: Spencer Quin\nYear of publication:2022\nNumber of pages:156',
'Project Hail Mary':'Author:Andy Weir\nYear of publication:2022\nNumber of pages:496'
}
request = input('Enter the title of the book:')
if request in books:
    print(books[request])
else:
    print('No book found by that title')

#Task 4

students = {
    'Kanivets': ('Artem', 2004, 'AKIT 21-2'),
    'Washington': ('Stephen', 2003, 'KN 20-1'),
    'Gonzalez': ('Travis', 2001, 'AKIT 18-2'),

}

last_name = input("Enter students last name: ")

if last_name in students:
    info = students[last_name]
    print(f"Last name: {last_name}")
    print(f"First name: {info[0]}")
    print(f"Year of birth: {info[1]}")
    print(f"Group: {info[2]}")
else:
    print("Student not found")


#Task 5

def add_phone_number(contact, phone_number):
    if contact in contacts:
        contacts[contact].append(phone_number)
        print(f"{phone_number} added to  {contact}")
    else:
        print(f"{contact} not found")

contacts = {
    'Artem': ['+380254638596', '+380975896542'],
    'Stephen': ['+380985467845'],
    'Travis': ['+9985612478'],
}


add_phone_number('Travis','+380982548561')


for contact, phone_numbers in contacts.items():
    print(f"Phone number for  {contact}:")
    for number in phone_numbers:
        print(number)
    print()



