import re





plotis = 3

k = 0

sk = []

lenta = [
    ["- ", "- ", "- "], 
    ["- ", "- ", "- "], 
    ["- ", "- ", "- "]
]

def format_lenta(lenta):
    return "\n".join([" ".join(i) for i in lenta])





class Counter:
    def increase_counter():
        global k
        k += 1

    def decrease_counter():
        global k
        k -= 1

    def reset_counter():
        global k
        k = 0





class File:
    def save_game():
        File1 = open("Lenta.txt", "w")
        File1.write(format_lenta(lenta))
        File1.close()
        text = input("Jeigu norite pamatyti ankstesnio žaidimo lentą parašykite 3\nJeigu norite pradėti žaidimą iš naujo parašykite 2\n:")
        if text == "3":
            File.print_saved_game()
        elif text == "2":
            Game.game()
        else:
            print("Netinkamas užrašas")
            File.save_game()

    def print_saved_game():
        File1 = open("Lenta.txt", "r")
        for i in File1:
            print(i.strip())
        File1.close()
        text = input("Jeigu norite pradėti žaidimą iš naujo parašykite 2\n:")
        if text == "2":
            Game.game()
        else:
            print("Netinkamas užrašas")
            File.print_saved_game()





class Lenta:
    def print_lenta():
        print("   1   2   3")
        for i in range(plotis):
            print(chr(65 + i), end="  ")
            for j in range(plotis):
                print(lenta[i][j], end="  ")
            print()

    def new_game():
        Counter.reset_counter()
        sk.clear()
        for i in range(plotis):
            for j in range(plotis):
                lenta[i][j] = "- "
        Lenta.print_lenta()
        print("1 žaidėjas pradeda žaidimą")

    def after_game():
        text = input("Jeigu norite išsaugoti šio žaidimo lentą, parašykite 0\nJeigu norite pamatyti ankstesnio žaidimo lentą parašykite 3\nJeigu norite pradėti žaidimą iš naujo parašykite 2\n:")
        if text == "3":
            File.print_saved_game()
        elif text == "2":
            Game.game()
        elif text == "0":
            File.save_game()
        else:
            print("Netinkamas užrašas")
            Lenta.after_game()





