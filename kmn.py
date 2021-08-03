import random
comp = 0
player = 0
for i in range(3):
    print('\t--------Рунд №'+ str(i+1)+'--------')
    kmn = ['Камень', 'Ножницы', 'Бумага']
    ran: str = random.choice(kmn)
    v = input("Что вы выбирете ?")
    print("Вы выбрали : ", v, '!')
    kmn = ['Камень', 'Ножницы', 'Бумага']
    print("Компютор выбрал : ", ran, "!")
    while True:
        if (v == ran):
            print('Оу,ничя!')
        elif (v == 'Камень') and ran == 'Бумага':
            comp = comp + 1
            print('Ты проиграл !')
        elif (v == "Камень") and ran == 'Ножницы':
            player = player + 1
            print('Вы выиграли !')
        elif (v == 'Ножницы') and ran == 'Камень':
            comp = comp + 1
            print('Ты проиграл !')
        elif (v == 'Ножницы') and ran == 'Бумага':
            player = player + 1
            print('Вы выиграли !')
        elif (v == 'Бумага') and ran == 'Ножницы':
            comp = comp + 1
            print('Ты проиграл !')
        elif (v == 'Бумага') and ran == 'Камень':
            player = player + 1
            print('Вы выиграли !')
        else:
            exit(1)
        break
print('\t-----Результат-----')
if i <= 3 and player==comp:
   print("Ничя")
elif i <= 3 and player<=comp:
    print("Ты проиграл!")
elif i <= 3 and player >= comp:
    print("Ты выиграл ")
else:
    exit(1)
