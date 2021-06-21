# Write a program to loop through a list of numbers and add +2 to every value to elements in list
C = [20,40,60,10,30,50,70]
print("My List :", C)
C = [x+2 for x in C]
print("After +2 :", C)
print("--------------------------------------------------------------------------------------------------------------")

# Write a program to get the below pattern
# 54321
# 4321
# 321
# 21
# 1
n = int(input("Enter The Number : "))
for i in range(n):
    for j in range(n-i,0,-1):
     print(j,end=" ")
    print()

print("--------------------------------------------------------------------------------------------------------------")
# Python Program to Print the Fibonacci sequence
n = int(input("Enter The Value of 'n' : "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series : ", end= " ")
while(count <= n):
    print(sum, end= " ")
    count += 1
    a = b
    b = sum
    sum = a + b

print("\n--------------------------------------------------------------------------------------------------------------")
# Explain Armstrong number and write a code with a function
# A number is called armstrong number if it is equal to the sum of the cubes of its own digits """
num = int(input("\n Enter a number : "))
sum = 0
temp = num
while temp > 0 :
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "Is An Armstrong Number ")
else:
    print(num, "Is Not An Armstrong Number")

print("--------------------------------------------------------------------------------------------------------------")
# Write a program to print the multiplication table of 9
num = 9
print("Multiplication Table Of 9 : ")
for i in range(1,11):
    print(num, 'x', i, '=', num*i)

print("--------------------------------------------------------------------------------------------------------------")
# Check if a program is negative or positive
n = float(input("Enter The Number : "))
if n > 0:
    print("Positive Number ")
elif num == 0:
    print("Zero")
else:
    print("Negative Number")

print("--------------------------------------------------------------------------------------------------------------")
# Write a program to convert the number of days to ages
days = int(input("Enter The Days : "))
year = days / 365
print("Number Of Years Is : ", year)

print("--------------------------------------------------------------------------------------------------------------")
# Solve Trigonometry problem using math function write a program to solve using math function
import math
x = 0.75
print("Math.cos(",x,"): ", math.cos(x));
print("Math.sin(",x,"): ", math.sin(x));
print("Math.tan(",x,"): ", math.tan(x));
print("Math.acos(",x,"): ", math.acos(x));
print("Math.asin(",x,"): ", math.asin(x));
print("Math.atan(",x,"): ", math.atan(x));
y = 2
print("Math.atan2(",y,",",x,"): ", math.atan2(y,x));
print("Math.hypot(",x,",",y,"): ", math.hypot(x,y));

print("--------------------------------------------------------------------------------------------------------------")
# Create a calculator only on a code level by using if condition (Basic arithmetic calculation)
print("Calculator")
print("1.Add ")
print("2.Sub ")
print("3.Multiply ")
print("4.Divide ")
ch =int(input("Enter Choice (1-4) : "))
if ch == 1:
    a = int(input("Enter A : "))
    b = int(input("Enter B : "))
    c = a + b
    print("Sum : ", c)
elif ch == 2:
    a =int(input("Enter A : "))
    b =int(input("Enter B : "))
    c = a - b
    print("Difference : ", c)
elif ch == 3:
    a = int(input("Enter A : "))
    b = int(input("Enter B : "))
    c = a * b
    print("Product : ", c)
elif ch == 4:
    a = int(input("Enter A : "))
    b = int(input("Enter B : "))
    c = a / b
    print("Quotient : ", c)
else:
    print("Invalid Choice")
print("--------------------------------------------------------------------------------------------------------------")