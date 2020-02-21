# Programme for finding fibonacci series
number = int(input("Enter the number for fibonacci series-> "))
term_1 = 0
term_2 = 1
print(f"Fibonacci series of the input term is: ")
for i in range(number):
    term_3 = term_1 + term_2
    print(term_1, end=" ")
    term_1 = term_2
    term_2 = term_3
