
#Task 1

def is_year_leap(year):
    if (year % 4) != 0:
        return False
    elif (year % 100) != 0:
        return True
    elif (year % 400) != 0:
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")


#Task 2

def is_year_leap(year):
    if (year % 4) != 0:
        return False
    elif (year % 100) != 0:
        return True
    elif (year % 400) != 0:
        return False
    else:
        return True

def days_in_month(year, month):

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12 or year < 1:
        return None
    if is_year_leap(year):
        days_in_months[1] = 29
    return days_in_months[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

#Task 3

def is_year_leap(year):

    if (year % 4) != 0:
        return False
    elif (year % 100) != 0:
        return True
    elif (year % 400) != 0:
        return False
    else:
        return True

def days_in_month(year, month):

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12 or year < 1:
        return None
    if is_year_leap(year):
        days_in_months[1] = 29
    return days_in_months[month - 1]

def day_of_year(year, month, day):
    if month < 1 or month > 12 or year < 1 or day < 1:
        return None

    days_in_month_value = days_in_month(year, month)

    if days_in_month_value is None or day > days_in_month_value:
        return None

    # Сума днів попередніх місяців + дні в поточному місяці
    total_days = sum(days_in_month(year, m) for m in range(1, month)) + day
    return total_days


print(f'2000 12 31 :{day_of_year(2000, 12, 31)}')
print(f'2015 6 25 :{day_of_year(2015, 6, 25)}')
print(f'2011 1 45 :{day_of_year(2011, 1, 45)}')
print(f'2007 5 12 :{day_of_year(2007, 5, 12)}')

#Task 4

def is_prime(num):

    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")

#Task 5


def liters_100km_to_miles_gallon(liters):

    miles_per_100km = 100000 / 1609.344
    gallons_per_liter = 1 / 3.785411784
    miles = miles_per_100km / liters
    gallons = miles / gallons_per_liter
    return gallons


def miles_gallon_to_liters_100km(miles):

    kilometers_per_mile = 1.609344
    liters_per_gallon = 3.785411784
    kilometers = miles * kilometers_per_mile
    liters = liters_per_gallon / (kilometers / 100)
    return liters


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


#Task 6

def is_a_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

print(is_a_triangle(1,2,3))
print(is_a_triangle(5,4,6))
print(is_a_triangle(1,4,2))
print(is_a_triangle(15,20,14))

#Task 7

def is_a_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False

    sides = [a, b, c]
    max_side = max(sides)
    sides.remove(max_side)

    return max_side ** 2 == sides[0] ** 2 + sides[1] ** 2

print(is_a_right_triangle(4,5,3))
print(is_a_right_triangle(5,10,6))
print(is_a_right_triangle(1,6,2))
print(is_a_right_triangle(5,12,13))