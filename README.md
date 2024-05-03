
# Tic-Tac-Toe game

### Introduction

My application is a Tic-Tac-Toe game. To start the program, you have to run the code. To use the program, players will have to write input for every choice of action. In every step of the program there will be instructions explaining your options or telling what to do next. 

### Body/Analysis

I have used inheritance and builder design pattern while coding win condition class:
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



Inheritance was achieved with check_win method:
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

### Results and summary

In the end, my goal of making moving with coordinates was achieved. The hardest part was making win condition class and implementing it into move method, so that it would check if any player has won after each move.
