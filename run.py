import random

class GameBoard:
    """
    main board class. sets the size of the board and changes letters to numbers for ease of use
    """
    def __init__(self, board):
        self.board = board

    def get_letters_to_numbers():
        #changes letters to numbers for ease of use
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return letters_to_numbers

    def print_board(self):
        #defines board structure
        print("     A B C D E F G H" )
        print("     ---------------" )
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|" .join(row)))
            row_number +=1

class Battleship:
    """
    creates the number of ships,gets user input, and the miss/hit ships
    """
    def __init(self, board):
        self.board = board

    def create_ships(self):
        #creates 5 ships and places them randomly on the board
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def get_user_input(self):
        #defines user input needed for the game to start
        try:
            x_row = input("Enter the row number of the ship: ")
            while x_row not in '12345678':
                print('not a choice, please select a valid row number')
                x_row = input("Enter the row number of the ship: ") 

            y_column = input("Enter the column letter of the ship: ").upper()
            while y_column not in "ABCDEFGH":
                print('not a choice, please select a valid column letter')
                y_column = input("Enter the column letter of the ship: ").upper()
            return int(x_row) -1, GameBoard.get_letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input")
            return self.get_user_input()

    def count_hit_ships():
        #counts how many ships have been hit
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships +=1

def RunGame():
    #states the introductory information needed to start the game and 
    # sets the board with all the ships waiting to be hit
    input("Welcome to Battleships. \nPress ENTER to start!")
    player1 = input("\nState your name to start\n>")
    while player1 == "":
        player1 = input("\nI didnt get that,please state your name\n>")
    else:
        print(f"\nOk, {player1}, let's begin..\n")
    computer_board = GameBoard([[""] * 8 for i in range(8)])
    user_guess_board = GameBoard([[""] * 8 for in range(8)])
    Battleship.create_ships(computer_board)


                                 
                                   
                           
                        