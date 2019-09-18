'''
SI 507 Fall 2018 Homework 1
'''

# Create board - Setup the data structure for storing board data
# print the inital board
print("CURRENT BOARD:")
print("   |   |")
print("-----------")
print("   |   |")
print("-----------")
print("   |   |")

board=[] #board is a data structure that consists of nine elements, each element is "" or "X" or "O"
# Nine elements are stored from left to right line by line

cell_info=[] #cell_info is a data structure that consists of two elements: cell_letter and cell_location

# Loop until game is over
    
    # Step 1: Print board
    '''
    This function will take in current board data and print out the board in the console as shown 
    in the instructions.
    parameter: board_data - a data structure used for holding current moves on the board
    return: None
    '''
    def print_board(board_data):
        pass

    # Step 2: 
    '''
    This function will get the information of the next cell 
    parameter: input_str - an input string (e.g. "O's move > NE")
    return: cell_info - a data structure composed of two elements: cell_letter (e.g. "O") and cell_location (e.g. NE)
    '''
    def get_information(input_str):
        pass

    # Step 3:
    '''
    This function will check whether the next cell to be moved into is empty
    parameter: cell_location - a data structure used for holding the location of next cell. board_data - a data structure used for holding current moves on the board
    return: true or false
    '''
    def check_empty(cell_location, board_data):
        pass

    # Step 4:
    '''
    This function will update the board after something was moved into a cell
    parameter: cell_info - a data structure used for holding the letter and location of the latest moved cell.
    return: None
    '''
    def update_board(cell_info):
        pass

    # Step 5: Determine if game is over
    '''
    Take in the current board data and determine if one player wins the game or the game draws. If the game is over,
    terminate the loop, or continue the loop.
    parameter: board_data - current board data
    return: information about current game status
    '''

    def determine_over(board_data):
        pass
