# Programme to give a third list from adding odd and even elements from first and second list
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = []
List = [34, 54, 67, 89, 11, 43, 94]
sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
for x in range(1, len(listOne)+1):
    if x % 2 == 0:
        listThree.append(listOne[x-1])
for x in range(1, len(listTwo)+1):
    if x % 2 == 1:
        listThree.append(listTwo[x-1])
print(f"This is output of first question = {listThree}")

print(List)
List.remove(11)
print(f"This is list after removing 4 th  index = {List}")
List.insert(2, 11)
print(f"This is list after inserting 2 th  index = {List}")
List.append(11)
print(f"This is list after inserting at end = {List}")

sampleList1 = sampleList[:3]
print(f"Chunk1 = {sampleList1} and reverse = {sampleList1[::-1]}")
sampleList2 = sampleList[3:6]
print(f"Chunk1 = {sampleList2} and reverse = {sampleList2[::-1]}")
sampleList3 = sampleList[6:]
print(f"Chunk1 = {sampleList3} and reverse = {sampleList3[::-1]}")