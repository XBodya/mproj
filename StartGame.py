# Start Game

class StartGame:
    def __init__(self):
        self.playerNumber = 0
        self.playerData = []
        self.givePlayerNumberQ = False

    def givePlayerNumber(self):
        self.playerNumber = int(input("Введите количество игроков(2-6)>> "))
        if isinstance(self.playerNumber, int):
            if self.playerNumber < 2 or self.playerNumber > 6:
                print("Неверное число игроков")
        else:
            self.givePlayerNumber()
        self.givePlayerNumberQ = True

    def givePlayerName(self):
        pass

