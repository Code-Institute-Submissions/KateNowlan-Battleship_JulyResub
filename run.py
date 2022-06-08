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
                        