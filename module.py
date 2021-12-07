from random import *
from gtts import gTTS
import os

def translate(lang1: list, lang2: list):
    """
    Ищет индекс слова в списке и выводит его перевод

    Возвращает False, если такого слова нет
    :param list lang1: Список первого языка
    :param list lang2: Список второго языка
    """
    word = input("Введите слово: ")
    t = wordS(word, lang1)
    if t == True:
        index1 = lang1.index(word)
        transword = lang2[index1]
        print(f"Перевод: {transword}")
    else:
        print("Такого слова нет в словаре")
        return False

def wordN(file: str, x: str)->list:
    """
    Добавляет новое слово в список

    :param str f: Название файла
    :param str x: Добавляемое слово
    """
    mas = [] 
    with open(file, "a", encoding = "utf-8-sig") as f:
        f.write(x+"\n")
    mas = readFile(file)
    return mas

def readFile(file: str)->list:
    """
    Читает строки из файла и добавляем их в список

    :param str f: Название файла
    """
    file = open(file, "r", encoding = "utf-8-sig")
    mas = []
    for line in file:
        mas.append(line.strip())
    file.close()
    return mas

def wordS(n: str, l: list):
    """
    Ищет слово в списке

    Возвращает True/False
    :param str n: Ищет логин
    :rtype: bool
    """
    if n in l:
        t = True
    else:
        t = False
    return t

def correction(lang1: list, lang2: list, choice: int):
    """
    Ищет слово в файле и исправляет его

    :param list lang1: Список первого языка
    :param list lang2: Список второго языка
    :param int choice: Выбор языка
    """
    print("Введите слово, которе хотите исправить")
    if choice == 1:
        wordup = input("На рус.: ")
        word = wordup.lower()
        check = wordS(word, lang1)
    else:
        wordup = input("На англ.: ")
        word = wordup.lower()
        check = wordS(word, lang1)

    if check == False:
        print("Слово не найденно.")
    else:
        wordindex = lang1.index(word)
        transword = lang2[wordindex]
        print(f"Изначальный перевод - {transword}")
        print("Введите заменяемое слово")
        if choice == 1:
            replaceup = input("На англ.: ")
            replace = replaceup.lower()
            with open ("eng.txt", "r") as f:
                old_data = f.read()
            new_data = old_data.replace(transword, replace)
            with open ("eng.txt", "w") as f:
                f.write(new_data)
        else:
            replaceup = input("На рус.: ")
            replace = replaceup.lower()
            with open ("rus.txt", "r") as f:
                old_data = f.read()
            new_data = old_data.replace(transword, replace)
            with open ("rus.txt", "w") as f:
                f.write(new_data)

def chekup(lang1: list, lang2: list):
    """
    Проверка знаний слов.

    :param list lang1: Список первого языка
    :param list lang2: Список второго языка
    """
    r = 0
    i = 0
    print("Задание: будет даваться по три слова за раз. У данного слова нужно написать его перевод. В конце вы узнаете результат.")
    while True:
        for i in range(3):
            word = choice(lang1)
            index = lang1.index(word)
            transword = lang2[index]
            chek = input(f"{i+1}. {word} - ")
            if chek == transword:
                i += 1
                r += 1
                print("Перевод верный")
            else:
                i += 1
                print("Перевод не верный")
        result = r/i * 100
        print(f"Ваш результат: {r} правильных ответов, {result}%")
        ans = input("Желаете закончить? y/n ")
        if ans == "y":
            break

def ttsG():
    '''
    Синтез речи.
    '''
    print("Синтез речи")
    lang = int(input("На каком языке хотите воспроизводить речь? РУС/АНГЛ - (1/2): "))
    blabla = input('Введите слово: ')
    if lang == 1:
        tts = gTTS(text=blabla, lang="ru")
        tts.save("test.mp3")
    else:
        tts = gTTS(text=blabla, lang="en")
        tts.save("test.mp3")
    os.system("test.mp3")
