num = int(input("Input a four digit: "))
x = num // 1000

x1 = (num - x * 1000) // 100
.
x2 = (num - x * 1000 - x1 * 100) // 10

x3 = num - x * 1000 - x1 * 100 - x2 * 10

print("The sum of digits  is", x + x1 + x2 + x3)