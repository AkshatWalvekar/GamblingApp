from repository.stake_repository import StakeRepository
from utils.stake_validator import validate_stake_amount
from models.stake_transactions import StakeTransaction
from repository.gambler_repository import GamblerRepository


class StakeService:

    def __init__(self):
        self.repo = StakeRepository()
        self.gambler_repo = GamblerRepository()

    # Add money
    def deposit(self, gambler_id, amount):
        validate_stake_amount(amount)

        gambler = self.gambler_repo.find_by_id(gambler_id)
        new_balance = gambler["current_stake"] + amount

        self.repo.update_balance(gambler_id, new_balance)

        tx = StakeTransaction(gambler_id, "DEPOSIT", amount, new_balance)
        self.repo.add_transaction(tx)

        print(" Deposit successful")

    # Withdraw money
    def withdraw(self, gambler_id, amount):
        validate_stake_amount(amount)

        gambler = self.gambler_repo.find_by_id(gambler_id)

        if gambler["current_stake"] < amount:
            raise ValueError("Insufficient balance")

        new_balance = gambler["current_stake"] - amount

        self.repo.update_balance(gambler_id, new_balance)

        tx = StakeTransaction(gambler_id, "WITHDRAW", amount, new_balance)
        self.repo.add_transaction(tx)

        print(" Withdrawal successful")

    # Check boundary
    def check_limits(self, gambler_id):
        gambler = self.gambler_repo.find_by_id(gambler_id)

        if gambler["current_stake"] >= gambler["win_threshold"]:
            print(" Win limit reached!")

        elif gambler["current_stake"] <= gambler["loss_threshold"]:
            print(" Loss limit reached!")

    # Transaction history
    def get_history(self, gambler_id):
        transactions = self.repo.get_transactions(gambler_id)

        for tx in transactions:
            print(tx)