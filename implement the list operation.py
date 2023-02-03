
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested List: ", nested_list)

list1 = [1, 2, 3, 4, 5]
print("Length of list1: ", len(list1))


list2 = [6, 7, 8, 9, 10]
list3 = list1 + list2
print("Concatenated List: ", list3)

print(5 in list1)

for element in list1:
    print(element)

print("Index 2: ", list1[2])

print("Sliced list: ", list1[1:3])
