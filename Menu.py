# class Menu


class Menu:
    def __init__(self):
        pass

    def choose(self, userInput):
        if userInput in {0, 1, 2}:
            return userInput
        else:
            self.home()

    def home(self):
        print("Добро пожаловать в Монополию")
        print("1.Играть с классическими правилами")
        print("2.Играть с хоумрулами")
        print("0.Выход")
