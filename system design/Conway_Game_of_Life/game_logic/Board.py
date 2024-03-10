import copy

from utils.input_user import get_integer_input


class Board:
    def __init__(self, size):
        """
        Initializes a new game board.

        Parameters:
            size (int): The size of the board.
        """
        self.size = size
        self.board = self.init_board()
        self.copy_board = None

    def init_board(self):
        """
        Initializes the board with empty cells.

        Returns:
            list: The initialized board.
        """
        return [[' ' for _ in range(self.size)] for _ in range(self.size)]

    def print_results(self):
        """
        Prints the current state of the board.
        """
        for row in self.board:
            print(row)

    def update_board(self):
        """
        Prints the current state of the board.
        """
        self.copy_board= copy.deepcopy(self.board)
        for i in range(self.size):
            for j in range(self.size):
                count_living_neighbor_i_j = self.count_living_neighbors(i, j)
                if self.copy_board[i][j]=='X':
                    if count_living_neighbor_i_j >=2:
                        pass
                    else:
                        self.board[i][j] = ' '
                else:
                    if count_living_neighbor_i_j >=3:
                        self.board[i][j] = 'X'

    def populate_living_cells(self):
        """
         Allows the user to input the coordinates of living cells on the board.
         """
        print("Please input the coordinates of the living cells.")
        print("Press Enter when you're done.")
        while True:
            row_board = get_integer_input(msg_to_show="Please enter the row number: ", min_value=0,
                                          max_value=self.size - 1)
            col_board = get_integer_input(msg_to_show="Please enter the col number: ", min_value=0,
                                          max_value=self.size - 1)
            if self.board[row_board][col_board] == 'X':
                print("Cell is already occupied by a living cell.")
            else:
                self.board[row_board][col_board] = 'X'  # Set cell as living

            continue_or_not = get_integer_input(
                "You want to continue?\n1. Yes\n2. No\nPlease enter the number corresponding to your choice: ",
                min_value=1, max_value=2)
            if continue_or_not == 2:
                break
            if continue_or_not == 1:
                pass

    def count_living_neighbors(self, row, col):
        """
        Counts the number of living neighbors for a given cell.

        Parameters:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            int: The number of living neighbors.
        """
        # Count the number of living neighbors for the cell at position (row, col)
        living_neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue  # Skip the current cell
                neighbor_row = row + i
                neighbor_col = col + j
                # # Check if the neighbor cell is within the bounds of the board and alive
                if 0 <= neighbor_row < self.size and 0 <= neighbor_col < self.size and self.copy_board[neighbor_row][
                    neighbor_col] == 'X':
                    living_neighbors += 1
        return living_neighbors
