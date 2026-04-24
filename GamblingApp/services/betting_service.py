import random
from repository.bet_repository import BetRepository
from repository.gambler_repository import GamblerRepository
from repository.stake_repository import StakeRepository
from models.bet import Bet

class BettingService:

    def __init__(self):
        self.bet_repo = BetRepository()
        self.gambler_repo = GamblerRepository()
        self.stake_repo = StakeRepository()

    def place_bet(self, gambler_id, amount, win_probability=0.5):

        gambler = self.gambler_repo.find_by_id(gambler_id)

        if not gambler:
            raise ValueError("Gambler not found")

        if amount > gambler["current_stake"]:
            raise ValueError("Insufficient balance")

        stake_before = gambler["current_stake"]

        # 🎲 Determine win/loss
        win = random.random() < win_probability

        if win:
            stake_after = stake_before + amount
            print("🎉 You WON!")
        else:
            stake_after = stake_before - amount
            print("💔 You LOST!")

        # Update stake
        self.stake_repo.update_balance(gambler_id, stake_after)

        # Save bet
        bet = Bet(gambler_id, amount, win, stake_before, stake_after)
        self.bet_repo.save(bet)

        print(f"💰 New Balance: {stake_after}")

        return win