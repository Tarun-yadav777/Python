# programme to find the sum of the list
def sum_list(y):
    sum_of_list = 0
    for i in y:
        sum_of_list += i
    return sum_of_list


x = [8, 2, 3, 0, 7]
print(f"Sum of the given list = {sum_list(x)}")
