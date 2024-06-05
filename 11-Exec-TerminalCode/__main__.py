import subprocess

print("*" * 15)

path = input("Please give me path of folder you want to learn:")
print(path)

result = subprocess.call(["ls", "-a", path])

print("Folders:")
print(result)
