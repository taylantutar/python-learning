print("* " * 20)

list = ["ali", "Ayşe", "Kaan", 12, True]
print(list)
# ['ali', 'Ayşe', 'Kaan', 12, True]

list.append("Duru")
print(list)
# ['ali', 'Ayşe', 'Kaan', 12, True, 'Duru']
print(list[0])
# ali
print(list[0:2])
# ['ali', 'Ayşe']

print("* " * 20)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)
# 1, 2, 3, 4, 5, 6]

print(list1 * 3)
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

list1.reverse()
print(list1)
# [3, 2, 1]
