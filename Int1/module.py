import random
import time


def gameStart(homeRules):
    print("ok")

def homeRuleSet():
    print("Выберите хоумрулы:")
    homeRules = [0, 0, 0]
    while (1):
        print("1.Получите 400 при попадании прямо на поле \"Вперед\"")
        if homeRules[0] == 0:
            print("(выключено)")
        else:
            print("(включено)")
        print("2.Все деньги идущие на налоги можно получить на поле \"Бесплатная стоянка\"")
        if homeRules[1] == 0:
            print("(выключено)")
        else:
            print("(включено)")
        print("3.Игрок находящийся в тюрьме не получает ренту")
        if homeRules[3] == 0:
            print("(выключено)")
        else:
            print("(включено)")
        print("0.Готово")
        userInput = input()
        if userInput == "0":
            break
        elif userInput == "1":
            if homeRules[0] == 1:
                homeRules[0] = 0
            else:
                homeRules[0] = 1
        elif userInput == "2":
            if homeRules[1] == 1:
                homeRules[1] = 0
            else:
                homeRules[1] = 1
        elif userInput == "3":
            if homeRules[2] == 1:
                homeRules[2] = 0
            else:
                homeRules[2] = 1
        else:
            continue
    return homeRules


def mainMenu():
    while(1):
        print("Добро пожаловать в монополию!")
        print("1.Играть с классическими правилами")
        print("2.Играть с хоумрулами")
        print("0.Выход")
        userInput = input()
        if userInput == "0":
            exit(0)
        elif userInput == "1":
            gameStart([0, 0, 0])
        elif userInput == "2":
            gameStart(homeRuleSet())


