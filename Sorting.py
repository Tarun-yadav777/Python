# Programme to sort list through function

item = [("D01", 12), ("D02", 45), ("D05", 1), ("D00", 75)]

#
# def sort_item(item):
#     return item[1]


item.sort(key=lambda item:item[1])
print(item)