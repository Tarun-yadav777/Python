# Programme to find the max of 3 numbers
def maximum_Of_3(a, b, c):
    if a > b and a > c:
        return a
    elif a < b and b > c:
        return b
    return c


x = int(input("Enter the first number-> "))
y = int(input("Enter the second number-> "))
z = int(input("Enter the third number-> "))
print(f" Maximunm of the three number is = {maxOf3(x, y, z)}")
