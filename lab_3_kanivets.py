#Task1

import math

x=1
mu=0
sigma=1
f=1/(sigma*math.sqrt(2*math.pi))*math.exp(-((x - mu) ** 2) / (2 * (sigma ** 2)))
print(f)

#Task2

john=3
mary=5
adam=6
print(f'{john},{mary},{adam}.')
totalapples=john+mary+adam
print(totalapples)
print(f'Загальна кількість яблук:{totalapples}')

#Task3

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#Task4

x = 0
x = float(x)
y = 3*(x**3)-2*(x**2)+(3*x)-1
print("y =", y)

#Task5

# this program computes the number of seconds in a given number of hours

hours = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", hours)
print("Seconds in Hours: ", hours * seconds) # printing the number of seconds in a given number of hours


#Task6

a = 10.5
b = 5.5

print(f'addition: {a+b}\nsubtraction: {a-b}\nmultiplication: {a*b}\ndivision: {a/b}')
print("\nThat's all, folks!")

#Task7

x = float(input("Enter value for x: "))

y=1/(x+(1/(x+(1/(x+(1/(x+(1/x))))))))

print("y =", y)

#Task8

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

min_result= (mins+dura)%60
hour_result=(hour+(mins+dura)//60)%24

print(f'{hour_result}:{min_result}')
