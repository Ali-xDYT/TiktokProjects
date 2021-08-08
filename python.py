side1 = input("Enter 1st side length: ")
side2 = input("Enter 2nd side length: ")
side3 = input("Enter 3rd side length: ")

a = float(side1) ** 2
b = float(side2) ** 2
c = float(side3) ** 2

if c == a + b:
    type = "a right "
if c < a + b:
    type = "an acute triangle"
if c > a + b:
    type = "an obtuse triangle"

print("Triangle is " + type)


