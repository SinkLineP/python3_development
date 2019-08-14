a = input("Введите текст: ")
line = a.split()
z = [x[::-1] for x in line]
print("------------------------")
print(*z)