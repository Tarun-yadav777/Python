# programme to return new list with removal of duplicate elements
def new_list(y):
    z = []
    for i in y:
        if i not in z:
            z.append(i)
    return z


x = [1, 2, 3, 3, 3, 3, 4, 5]
print(f"Previous List = {x} \n New List = {new_list(x)}")
