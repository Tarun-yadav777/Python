# Programme to count the number of upper case and lower case


def countUC(myString):
    count = 0
    for i in myString:
        if i.isupper():
            count += 1
    return count


def countLC(myString):
    count = 0
    for i in myString:
        if i.islower():
            count += 1
    return count


string = input("Enter the string u want to check-> ")
print(f"Number of upper case = {countUC(string)} and Number of lower case = {countLC(string)}")
