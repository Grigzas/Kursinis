
# Tic-Tac-Toe game

### Introduction

My application is a Tic-Tac-Toe game. To start the program, you have to run the code. To use the program, players will have to write input for every choice of action. In every step of the program there will be instructions explaining your options or telling what to do next. 

### Body/Analysis

I have used inheritance and builder design pattern while coding win condition class:<br>
class Win:<br>
    def check_win(self):<br>
        raise NotImplementedError<br>
    <br>
class HorizontalWin(Win):<br>
    def check_win(self, lenta):<br>
        for i in lenta:<br>
            if all(cell == i[0] for cell in i) and i[0] != "- ":<br>
                return True<br>
            elif all(cell == i[1] for cell in i) and i[1] != "- ":<br>
                return True<br>
            elif all(cell == i[2] for cell in i) and i[2] != "- ":<br>
                return True<br>
        return False<br>
        
class VerticalWin(Win):<br>
    def check_win(self, lenta):<br>
        for j in range(3):<br>
            if all(i[j] == lenta[0][j] for i in lenta) and lenta[0][j] != "- ":<br>
                return True<br>
            elif all(i[j] == lenta[1][j] for i in lenta) and lenta[1][j] != "- ":<br>
                return True<br>
            elif all(i[j] == lenta[2][j] for i in lenta) and lenta[2][j] != "- ":<br>
                return True<br>
        return False<br>
    <br>
class DiagonalWin(Win):<br>
    def check_win(self, lenta):<br>
        if (lenta[0][0] == lenta[1][1] == lenta[2][2] != "- ") or (lenta[0][2] == lenta[1][1] == lenta[2][0] != "- "):<br>
            return True<br>
        else:<br>
            return False<br>
<br>
<br>
<br>
Inheritance was achieved with check_win method:<br>
@staticmethod<br>
def check_win(lenta):<br>
    horizontal_win = HorizontalWin()<br>
    vertical_win = VerticalWin()<br>
    diagonal_win = DiagonalWin()<br>
    if (horizontal_win.check_win(lenta) or<br>
        vertical_win.check_win(lenta) or<br>
        diagonal_win.check_win(lenta)):<br>
        return True<br>
    else:<br>
        return False<br>
<br>
<br>
<br>
Encapsulation was achieved with Game class:<br>
class Game:<br>
    def __init__(self):<br>
        self.lenta = lenta<br>
<br>
    def start():<br>
        text = input("Jeigu norite pamatyti praeito žaidimo lentą, parašykite 0\nJeigu norite pradėti naują žaidimą parašykite 1 (atminkite, jeigu žaidimo eigoje norite pradėti žaidimą iš naujo arba žaidimas baigėsi lygiosiomis, parašykite 1)\n:")<br>
        if text == "0":<br>
            File.print_saved_game()<br>
        elif text == "1":<br>
            Game.game()<br>
        else:<br>
            print("Netinkamas užrašas")<br>
            Game.start()<br>
<br>
<br>
<br>
While, reading from file and writing to file is done with File class:<br>
class File:<br>
    def save_game():<br>
        File1 = open("Lenta.txt", "w")<br>
        File1.write(Lenta.format_lenta(lenta))<br>
        File1.close()<br>
        text = input("Jeigu norite pamatyti ankstesnio žaidimo lentą parašykite 2\nJeigu norite pradėti žaidimą iš naujo parašykite 1\n:")<br>
        if text == "2":<br>
            File.print_saved_game()<br>
        elif text == "1":<br>
            Game.game()<br>
        else:<br>
            print("Netinkamas užrašas")<br>
            File.save_game()<br>
<br>
    def print_saved_game():<br>
        File1 = open("Lenta.txt", "r")<br>
        for i in File1:<br>
            print(i.strip())<br>
        File1.close()<br>
        text = input("Jeigu norite pradėti žaidimą iš naujo parašykite 1\n:")<br>
        if text == "1":<br>
            Game.game()<br>
        else:<br>
            print("Netinkamas užrašas")<br>
            File.print_saved_game()<br>

### Results and summary

In the end, my goal of making moving with coordinates was achieved. The hardest part was making win condition class and implementing it into move method, so that it would check if any player has won after each move.
