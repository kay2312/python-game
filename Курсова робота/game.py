import datetime
import ctypes
from data_file import *
from canvas import *
from weapon import Weapon

lib = ctypes.CDLL('./game_2.dll')


class Design(Weapon):
    def __init__(self, score, level, heart):
        super().__init__(enemy, arsenal)
        self.score = score
        self.level = level
        self.heart = heart

    button_input = None
    entry = None

    def weapon(self, numb):  # зменшення кількості ворогів
        global check
        window.clear_all()
        if numb == 1:
            self.enemy = super().sword(self.enemy)
        elif numb == 5:
            self.enemy = super().crossbow(self.enemy)
        elif numb == 10:
            self.enemy = super().catapult(self.enemy)
        elif numb == 50:
            self.enemy = super().gun(self.enemy)

        self.arsenal = super().arsenal(self.arsenal)

        check = super().control(self.enemy, self.arsenal)

        if check == 2:
            window.level_game(self.enemy, self.arsenal)
        elif check == 1:
            window.passed_level(check)
        elif check == 0:
            window.passed_level(check)

    @staticmethod
    def file_reading():  # зчитування даних про гравців
        global btn_menu
        window.clear_all()
        data.file_reading()
        window.design_castle_part()
        btn_menu = Button(canvas, text="Меню", font=('Times New Roman', 13), command=Design.clear_rules, bg='#000033',
                          fg='#00FF00')
        btn_menu.configure(width=12, height=2, highlightcolor='#FF0000')
        btn_menu.place(relx=0.18, rely=0.9, anchor=CENTER)

    def file_filling(self):  # заповнення у файл даних про гравця
        data.file_filling(name, self.level, self.score, minutes, seconds)

    @staticmethod
    def enter_name():  # введення імені гравця
        global entry

        window.clear_all()

        if Design.entry:
            Design.entry.destroy()  # видалення попереднього Entry, якщо воно існує

        Design.entry = Entry(tk, bg='#00FF00', fg='black', width=30)
        Design.entry.place(x=160, y=190)
        Design.button_input = Button(tk, text="Ввести", font=('Times New Roman', 15), command=Design.button_name,
                                     bg='#000033',
                                     fg='#00FF00')
        Design.button_input.configure(width=15, height=2, highlightcolor='#FF0000')
        Design.button_input.place(relx=0.5, rely=0.603, anchor=CENTER)
        canvas.create_text(250, 70, text="Введіть ім'я:", font=('Courier', 26), fill='#00FF00')
        canvas.create_text(249, 69, text="Введіть ім'я:", font=('Courier', 26), fill='#00FF00')
        window.design_castle()

    def button_level(self):  # створення пробного рівня
        global control

        value = int(Design.entry.get()) - 1

        if value >= 0 and value <= 9:
            self.level = value
            control = 1
            window.new_level()

    @staticmethod
    def button_name():  # введення імені гравця
        global name

        name = Design.entry.get()

        window.new_level()

    @staticmethod
    def trial_level():  # введення пробного рівня
        global entry

        Design.clear_all()
        if Design.entry:
            Design.entry.destroy()  # видаляємо попереднє Entry, якщо воно існує

        Design.entry = Entry(tk, bg='#00FF00', fg='black', width=30)
        Design.entry.place(x=160, y=190)
        Design.button_input = Button(tk, text="Ввести", font=('Times New Roman', 15),
                                     command=lambda: window.button_level(),
                                     bg='#000033',
                                     fg='#00FF00')
        Design.button_input.configure(width=15, height=2, highlightcolor='#FF0000')
        Design.button_input.place(relx=0.5, rely=0.603, anchor=CENTER)
        canvas.create_text(250, 70, text="Введіть рівень:", font=('Courier', 26), fill='#00FF00')
        canvas.create_text(249, 69, text="Введіть рівень:", font=('Courier', 26), fill='#00FF00')
        window.design_castle()

    @staticmethod
    def clear_all():  # стирання всіх кнопок, картинок
        if Design.button_input:
            Design.button_input.destroy()

        if Design.entry:
            Design.entry.destroy()

        btn_exit.destroy()
        btn_menu.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        btn_5.destroy()
        btn_arsenal_1.destroy()
        btn_arsenal_2.destroy()
        btn_arsenal_3.destroy()
        btn_arsenal_4.destroy()
        btn_next_level.destroy()

        canvas.delete("all")

    def new_level(self):  # формування даних для нового рівня
        global start_time
        self.level = self.level + 1
        self.arsenal = lib.RandomArsenal(self.level)
        self.enemy = lib.RandomEnemy(self.level, self.arsenal)
        start_time = datetime.datetime.now()
        window.level_game(self.enemy, self.arsenal)

    @staticmethod
    def menu():
        global btn_menu, btn_next_level, btn_1, btn_2, btn_3, btn_4, \
            btn_5, btn_arsenal_1, btn_arsenal_2, btn_arsenal_3, btn_arsenal_4

        window.clear_all()

        window.design_castle()

        image_skeleton = canvas.create_image(10, 15, anchor=NW, image=skeleton_image)
        image_skeleton = canvas.create_image(410, 15, anchor=NW, image=skeleton_image)

        canvas.create_text(250, 70, text="Математичний", font=('Courier', 26), fill='#00FF00')
        canvas.create_text(249, 69, text="Математичний", font=('Courier', 26), fill='#00FF00')
        canvas.create_text(250, 110, text="постріл", font=('Courier', 26), fill='#00FF00')
        canvas.create_text(249, 109, text="постріл", font=('Courier', 26), fill='#00FF00')

        btn_1 = Button(canvas, text="Нова гра", font=('Times New Roman', 13),
                       command=Design.enter_name,
                       bg='#000033',
                       fg='#00FF00')
        btn_2 = Button(canvas, text="Спробувати", font=('Times New Roman', 13), command=Design.trial_level,
                       bg='#000033',
                       fg='#00FF00')
        btn_3 = Button(canvas, text="Правила", font=('Times New Roman', 13), command=lambda: window.text_rules(), bg='#000033',
                       fg='#00FF00')
        btn_4 = Button(canvas, text="Рейтинг", font=('Times New Roman', 13), command=lambda: window.file_reading(), bg='#000033',
                       fg='#00FF00')
        btn_5 = Button(canvas, text="Вийти", font=('Times New Roman', 13), command=Design.stop_program, bg='#000033',
                       fg='#00FF00')

        btn_1.configure(width=12, height=2, highlightcolor='#FF0000')  # Налаштування розміру кнопки
        btn_1.place(relx=0.38, rely=0.4, anchor=CENTER)  # Розміщення кнопки посередині канви
        btn_2.configure(width=12, height=2, highlightcolor='#FF0000')
        btn_2.place(relx=0.615, rely=0.4, anchor=CENTER)
        btn_3.configure(width=12, height=2, highlightcolor='#FF0000')
        btn_3.place(relx=0.38, rely=0.5, anchor=CENTER)
        btn_4.configure(width=12, height=2, highlightcolor='#FF0000')
        btn_4.place(relx=0.615, rely=0.5, anchor=CENTER)
        btn_5.configure(width=12, height=2, highlightcolor='#FF0000')
        btn_5.place(relx=0.5, rely=0.603, anchor=CENTER)

    @staticmethod
    def stop_program():  # зупинити програму
        tk.quit()

    @staticmethod
    def clear_rules():  # стирання сторінки з правилами і перехід до меню
        window.clear_all()

        window.menu()

    def text_rules(self):  # завантаження правил з файлу
        global btn_menu

        window.clear_all()

        data.text_rules()

        Design.design_castle_part()

        btn_menu = Button(canvas, text="Меню", font=('Times New Roman', 13), command=Design.clear_rules, bg='#000033',
                          fg='#00FF00')
        btn_menu.configure(width=12, height=2, highlightcolor='#FF0000')  # налаштування розміру кнопки
        btn_menu.place(relx=0.18, rely=0.9, anchor=CENTER)  # розміщення кнопки посередині полотна

    def level_game(self, enemy, arsenal):  # формування рівню
        global btn_arsenal_1, btn_arsenal_2, btn_arsenal_3, btn_arsenal_4

        window.clear_all()

        canvas.create_text(85, 25, text=f"Рівень:{self.level}", font=('Courier', 15), fill='#98FF98')
        canvas.create_text(84, 24, text=f"Рівень:{self.level}", font=('Courier', 15), fill='#00FF00')

        canvas.create_text(420, 25, text=f"Бали:{self.score}", font=('Courier', 15), fill='#98FF98')
        canvas.create_text(419, 24, text=f"Бали:{self.score}", font=('Courier', 15), fill='#00FF00')

        canvas.create_line(0, 45, 500, 45, fill='#98FF98')

        canvas.create_text(85, 79, text=f"Зброя:{self.arsenal}", font=('Courier', 20), fill='#00FF00')
        canvas.create_text(84, 78, text=f"Зброя:{self.arsenal}", font=('Courier', 20), fill='#00FF00')

        heart_3 = canvas.create_image(450, 59, anchor=NW, image=heart_image)
        heart_2 = canvas.create_image(410, 59, anchor=NW, image=heart_image)
        heart_1 = canvas.create_image(370, 59, anchor=NW, image=heart_image)

        if self.heart < 3:  # стирання сердець
            if self.heart == 2:
                canvas.delete(heart_3)
            if self.heart == 1:
                canvas.delete(heart_3)
                canvas.delete(heart_2)

        window.design_castle()

        canvas.create_image(10, 102, anchor=NW, image=skeleton_image)
        canvas.create_image(30, 102, anchor=NW, image=skeleton_image)
        canvas.create_image(50, 102, anchor=NW, image=skeleton_image)
        canvas.create_image(70, 102, anchor=NW, image=skeleton_image)
        canvas.create_image(90, 102, anchor=NW, image=skeleton_image)

        canvas.create_image(420, 102, anchor=NW, image=skeleton_image)
        canvas.create_image(400, 102, anchor=NW, image=skeleton_image)
        canvas.create_image(380, 102, anchor=NW, image=skeleton_image)
        canvas.create_image(360, 102, anchor=NW, image=skeleton_image)
        canvas.create_image(340, 102, anchor=NW, image=skeleton_image)

        canvas.create_rectangle(185, 130, 320, 200, outline='#C0C0C0')
        canvas.create_rectangle(184, 129, 319, 199, outline='#C0C0C0')
        canvas.create_text(275, 165, text=f"{enemy}", font=('Courier', 25), fill='#C0C0C0')
        canvas.create_text(274, 164, text=f"{enemy}", font=('Courier', 25), fill='#C0C0C0')
        image_skeleton_head = canvas.create_image(193, 142, anchor=NW, image=skeleton_head_image)

        btn_arsenal_1 = Button(canvas, text="Меч - 1", font=('Times New Roman', 13), command=lambda: window.weapon(1),
                               bg='#000033',
                               fg='#00FF00')
        btn_arsenal_3 = Button(canvas, text="Катапульта - 10", font=('Times New Roman', 13), state='disabled',
                               bg='#000033',
                               fg='#00FF00')
        btn_arsenal_4 = Button(canvas, text="Гармата - 50", font=('Times New Roman', 13), state='disabled',
                               bg='#000033',
                               fg='#00FF00')
        btn_arsenal_2 = Button(canvas, text="Арбалет - 5", font=('Times New Roman', 13), state='disabled', bg='#000033',
                               fg='#00FF00')

        if self.level > 1:  # доступні види зброї для кожного рівня
            btn_arsenal_2 = Button(canvas, text="Арбалет - 5", font=('Times New Roman', 13),
                                   command=lambda: window.weapon(5),
                                   bg='#000033',
                                   fg='#00FF00')
        if self.level > 3:
            btn_arsenal_3 = Button(canvas, text="Катапульта - 10", font=('Times New Roman', 13),
                                   command=lambda: window.weapon(10),
                                   bg='#000033',
                                   fg='#00FF00')

        if self.level > 5:
            btn_arsenal_4 = Button(canvas, text="Гармата - 50", font=('Times New Roman', 13),
                                   command=lambda: window.weapon(50),
                                   bg='#000033',
                                   fg='#00FF00')

        btn_arsenal_1.configure(width=12, height=2, highlightcolor='#FF0000')
        btn_arsenal_1.place(relx=0.3, rely=0.55, anchor=CENTER)
        canvas.create_image(40, 255, anchor=NW, image=sword_image)

        btn_arsenal_2.configure(width=12, height=2, highlightcolor='#FF0000')
        btn_arsenal_2.place(relx=0.7, rely=0.55, anchor=CENTER)
        canvas.create_image(420, 260, anchor=NW, image=crossbow_image)
        btn_arsenal_3.configure(width=12, height=2, highlightcolor='#FF0000')
        btn_arsenal_3.place(relx=0.3, rely=0.7, anchor=CENTER)
        btn_arsenal_4.configure(width=12, height=2, highlightcolor='#FF0000')
        btn_arsenal_4.place(relx=0.7, rely=0.7, anchor=CENTER)

    def passed_level(self, check):
        global btn_menu, btn_next_level, time_level, end_time, \
            start_time, execution_time, minutes, seconds, control, btn_exit
        window.clear_all()
        time_level = 0
        place_sceleton = 102
        canvas.create_text(85, 25, text=f"Рівень:{self.level}", font=('Courier', 15), fill='#98FF98')
        canvas.create_text(84, 24, text=f"Рівень:{self.level}", font=('Courier', 15), fill='#00FF00')

        self.score = lib.Score(self.score, check, self.level, self.heart)   # формування балів

        canvas.create_text(420, 25, text=f"Бали:{self.score}", font=('Courier', 15), fill='#98FF98')
        canvas.create_text(419, 24, text=f"Бали:{self.score}", font=('Courier', 15), fill='#00FF00')

        canvas.create_line(0, 45, 500, 45, fill='#98FF98')

        end_time = datetime.datetime.now()
        execution_time = end_time - start_time
        total_seconds = execution_time.total_seconds()

        minutes += int(total_seconds // 60)  # формування часу
        seconds += int(total_seconds % 60)
        if seconds >= 60:
            minutes += 1
            seconds -= 60

        if control != 1:
            FileData.delete_names(name)  # стирання однакового імені

        canvas.create_text(250, 325, text=f"Час проходження: {minutes}:{seconds}", font=('Courier', 26),
                           fill='#00FF00')

        if check == 0 and self.level == 10 and control != 1:  # проайдена гра
            btn_exit = Button(canvas, text="Вийти", font=('Times New Roman', 13), command=Design.stop_program,
                              bg='#000033', fg='#00FF00')
            btn_exit.configure(width=15, height=2, highlightcolor='#FF0000')
            btn_exit.place(relx=0.5, rely=0.53, anchor=CENTER)
            canvas.create_text(250, 70, text="Ви пройшли гру!", font=('Courier', 26), fill='#00FF00')
            canvas.create_text(249, 69, text="Ви пройшли гру!", font=('Courier', 26), fill='#00FF00')
            canvas.create_text(250, 150, text=f"Пройдено рівнів: {self.level}", font=('Courier', 26), fill='#00FF00')
            canvas.create_text(250, 200, text=f"Рекорд: {self.score}", font=('Courier', 26), fill='#00FF00')
            Design.design_castle()
            window.file_filling()

        if check == 0 and self.level != 10 or control == 1:  # пройденний рівень

            btn_exit = Button(canvas, text="Вийти", font=('Times New Roman', 13), command=Design.stop_program,
                              bg='#000033', fg='#00FF00')
            btn_exit.configure(width=15, height=2, highlightcolor='#FF0000')
            btn_exit.place(relx=0.5, rely=0.5, anchor=CENTER)
            canvas.create_text(250, 70, text="Ви пройшли рівень!", font=('Courier', 26), fill='#00FF00')
            canvas.create_text(249, 69, text="Ви пройшли рівень!", font=('Courier', 26), fill='#00FF00')

            if control != 1:
                btn_next_level = Button(canvas, text="Наступний рівень", font=('Times New Roman', 13),
                                        command=window.new_level,
                                        bg='#000033', fg='#00FF00')
                btn_next_level.place(relx=0.5, rely=0.35, anchor=CENTER)  # Розміщення кнопки посередині канви
                btn_next_level.configure(width=15, height=2, highlightcolor='#FF0000')
            else:  # пробний рівень
                btn_menu = Button(canvas, text="Меню", font=('Times New Roman', 13),
                                  command=Design.menu,
                                  bg='#000033', fg='#00FF00')
                btn_menu.place(relx=0.5, rely=0.35, anchor=CENTER)  # Розміщення кнопки посередині канви
                btn_menu.configure(width=15, height=2, highlightcolor='#FF0000')
                self.level = 0
                check = 0
                self.score = 0
                minutes = 0
                seconds = 0
                control = 0
                self.heart = 3

            Design.design_castle()

        if check == 1:  # якщо програв
            self.level -= 1
            self.heart -= 1

            if self.heart == 0 and control != 1:  # програв рівень
                btn_exit = Button(canvas, text="Вийти", font=('Times New Roman', 13), command=Design.stop_program,
                                  bg='#000033', fg='#00FF00')
                btn_exit.configure(width=15, height=2, highlightcolor='#FF0000')
                btn_exit.place(relx=0.5, rely=0.53, anchor=CENTER)
                canvas.create_text(250, 70, text="Ви не пройшли гру!", font=('Courier', 26), fill='#00FF00')
                canvas.create_text(249, 69, text="Ви не пройшли гру!", font=('Courier', 26), fill='#00FF00')
                canvas.create_text(250, 150, text=f"Пройдено рівнів: {self.level}", font=('Courier', 26),
                                   fill='#00FF00')
                canvas.create_text(250, 200, text=f"Рекорд: {self.score}", font=('Courier', 26), fill='#00FF00')
                window.design_castle()
                window.file_filling()

            if self.heart != 0:  # не пройшов гру
                canvas.create_text(250, 110, text="Ви не пройшли рівень!", font=('Courier', 26), fill='#00FF00')
                canvas.create_text(249, 109, text="Ви не пройшли рівень!", font=('Courier', 26), fill='#00FF00')
                btn_exit = Button(canvas, text="Вийти", font=('Times New Roman', 13), command=Design.stop_program,
                                  bg='#000033', fg='#00FF00')
                btn_exit.configure(width=15, height=2, highlightcolor='#FF0000')
                btn_exit.place(relx=0.5, rely=0.5, anchor=CENTER)
                if control != 1:
                    btn_next_level = Button(canvas, text="Спробувати ще", font=('Times New Roman', 13),
                                            command=window.new_level,
                                            bg='#000033', fg='#00FF00')
                    btn_next_level.place(relx=0.5, rely=0.35, anchor=CENTER)  # Розміщення кнопки посередині канви
                    btn_next_level.configure(width=15, height=2, highlightcolor='#FF0000')
                    window.design_castle()
                else:  # пробний рівень
                    btn_menu = Button(canvas, text="Меню", font=('Times New Roman', 13),
                                      command=Design.menu,
                                      bg='#000033', fg='#00FF00')
                    btn_menu.place(relx=0.5, rely=0.35, anchor=CENTER)  # Розміщення кнопки посередині канви
                    btn_menu.configure(width=15, height=2, highlightcolor='#FF0000')
                    level = 0
                    check = 2
                    self.score = 0
                    minutes = 0
                    seconds = 0
                    control = 0
                    self.heart = 3

    @staticmethod
    def design_castle():  # повний дизайн
        canvas.create_image(-8, (500 - tower_image_weight + 2), anchor=NW, image=tower_image)
        canvas.create_image(52, (500 - tower_image_height + 2), anchor=NW, image=tower_image)
        canvas.create_image(115, (500 - tower_image_height + 2), anchor=NW, image=tower_image)
        Design.design_castle_part()

    @staticmethod
    def design_castle_part():  # частковий дизайн
        canvas.create_image(((500 / 2) - (castle_image_weight / 2)), (500 - castle_image_height + 2), anchor=NW,
                            image=castle_image)
        canvas.create_image(315, (500 - tower_image_height + 2), anchor=NW, image=tower_image)
        canvas.create_image(380, (500 - tower_image_height + 2), anchor=NW, image=tower_image)
        canvas.create_image(442, (500 - tower_image_height + 2), anchor=NW, image=tower_image)


start_time = datetime.datetime.now()
score = 0
level = 0
check = 2
heart = 3
time_level = 0
end_level = 0
end_time = 0
execution_time = 0
minutes = 0
seconds = 0
control = 0
entry = 0
arsenal = 0
enemy = 0
name = ' '

window = Design(score, level, heart)

filename = "D:\Python\Курсова робота\дані_гри.txt"  # Назва файлу з даними

btn_1 = Button(canvas, text="Нова гра", font=('Times New Roman', 13), command=lambda: window.level_game(enemy, arsenal),
               bg='#000033',
               fg='#00FF00')
btn_2 = Button(canvas, text="Продовжити", font=('Times New Roman', 13), state='disabled', bg='#000033', fg='#00FF00')
btn_3 = Button(canvas, text="Правила", font=('Times New Roman', 13), command=lambda: window.text_rules(), bg='#000033',
               fg='#00FF00')
btn_4 = Button(canvas, text="Рейтинг", font=('Times New Roman', 13), command='disabled', bg='#000033', fg='#00FF00')
btn_5 = Button(canvas, text="Вийти", font=('Times New Roman', 13), command=Design.stop_program, bg='#000033',
               fg='#00FF00')

btn_menu = Button(canvas, text="Меню", font=('Times New Roman', 13), command=Design.clear_rules, bg='#000033',
                  fg='#00FF00')
btn_arsenal_1 = Button(canvas, text="Меч - 1", font=('Times New Roman', 13), command=lambda: window.weapon(1),
                       bg='#000033',
                       fg='#00FF00')
btn_arsenal_2 = Button(canvas, text="Арбалет - 5", font=('Times New Roman', 13), state='disabled', bg='#000033',
                       fg='#00FF00')
btn_arsenal_3 = Button(canvas, text="Катапульта - 10", font=('Times New Roman', 13), state='disabled', bg='#000033',
                       fg='#00FF00')
btn_arsenal_4 = Button(canvas, text="Гармата - 50", font=('Times New Roman', 13), state='disabled', bg='#000033',
                       fg='#00FF00')
btn_next_level = Button(canvas, text="Наступний рівень", font=('Times New Roman', 13), command=Design.clear_rules,
                        bg='#000033', fg='#00FF00')

button_input = Button(tk, text="Ввести", font=('Times New Roman', 15), command=window.button_level,
                      bg='#000033',
                      fg='#00FF00')

btn_exit = Button(canvas, text="Вийти", font=('Times New Roman', 13), command=Design.stop_program,
                  bg='#000033', fg='#00FF00')

window.menu()
tk.mainloop()
