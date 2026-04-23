class GamblerStatistics:
    def __init__(self, total_bets, total_wins, total_losses, current_stake):
        self.total_bets = total_bets
        self.total_wins = total_wins
        self.total_losses = total_losses
        self.current_stake = current_stake

    def win_rate(self):
        if self.total_bets == 0:
            return 0
        return (self.total_wins / self.total_bets) * 100