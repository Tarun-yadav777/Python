# Programme to check weather entered number is prime or not
number = input("Enter the number u wanna check-> ")
number = int(number)
is_Prime = True
for x in range(2, number):
    if number % x == 0:
        is_Prime = False
        break

if is_Prime:
    print(f"{number} is Prime")
else:
    print(f"{number} is not Prime")
