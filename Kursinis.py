plotis = 3
lenta = [["- ", "- ", "- "], 
         ["- ", "- ", "- "], 
         ["- ", "- ", "- "]]



k = 0
def increase_counter():
    global k
    k += 1

def decrease_counter():
    global k
    k -= 1

def reset_counter():
    global k
    k = 0



class Game:
    def __init__(self):
        self.lenta = lenta

    def new_game():
        reset_counter()
        for i in range(plotis):
            for j in range(plotis):
                lenta[i][j] = "- "
        print("   1   2   3")
        for i in range(plotis):
            print(chr(65 + i), end="  ")
            for j in range(plotis):
                print(lenta[i][j], end="  ")
            print()
        print("1 žaidėjas pradeda žaidimą")



class Player:
    def  __init__(self):
        self.lenta = lenta

    @classmethod
    def move(cls, a, b):
        if a == "A":
            if lenta[0][b-1] != "- ":
                print("Šis laukelis užimtas, pasirinkite kitą laukelį")
            else:
                if k == 0:
                    lenta[0][b-1] = "X "
                else:
                    lenta[0][b-1] = "O "
                print("   1   2   3")
                for i in range(plotis):
                    print(chr(65 + i), end="  ")
                    for j in range(plotis):
                        print(lenta[i][j], end="  ")
                    print()
                if cls.check_win(lenta):
                    if k == 0:
                        print("1 žaidėjas laimėjo")
                    else:
                        print("2 žaidėjas laimėjo")
                if cls.check_win(lenta):
                    return
                else:
                    if k == 0:
                        print("2 žaidėjo eilė")
                        increase_counter()
                    else:
                        print("1 žaidėjo eilė")
                        decrease_counter()
        elif a == "B":
            if lenta[1][b-1] != "- ":
                print("Šis laukelis užimtas, pasirinkite kitą laukelį")
            else:
                if k == 0:
                    lenta[1][b-1] = "X "
                else:
                    lenta[1][b-1] = "O "
                print("   1   2   3")
                for i in range(plotis):
                    print(chr(65 + i), end="  ")
                    for j in range(plotis):
                        print(lenta[i][j], end="  ")
                    print()
                if cls.check_win(lenta):
                    if k == 0:
                        print("1 žaidėjas laimėjo")
                    else:
                        print("2 žaidėjas laimėjo")
                if cls.check_win(lenta):
                    return
                else:
                    if k == 0:
                        print("2 žaidėjo eilė")
                        increase_counter()
                    else:
                        print("1 žaidėjo eilė")
                        decrease_counter()
        else:
            if lenta[2][b-1] != "- ":
                print("Šis laukelis užimtas, pasirinkite kitą laukelį")
            else:
                if k == 0:
                    lenta[2][b-1] = "X "
                else:
                    lenta[2][b-1] = "O "
                print("   1   2   3")
                for i in range(plotis):
                    print(chr(65 + i), end="  ")
                    for j in range(plotis):
                        print(lenta[i][j], end="  ")
                    print()
                if cls.check_win(lenta):
                    if k == 0:
                        print("1 žaidėjas laimėjo")
                    else:
                        print("2 žaidėjas laimėjo")
                if cls.check_win(lenta):
                    return
                else:
                    if k == 0:
                        print("2 žaidėjo eilė")
                        increase_counter()
                    else:
                        print("1 žaidėjo eilė")
                        decrease_counter()



    @staticmethod
    def check_win(lenta):
        horizontal_win = HorizontalWin()
        vertical_win = VerticalWin()
        diagonal_win = DiagonalWin()
        if (horizontal_win.check_win(lenta) or
            vertical_win.check_win(lenta) or
            diagonal_win.check_win(lenta)):
            return True
        else:
            return False



class Win:
    def check_win(self):
        raise NotImplementedError
    
class HorizontalWin(Win):
    def check_win(self, lenta):
        for i in lenta:
            if all(cell == i[0] for cell in i) and i[0] != "- ":
                return True
            else:
                return False
        
class VerticalWin(Win):
    def check_win(self, lenta):
        for j in range(3):
            if all(i[j] == lenta[0][j] for i in lenta) and lenta[0][j] != "- ":
                return True
            else:
                return False
    
class DiagonalWin(Win):
    def check_win(self, lenta):
        if (lenta[0][0] == lenta[1][1] == lenta[2][2] != "- ") or (lenta[0][2] == lenta[1][1] == lenta[2][0] != "- "):
            return True
        else:
            return False






game = Game
player1 = Player
player2 = Player

game.new_game()

#player1.move("A", 1)

#player2.move("B", 2)

#player1.move("B", 3)

#player2.move("A", 3)

#player1.move("A", 2)

#player2.move("C", 1)
