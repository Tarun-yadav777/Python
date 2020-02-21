# Programme to find the given number is perfect or not
def checkPerfect(y):
    sum = 0
    for i in range(1,y):
        if y % i == 0:
            sum += i
    if sum == y:
        return "Perfect Number"
    return "Not Perfect Number"


x = int(input("Enter the number to find weather its perfect or not-> "))
print(f"Number u entered is {checkPerfect(x)}")
