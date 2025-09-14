# 25/07/2025
# DATA TYPES IN PYTHON



# Swap using temporary variable
a = 10
b = 20
print("Before Swap:", a, b)

temp = a
a = b
b = temp
print("After Swap using temp:", a, b)

# Swap using tuple unpacking
x, y = 30, 40
print("Before Swap:", x, y)
x, y = y, x
print("After Swap using tuple unpacking:", x, y)


a = input("Enter first value: ")
b = input("Enter second value: ")
c = input("Enter third value: ")

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


salary = float(input("Enter your current salary: "))
hike = salary * 0.15
new_salary = salary + hike

print("Old Salary:", salary)
print("New Salary after 15% hike:", new_salary)


pi = 3.14159
r = float(input("Enter radius of circle: "))

area = pi * r * r
perimeter = 2 * pi * r

print("Area of Circle:", area)
print("Perimeter of Circle:", perimeter)


ch = input("Enter a character: ")
print("ASCII value of", ch, "is", ord(ch))


num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")


x = 10
print("Start:", x)

x += 5
print("After += 5:", x)

x -= 3
print("After -= 3:", x)

x *= 2
print("After *= 2:", x)

x //= 4
print("After //= 4:", x)

x %= 3
print("After %= 3:", x)


age = int(input("Enter age: "))
name = input("Enter name: ")

if age >= 18 and name != "":
    print("Valid user")
else:
    print("Invalid user")


num = 8  # binary: 1000
print("Original:", num)

print("Left shift by 1:", num << 1, "(8 * 2 = 16)")
print("Left shift by 2:", num << 2, "(8 * 2^2 = 32)")

print("Right shift by 1:", num >> 1, "(8 / 2 = 4)")
print("Right shift by 2:", num >> 2, "(8 / 2^2 = 2)")


a = 12  # binary: 1100
b = 5   # binary: 0101

print("a & b =", a & b)   # AND
print("a | b =", a | b)   # OR
print("a ^ b =", a ^ b)   # XOR
print("~a =", ~a)         # NOT


s = "100"
num = int(s)
print(num, type(num))

f = 12.5
str_f = str(f)
print(str_f, type(str_f))

i = 0
bool_i = bool(i)
print(bool_i, type(bool_i))


celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Celsius to Fahrenheit:", fahrenheit)

f = float(input("Enter temperature in Fahrenheit: "))
c = (f - 32) * 5/9
print("Fahrenheit to Celsius:", c)


a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))

print("Quotient:", a // b)
print("Remainder:", a % b)

if a % b == 0:
    print(a, "is divisible by", b)
else:
    print(a, "is not divisible by", b)


text = "Python Programming"

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
print("'Python' in text?", "Python" in text)


num = int(input("Enter a 3-digit number: "))

d1 = num // 100
d2 = (num // 10) % 10
d3 = num % 10

print("Sum of digits:", d1 + d2 + d3)


list1 = [1, 2, 3]
list2 = [1, 2, 3]

print("Equality (==):", list1 == list2)  # True
print("Identity (is):", list1 is list2)  # False


years = int(input("Enter age in years: "))
months = years * 12
days = years * 365

print("Age in months:", months)
print("Age in days:", days)


x = 10 + 3.5
y = "Age: " + str(30)
z = True + False + 2

print("x =", x, "Type:", type(x))
print("y =", y, "Type:", type(y))
print("z =", z, "Type:", type(z))


n = 10  # binary: 1010

print("~n =", ~n, "which is -(n+1) =", -(n+1))
print("n << 1 =", n << 1, "(10 * 2 = 20)")
print("n >> 2 =", n >> 2, "(10 // 2^2 = 2)")
