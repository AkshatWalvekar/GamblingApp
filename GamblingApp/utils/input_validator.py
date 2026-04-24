from exceptions.custom_exceptions import *

class InputValidator:

    @staticmethod
    def validate_stake(stake):
        if stake <= 0:
            raise StakeValidationException("Stake must be positive")

    @staticmethod
    def validate_bet_amount(amount, current_stake):
        if amount <= 0:
            raise BetValidationException("Bet must be positive")

        if amount > current_stake:
            raise BetValidationException("Bet exceeds current stake")

    @staticmethod
    def validate_limits(stake, win, loss):
        if win <= stake:
            raise LimitValidationException("Win threshold must be greater than stake")

        if loss >= stake:
            raise LimitValidationException("Loss threshold must be less than stake")

    @staticmethod
    def validate_probability(prob):
        if prob < 0 or prob > 1:
            raise ProbabilityValidationException("Probability must be between 0 and 1")