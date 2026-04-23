class StakeTransaction:
    def __init__(self, gambler_id, transaction_type, amount, balance_after):
        self.gambler_id = gambler_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance_after = balance_after