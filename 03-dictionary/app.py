print("* " * 20)

dict = {"name": "Düzgün", "age": 32}
print(dict)
# {'name': 'Düzgün', 'age': 32}

print(dict["name"])
# Düzgün

print(dict.keys())
# dict_keys(['name', 'age'])

print(dict.values())
# dict_values(['Düzgün', 32])

dict.pop("name")
print(dict)

dict.clear()
print(dict)
# {}