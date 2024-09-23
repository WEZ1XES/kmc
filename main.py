
#Яндекс код банит, я на гитхаб выложил 


import random
import time

player_money = 0
comp_money = 0

while True:
    time.sleep(1)
    player = int(input('Выберете ход: 1 = камень, 2 = ножницы или 3 = бумага'))
    time.sleep(1)
    comp = random.randint(1,3)
    if comp == 1:
        comp_choise = "камень"
    if comp == 2:
        comp_choise = "ножницы"
    if comp == 3:
        comp_choise = "бумага"
    time.sleep(1)
    print('Выбор компьютера: ', comp_choise)
    time.sleep(1)

    if (player == 1 and comp == 2) or (player == 2 and comp == 3) or (player == 3 and comp == 1):
        time.sleep(1)
        print('Ты победил в эпичной схватке!')
        comp_money += 1
        print('Тебе + одно очко')
        time.sleep(1)
    elif player == comp:
        time.sleep(1)
        print('Ничья')
        time.sleep(1)
    else:
        time.sleep(1)
        print('Ты проиграл, жди бан')
        time.sleep(1)
        player_money += 1
        print('Компьютеру + одно очко')
    print(comp_money)
    print(player_money)

