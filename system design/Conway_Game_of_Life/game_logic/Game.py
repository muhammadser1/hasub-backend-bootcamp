from game_logic.Board import Board
from utils.input_user import *


class Game:
    def __init__(self, ):
        """
        Initializes a new Game object.
        """
        self.board = None

    def start(self):
        """
        Starts the Conway's Game of Life simulation.
        """
        print("\nWelcome to Conway's Game of Life \n")
        # Prompt the user to set the size of the board and number of simulation rounds

        board_size = get_integer_input(msg_to_show="Set the size of the board:")
        simulation_rounds = get_integer_input(msg_to_show="How many rounds do you wish to simulate? ")

        # Initialize the game board and populate it with living cells
        self.board = Board(board_size)
        self.board.populate_living_cells()

        # Start the simulation
        self.simulate(simulation_rounds)

    def simulate(self, simulation_rounds):
        """
        Simulates the game for the specified number of rounds.

        Parameters:
            simulation_rounds (int): Number of rounds to simulate.
        """
        for _ in range(simulation_rounds):
            print("Round:", _ + 1)
            self.board.print_results()
            self.board.update_board()

        print("\nGame completed. Thanks for playing!")
