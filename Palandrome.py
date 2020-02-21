# Programme to check weather the input string is palindrome or not
def checkPalindrome(input_String):
    reversed_string = input_String[::-1]
    return reversed_string == input_String


string = input("Enter the string to check->")
print(f"String is palindrome = {checkPalindrome(string)}")
