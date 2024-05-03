
# Tic-Tac-Toe game

### Introduction

My application is a Tic-Tac-Toe game. To start the program, you have to run the code. To use the program, players will have to write input for every choice of action. In every step of the program there will be instructions explaining your options or telling what to do next. 

### Body/Analysis

I have used inheritance and builder design pattern while coding win condition class:
```
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
Inheritance was achieved with check_win method:<br>
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
```
<br>
Encapsulation was achieved with Game class:
```
class Game:
    def __init__(self):
        self.lenta = lenta

    def start():
        text = input("Jeigu norite pamatyti praeito žaidimo lentą, parašykite 0\nJeigu norite pradėti naują žaidimą parašykite 1 (atminkite, jeigu žaidimo eigoje norite pradėti žaidimą iš naujo arba žaidimas baigėsi lygiosiomis, parašykite 1)\n:")
        if text == "0":
            File.print_saved_game()
        elif text == "1":
            Game.game()
        else:
            print("Netinkamas užrašas")
            Game.start()
```
<br>
While, reading from file and writing to file is done with File class:
```
class File:
    def save_game():
        File1 = open("Lenta.txt", "w")
        File1.write(Lenta.format_lenta(lenta))
        File1.close()
        text = input("Jeigu norite pamatyti ankstesnio žaidimo lentą parašykite 2\nJeigu norite pradėti žaidimą iš naujo parašykite 1\n:")
        if text == "2":
            File.print_saved_game()
        elif text == "1":
            Game.game()
        else:
            print("Netinkamas užrašas")
            File.save_game()

    def print_saved_game():
        File1 = open("Lenta.txt", "r")
        for i in File1:
            print(i.strip())
        File1.close()
        text = input("Jeigu norite pradėti žaidimą iš naujo parašykite 1\n:")
        if text == "1":
            Game.game()
        else:
            print("Netinkamas užrašas")
            File.print_saved_game()
```

### Results and summary

In the end, my goal of making moving with coordinates was achieved. The hardest part was making win condition class and implementing it into move method, so that it would check if any player has won after each move.
