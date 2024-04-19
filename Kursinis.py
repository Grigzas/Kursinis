plotis = 3
lenta = [["- ", "- ", "- "], 
         ["- ", "- ", "- "], 
         ["- ", "- ", "- "]]
print("   1   2   3")
for i in range(plotis):
    print(chr(65 + i), end="  ")
    for j in range(plotis):
        print(lenta[i][j], end="  ")
    print()


class Game:
    def __init__(self):
        self.lenta = lenta

    def new_game():
        for i in range(plotis):
            for j in range(plotis):
                lenta[i][j] = "- "
        print("   1   2   3")
        for i in range(plotis):
            print(chr(65 + i), end="  ")
            for j in range(plotis):
                print(lenta[i][j], end="  ")
            print()
            


class Player:
    def  __init__(self):
        self.lenta = lenta

    def move(a, b, c):
        if lenta[a][b] != "- ":
            print("Šis laukelis užimtas, pasirinkite kitą laukelį")
        elif lenta[0][0] == lenta[0][1] and lenta[0][1] == lenta[0][2] and lenta[0][0] != "- ":
            if lenta[0][0] == "X ":
                print("Žaidėjas_X laimėjo")
        else:
            lenta[a][b] = c
            print("   1   2   3")
            for i in range(plotis):
                print(chr(65 + i), end="  ")
                for j in range(plotis):
                    print(lenta[i][j], end="  ")
                print()



#player1 = Player
#player1.move(0, 0, "X ")

#player2 = Player
#player2.move(0, 0, "0 ")
                
game = Game
game.new_game()