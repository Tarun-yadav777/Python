# Programme to reverse the string
def reverse_myString(MYstring):
    return MYstring[::-1]


my_string = input("Enter the string to reverse-> ")
print(f"Reversed String = {reverse_myString(my_string)}")