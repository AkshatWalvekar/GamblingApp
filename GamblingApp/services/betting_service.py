import random
from repository.bet_repository import BetRepository
from repository.gambler_repository import GamblerRepository
from repository.stake_repository import StakeRepository
from models.bet import Bet
from utils.input_validator import InputValidator

class BettingService:

    def __init__(self):
        self.bet_repo = BetRepository()
        self.gambler_repo = GamblerRepository()
        self.stake_repo = StakeRepository()

    def place_bet(self, gambler_id, amount, win_probability=0.5):

        gambler = self.gambler_repo.find_by_id(gambler_id)

        if not gambler:
            raise ValueError("Gambler not found")

        InputValidator.validate_bet_amount(amount, gambler["current_stake"])
        InputValidator.validate_probability(win_probability)

        stake_before = gambler["current_stake"]

        win = random.random() < win_probability

        if win:
            stake_after = stake_before + amount
            print(" You WON!")
        else:
            stake_after = stake_before - amount
            print(" You LOST!")

        self.stake_repo.update_balance(gambler_id, stake_after)

        bet = Bet(gambler_id, amount, win, stake_before, stake_after)
        self.bet_repo.save(bet)

        print(f" New Balance: {stake_after}")

        return win