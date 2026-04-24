from repository.stake_repository import StakeRepository
from repository.gambler_repository import GamblerRepository
from models.stake_transactions import StakeTransaction
from utils.input_validator import InputValidator

class StakeService:

    def __init__(self):
        self.repo = StakeRepository()
        self.gambler_repo = GamblerRepository()

    def deposit(self, gambler_id, amount):
        InputValidator.validate_stake(amount)

        gambler = self.gambler_repo.find_by_id(gambler_id)
        new_balance = gambler["current_stake"] + amount

        self.repo.update_balance(gambler_id, new_balance)

        tx = StakeTransaction(gambler_id, "DEPOSIT", amount, new_balance)
        self.repo.add_transaction(tx)

        print(" Deposit successful")

    def withdraw(self, gambler_id, amount):
        gambler = self.gambler_repo.find_by_id(gambler_id)

        InputValidator.validate_stake(amount)
        InputValidator.validate_bet_amount(amount, gambler["current_stake"])

        new_balance = gambler["current_stake"] - amount

        self.repo.update_balance(gambler_id, new_balance)

        tx = StakeTransaction(gambler_id, "WITHDRAW", amount, new_balance)
        self.repo.add_transaction(tx)

        print(" Withdrawal successful")

    def check_limits(self, gambler_id):
        gambler = self.gambler_repo.find_by_id(gambler_id)

        if gambler["current_stake"] >= gambler["win_threshold"]:
            print(" Win limit reached!")

        elif gambler["current_stake"] <= gambler["loss_threshold"]:
            print(" Loss limit reached!")

    def get_history(self, gambler_id):
        transactions = self.repo.get_transactions(gambler_id)

        for tx in transactions:
            print(f"{tx['transaction_type']} | Amount: {tx['amount']} | Balance: {tx['balance_after']}")