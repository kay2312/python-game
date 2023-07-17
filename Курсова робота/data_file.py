from tkinter import *
from canvas import *
import textwrap


class FileData:
    @staticmethod
    def delete_names(name):     # вмдалення повторного ім'я
        with open(filename, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            file.seek(0)  # переміщаємо покажчик на початок файлу

            for line in lines:
                if name not in line:
                    file.write(line)

            file.truncate()  # відсікаємо зайву частину файлу


    def file_filling(self, name, level, score, minutes, seconds):  # заповнення у файл даних про гравця

        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f'{name}, {level}, {score}, {minutes}, {seconds}\n')

    def file_reading(self):         # виведення даних про гравців

        z = 50

        with open(filename, 'r', encoding='utf-8') as file:
            canvas.create_text(240, 45, text=f' Ім\'я: \t\tРівень: \tБали: \tЧас: ', font=('Courier', 14),
                               fill='#00FF00')
            data = file.read()

            if data.isspace():  # якщо є тільки пробіли (немає даних)
                pass
            else:
                players = []
                for line in data.splitlines():
                    values = line.strip().split(',')
                    if len(values) == 1 and values[0].strip() == '':
                        continue
                    name = values[0]
                    level = int(values[1])
                    score = int(values[2])
                    minutes = int(values[3])
                    seconds = int(values[4])

                    total_seconds = minutes * 60 + seconds
                    players.append((name, level, score, total_seconds))

                # сортування гравців за балами і часом
                players_sorted = sorted(players, key=lambda x: (-x[2], x[3]))

                for player in players_sorted[:10]:
                    name, level, score, total_seconds = player

                    minutes = total_seconds // 60
                    seconds = total_seconds % 60

                    z += 30

                    canvas.create_text(245, z, text=f'{name: <10} \t{level} \t\t{score} \t{minutes}:{seconds}',
                                       font=('Courier', 14), fill='#00FF00')

    def text_rules(self):  # завантажити текст з файлу
        text_rules = open('D:\\Python\\Курсова робота\\Правила.txt', 'r', encoding='utf-8')
        text = text_rules.read()

        # розділити текст на декілька рядків
        wrapper = textwrap.TextWrapper(width=56)  # задати ширину рядка
        wrapped_text = wrapper.wrap(text)

        y = 20
        for line in wrapped_text:
            canvas.create_text(252, y, text=line, font=('Courier', 11), fill='#00FF00')
            y += 20


filename = "D:\Python\Курсова робота\дані_гри.txt"
data = FileData()
