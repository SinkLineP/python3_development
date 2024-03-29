# ввод строки
s = input('Введите слово: ')

# длинна строки
l = len(s)

# длина половины строки
# ( Находится делением нацело на 2. 
# Если количество символов нечетно, 
# то стоящий в середине не учитывается, 
# т.к его сравниваемая пара - он сам. )
l = l//2

# количество итераций цикла равно длине половины строки
for i in range(l):
    # Если символ с индексом i не равен "симметричному" 
    # символу с конца строки (который находится путем
    # индексации с конца),
    if s[i] != s[-1-i]:
        # то выводится сообщение, что строка не палиндром
        print("Не является полиндромом")
        # выход из программы
        quit()

# До этого места кода программа дойдет, если не произойдет 
# выход из программы в цикле выше.
# Если выхода не произошло, значит строка - палиндром.
print("Является полиндромом")