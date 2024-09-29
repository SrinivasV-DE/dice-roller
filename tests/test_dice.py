# tests/test_dice.py
from dic_roller.dice import Dice


class TestDice():
    def test_one_roll(self):
        dice = Dice()
        roll = dice.roll()
        assert isinstance(roll, int)
        assert roll > 0
        assert roll < 7