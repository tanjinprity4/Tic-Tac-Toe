class Player():
    def __init__(self, x_or_o, player_num, arr):
        self.x_or_o = x_or_o
        self.player_num = player_num
        print("Enter a number from 0 to 9 according to the board:")
        self.print_board(arr)
        
    def print_board(self,array):
        for i in array:
            for j in i:
                print(j, end=" |")
            print()
        print()
        
    def move(self, array, arr_filled):
        str_pos = input("Player " + str(self.player_num) + ": ")
        int_pos = int(str_pos)
        while is_full(arr_filled, int_pos):
            print("The position is taken, enter again!")
            str_pos = input("Player " + str(self.player_num) + ": ")
            int_pos = int(str_pos)
        for i in range(0,3):
            for j in range(0,3):
                if array[i][j] == str_pos:
                    int_posR = i
                    int_posC = j
                    array[int_posR].pop(int_posC)
                    array[int_posR].insert(int_posC, self.x_or_o)
                    arr_filled.append(int_pos)
                    self.print_board(array)
                    break
        
    
    def check_for_winner(self,array):
        bool_winner = False
        for i in range(0,3):
            if array[i][0] == array[i][1] == array [i][2] == self.x_or_o: 
                bool_winner = True
                break
        if array[0][0]== array[1][0] == array [2][0] == self.x_or_o:
            bool_winner = True
            
        elif array[0][1]== array[1][1] == array [2][1] == self.x_or_o:
            bool_winner = True
            
        elif array[0][2]== array[1][2] == array [2][2] == self.x_or_o:
            bool_winner = True
            
        elif array[0][0]== array[1][1] == array [2][2] == self.x_or_o:
            bool_winner = True
            
        elif array[0][2]== array[1][1] == array [2][0] == self.x_or_o:
            bool_winner = True
        return bool_winner
        

        
def is_full(arr_filled, int_pos):
    bool_full = False
    for i in range(len(arr_filled)):
        if arr_filled[i] == int_pos:
            bool_full = True
    return bool_full
    
def run():
    array = [["1","2","3"],["4","5","6"],["7","8","9"]]
    arr_filled = []
    print("Player 1: x or o?")
    x_or_o = input()
    while x_or_o!= "x" and x_or_o !="o":
        x_or_o = input("Enter x_or_o for player 1: ")
    player1 = Player(x_or_o, 1, array)
    player1.move(array, arr_filled)
    if x_or_o == "x":
        print("Player 2 is o")
        player2 =  Player("o", 2, array)
    else:
        print("Player 2 is x")
        player2 =  Player("x", 2, array)
    while len(arr_filled) < 8:
        player2.move(array, arr_filled)
        if player2.check_for_winner(array) == True:
            print("Winner: Player 2!" )
            break
        player1.move(array, arr_filled)
        if player1.check_for_winner(array) == True:
            print("Winner: Player 1!")
            break
    if player1.check_for_winner(array) == False and player2.check_for_winner(array) == False:
        print("No winner!!")
        
if __name__ == "__main__":
    run()
