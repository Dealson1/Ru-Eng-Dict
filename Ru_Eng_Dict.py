from module import *
rus_list = readFile("rus.txt")
eng_list = readFile("eng.txt")

while True:
    menu = input("Перевод - T\nДобавить слово - N\nИсправить ошибку - E\nПроверка знаний - C\nСинтез речи - R\nВыход - L\n")
    if menu.upper() == "T":
        v = int(input("РУС - АНГЛ или АНГЛ - РУС (1/2): "))
        if v == 1:
            basic = rus_list
            secondary = eng_list
            t = translate(basic, secondary)
        elif v == 2:
            basic = eng_list
            secondary = rus_list
            t = translate(basic, secondary)

        if t == False:
            ans = input("Хотите добавить новое слово? (y/n): ")
            if ans == "y":
                rus = input("Новое слово (на русском): ")
                eng = input("New word (in english): ")
                rus_list = wordN("rus.txt", rus.lower())
                eng_list = wordN("eng.txt", eng.lower())
            else:
                pass
    elif menu.upper() == "N":
        rus = input("Новое слово (на русском): ")
        eng = input("New word (in english): ")
        rus_list = wordN("rus.txt", rus.lower())
        eng_list = wordN("eng.txt", eng.lower())
        pass
    elif menu.upper() == "E":
        choice = int(input("Перевод слова на каком языке исправить? Англ/Рус (1/2): "))
        if choice == 1:
            lang1 = rus_list
            lang2 = eng_list
            correction(lang1, lang2, choice)
            eng_list = readFile("eng.txt")
            print("Перевод исправлен")
        else:
            lang1 = eng_list
            lang2 = rus_list
            correction(lang1, lang2, choice)
            rus_list = readFile("rus.txt")
            print("Перевод исправлен")
        pass
    elif menu.upper() == "C":
        print("Проверка знаний")
        choice = int(input("С какого на какой язык переводить слова?. АНГЛ - РУС / РУС - АНГЛ (1/2): "))
        if choice == 1:
            lang1 = eng_list
            lang2 = rus_list
            chekup(lang1, lang2)
        else:
            lang1 = rus_list
            lang2 = eng_list
            chekup(lang1, lang2)
        pass
    elif menu.upper() == "R":
        ttsg()
    else:
        print("Выход.")
        break