class Game:
    def __init__(self):
        self.lenta = lenta

    def start():
        text = input("Jeigu norite pamatyti praeito žaidimo lentą, parašykite 0\nJeigu norite pradėti naują žaidimą parašykite 2 (atminkite, jeigu žaidimo eigoje norite pradėti žaidimą iš naujo arba žaidimas baigėsi lygiosiomis, parašykite 1)\n:")
        if text == "0":
            File.print_saved_game()
        elif text == "2":
            Game.game()
        else:
            print("Netinkamas užrašas")
            Game.start()

    @classmethod
    def game(cls):
            Lenta.new_game()
            text = input("Įveskite ėjimo koordinates:")
            if text != "":
                if text == "1":
                    Game.game()
                else:
                    for char in text:
                        if char.isdigit():
                            sk.append(int(char))
                    raide = re.findall(r'[a-zA-Z]+', text)
            if text == "1":
                return
            if raide[0] == "A":
                if lenta[0][sk[0] - 1] != "- ":
                    print("Šis laukelis užimtas, pasirinkite kitą laukelį")
                    Game.move()
                else:
                    if k == 0:
                        lenta[0][sk[0] - 1] = "X "
                    else:
                        lenta[0][sk[0] - 1] = "O "
                    Lenta.print_lenta()
                    if k == 0:
                        sk.clear()
                        print("2 žaidėjo eilė")
                        Counter.increase_counter()
                        Game.move()
                    else:
                        sk.clear()
                        print("1 žaidėjo eilė")
                        Counter.decrease_counter()
                        Game.move()

            elif raide[0] == "B":
                if lenta[1][sk[0] - 1] != "- ":
                    print("Šis laukelis užimtas, pasirinkite kitą laukelį")
                    Game.move()
                else:
                    if k == 0:
                        lenta[1][sk[0] - 1] = "X "
                    else:
                        lenta[1][sk[0] - 1] = "O "
                    Lenta.print_lenta()
                    if k == 0:
                        sk.clear()
                        print("2 žaidėjo eilė")
                        Counter.increase_counter()
                        Game.move()
                    else:
                        sk.clear()
                        print("1 žaidėjo eilė")
                        Counter.decrease_counter()
                        Game.move()

            else:
                if lenta[2][sk[0] - 1] != "- ":
                    print("Šis laukelis užimtas, pasirinkite kitą laukelį")
                    Game.move()
                else:
                    if k == 0:
                        lenta[2][sk[0] - 1] = "X "
                    else:
                        lenta[2][sk[0] - 1] = "O "
                    Lenta.print_lenta()
                    if k == 0:
                        sk.clear()
                        print("2 žaidėjo eilė")
                        Counter.increase_counter()
                        Game.move()
                    else:
                        sk.clear()
                        print("1 žaidėjo eilė")
                        Counter.decrease_counter()
                        Game.move()

    @classmethod
    def move(cls):
            text = input("Įveskite ėjimo koordinates:")
            if text != "":
                if text == "1":
                    Game.game()
                else:
                    for char in text:
                        if char.isdigit():
                            sk.append(int(char))
                    raide = re.findall(r'[a-zA-Z]+', text)
            if text == "1":
                return
            if raide[0] == "A":
                if lenta[0][sk[0] - 1] != "- ":
                    print("Šis laukelis užimtas, pasirinkite kitą laukelį")
                    cls.move()
                else:
                    if k == 0:
                        lenta[0][sk[0] - 1] = "X "
                    else:
                        lenta[0][sk[0] - 1] = "O "
                    Lenta.print_lenta()
                    if cls.check_win(lenta):
                        if k == 0:
                            print("1 žaidėjas laimėjo")
                        else:
                            print("2 žaidėjas laimėjo")
                        Lenta.after_game()
                    if cls.check_win(lenta):
                        return
                    else:
                        if k == 0:
                            sk.clear()
                            print("2 žaidėjo eilė")
                            Counter.increase_counter()
                            cls.move()
                        else:
                            sk.clear()
                            print("1 žaidėjo eilė")
                            Counter.decrease_counter()
                            cls.move()

            elif raide[0] == "B":
                if lenta[1][sk[0] - 1] != "- ":
                    print("Šis laukelis užimtas, pasirinkite kitą laukelį")
                    cls.move()
                else:
                    if k == 0:
                        lenta[1][sk[0] - 1] = "X "
                    else:
                        lenta[1][sk[0] - 1] = "O "
                    Lenta.print_lenta()
                    if cls.check_win(lenta):
                        if k == 0:
                            print("1 žaidėjas laimėjo")
                        else:
                            print("2 žaidėjas laimėjo")
                        Lenta.after_game()
                    if cls.check_win(lenta):
                        return
                    else:
                        if k == 0:
                            sk.clear()
                            print("2 žaidėjo eilė")
                            Counter.increase_counter()
                            cls.move()
                        else:
                            sk.clear()
                            print("1 žaidėjo eilė")
                            Counter.decrease_counter()
                            cls.move()

            else:
                if lenta[2][sk[0] - 1] != "- ":
                    print("Šis laukelis užimtas, pasirinkite kitą laukelį")
                    cls.move()
                else:
                    if k == 0:
                        lenta[2][sk[0] - 1] = "X "
                    else:
                        lenta[2][sk[0] - 1] = "O "
                    Lenta.print_lenta()
                    if cls.check_win(lenta):
                        if k == 0:
                            print("1 žaidėjas laimėjo")
                        else:
                            print("2 žaidėjas laimėjo")
                        Lenta.after_game()
                    if cls.check_win(lenta):
                        return
                    else:
                        if k == 0:
                            sk.clear()
                            print("2 žaidėjo eilė")
                            Counter.increase_counter()
                            cls.move()
                        else:
                            sk.clear()
                            print("1 žaidėjo eilė")
                            Counter.decrease_counter()
                            cls.move()
     




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
            elif all(cell == i[1] for cell in i) and i[1] != "- ":
                return True
            elif all(cell == i[2] for cell in i) and i[2] != "- ":
                return True
        return False
        
class VerticalWin(Win):
    def check_win(self, lenta):
        for j in range(3):
            if all(i[j] == lenta[0][j] for i in lenta) and lenta[0][j] != "- ":
                return True
            elif all(i[j] == lenta[1][j] for i in lenta) and lenta[1][j] != "- ":
                return True
            elif all(i[j] == lenta[2][j] for i in lenta) and lenta[2][j] != "- ":
                return True
        return False
    
class DiagonalWin(Win):
    def check_win(self, lenta):
        if (lenta[0][0] == lenta[1][1] == lenta[2][2] != "- ") or (lenta[0][2] == lenta[1][1] == lenta[2][0] != "- "):
            return True
        else:
            return False





game = Game
game.start()
