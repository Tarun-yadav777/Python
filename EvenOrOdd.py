# Programme to find weather the input no is even or odd
number = input("Enter the number u wanna check-> ")
number = int(number)
if number % 2 == 0:
    print(f"Entered number {number} is Even")
else:
    print(f"Entered number {number} is odd")
