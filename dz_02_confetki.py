"""Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?" """

from random import randint

common_count = 200
max_take = 28
input("Нажмите Enter для того, чтобы выбрать кто ходит первый")
select = randint(1, 7)
print("Вам выпало", select)
comp_select = randint(1, 7)
print("Компьютеру выпало:", comp_select)
turn_player = False if comp_select > select else True
while common_count > max_take:
    if turn_player:
        confets = max_take + 1
        while confets > max_take:
            confets = int(input(f"Ваш ход. Сколько конфеток берете (от 1 до {max_take})? "))
    else:
        confets = randint(1, max_take + 1)
        print(f"Компьютер взял {confets} конфет")
    common_count -= confets
    print(f"Осталось {common_count} конфет")
    turn_player = not turn_player

if turn_player:
    print("Вы победили!")
else:
    print("Победил компьютер")