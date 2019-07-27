import datetime

print("Введите Год: ")
year = int (input())
print("Введите Месяц: ")
month = int (input())
print("Введите день: ")
day = int (input())


today = datetime.date.today()
future = datetime.date(year,month,day)
diff = future - today
print ("Прошло-{}-дней.".format(diff.days))