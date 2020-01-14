import unittest
import tictactoe


class TestTicTacToe(unittest.TestCase):
    def test_player_input(self):
        """
        TEST: when player 1 chooses X
        """
        var = tictactoe.player_input()
        self.assertEqual(var, ('X', 'O'))

    def test_player_input_player2(self):
        """
        TEST: when player 1 chooses O
        """
        var = tictactoe.player_input()
        self.assertEqual(var, ('O', 'X'))

    def test_full_board_true(self):
        """
        TEST: when game board is full
        """
        test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        var = tictactoe.full_board(test_board)
        self.assertEqual(var, True)

    def test_full_board_false(self):
        """
        TEST: when game board is not full
        """
        test_board = [' ' for x in range(10)]
        var = tictactoe.full_board(test_board)
        self.assertEqual(var, False)


if __name__ == '__main__':
    unittest.main()
