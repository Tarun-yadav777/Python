# Programme to calculate the factorial of input number
factorial = 1
x = int(input("Enter the number of which u wanna find factorial-> "))
y = x
while x >= 1:
    factorial = factorial * x
    x = x - 1
print(f"Factorial of the {y} is = {factorial}")
