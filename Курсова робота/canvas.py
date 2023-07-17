from tkinter import *


# створення полотна
tk = Tk()
tk.title("МАТЕМАТИЧНИЙ ПОСТРІЛ")
tk.resizable(False, False)  # заборона розгортання вікна по горизонталі і вертикалі
canvas = Canvas(tk, width=500, height=500)
canvas.configure(bg='#000033')
canvas.pack()
tk.protocol("WM_DELETE_WINDOW", tk.quit)

castle_image = PhotoImage(file='D:\\Python\\Курсова робота\\castle.png')
castle_image_weight = 128
castle_image_height = 128
tower_image = PhotoImage(file='D:\\Python\\Курсова робота\\tower.png')
tower_image_weight = 72
tower_image_height = 72
skeleton_image = PhotoImage(file='D:\\Python\\Курсова робота\\skeleton_1.png')
skeleton_image_weight = 72
skeleton_image_height = 72

heart_image = PhotoImage(file='D:\\Python\\Курсова робота\\heart_2.png')
skeleton_head_image = PhotoImage(file='D:\\Python\\Курсова робота\\skeleton_head.png')
cannon_image = PhotoImage(file='D:\\Python\\Курсова робота\\cannon.png')
crossbow_image = PhotoImage(file='D:\\Python\\Курсова робота\\crossbow.png')
sword_image = PhotoImage(file='D:\\Python\\Курсова робота\\sword.png')
