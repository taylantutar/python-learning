class Human:
    def __init__(self,name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)

human_1= Human("Mert")

human_1.add_friend("Kaan")
print(human_1.name)
print(human_1.friends)

print()

human_1.add_friend("Ayse")
print(human_1.friends)

print()

human_2 = Human("Nazan")
print(human_2.name)
print(human_2.friends)


