import pytest
from unittest.mock import patch
from src.game import Game


class TestGame:
    @pytest.mark.parametrize("value, print, expected",
                            [(1, "you lose", 0), (2, "you lose", 0),
                                (3, "Try again", 1), (4, "Try again", 1),
                                (5, "Try again", 1), (6, "you win", 2)])
    def test_roll_dice_1(self, value, print, expected, capsys):
        with patch("src.game.rnd.randint", autospec=True) as mockrandint:
            mockrandint.return_value = value
            sut = Game()
            assert sut.roll_dice() == expected
            captured = capsys.readouterr()
            assert print in captured.out
