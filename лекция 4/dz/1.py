b = str(input("Введите текст: "))
s = b
a = max(s.split(), key=len)
print("Самое длинное слово: {}".format (a))