import ctypes
from tkinter import *
from data_file import FileData
from canvas import *

lib = ctypes.CDLL('./game_2.dll')


class Weapon:
    def __init__(self, enemy, arsenal):
        self.enemy = enemy
        self.arsenal = arsenal

    def control(self, enemy, arsenal):  # перевірка на проходження рівня
        global check
        if self.enemy == 0 and self.arsenal == 0:
            check = 0
            return check

        elif self.enemy != 0 and self.arsenal == 0:
            check = 1
            return check
        elif self.enemy == 0 and self.arsenal != 0:
            check = 1
            return check
        elif self.enemy < 0:
            check = 1
            return check
        elif self.arsenal < 0:
            check = 1
            return check
        else:
            return 2

    def sword(self, enemy):   # зменшення ворогів
        self.enemy = lib.Fire(self.enemy, 1)
        return self.enemy

    def crossbow(self, enemy):
        self.enemy = lib.Fire(self.enemy, 5)
        return self.enemy

    def catapult(self, enemy):
        self.enemy = lib.Fire(self.enemy, 10)
        return self.enemy

    def gun(self, enemy):
        self.enemy = lib.Fire(self.enemy, 50)
        return self.enemy

    def arsenal(self, arsenal):
        self.arsenal = lib.Fire(self.arsenal, 1)
        return self.arsenal


end_level = 0
arsenal = 0
enemy = 0
check = 1
level = Weapon(enemy, arsenal)
