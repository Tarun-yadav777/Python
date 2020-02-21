# To Print even numbers from 1 to 10 and count the nos
c = 0
for x in range(1, 10):
    if x % 2 == 0:
        print(x)
        c += 1
print(f"The no of even numbers is {c}")
