from random import randint
from random import shuffle

print("* " * 20)

i1 = randint(0, 100)
print(i1)

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(list1)
print(list1)

print("* " * 20)

l1 = ["a", "b", "c"]
l2 = [100, 200, 300]
l3 = ["Arda", "Alex", "Hakan"]

newList = list(zip(l1, l2, l3))
print(newList)
for item in newList:
    print(item)

print("* " * 20)

for k, v in enumerate(range(5, 25, 5)):
    print(f"Key: {k} Value: {v}")

print("* " * 20)

name = "Düzgün Tutar"
asciCodesOfNameChars = [ord(item) for item in name]
print(asciCodesOfNameChars)
