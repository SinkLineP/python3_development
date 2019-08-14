from tkinter import *
 
# Создаем окно
root = Tk()
# Устанавливаем название окна
root.title("PythonicWay Snake")
# ширина экрана
WIDTH = 800
# высота экрана
HEIGHT = 600
# Размер сегмента змейки
SEG_SIZE = 20
# Переменная отвечающая за состояние игры
IN_GAME = True

# создаем экземпляр класса Canvas (его мы еще будем использовать) и заливаем все зеленым цветом
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#003300")
c.grid()
# Наводим фокус на Canvas, чтобы мы могли ловить нажатия клавиш
c.focus_set()
 
# Запускаем окно
root.mainloop()