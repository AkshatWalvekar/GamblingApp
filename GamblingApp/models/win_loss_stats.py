class WinLossStats:
    def __init__(self, bets):
        self.bets = bets

    def total_bets(self):
        return len(self.bets)

    def total_wins(self):
        return sum(1 for b in self.bets if b["win"])

    def total_losses(self):
        return sum(1 for b in self.bets if not b["win"])

    def win_rate(self):
        if self.total_bets() == 0:
            return 0
        return (self.total_wins() / self.total_bets()) * 100

    def net_profit(self):
        profit = 0
        for b in self.bets:
            if b["win"]:
                profit += b["bet_amount"]
            else:
                profit -= b["bet_amount"]
        return profit

    def longest_win_streak(self):
        max_streak = 0
        current = 0

        for b in self.bets:
            if b["win"]:
                current += 1
                max_streak = max(max_streak, current)
            else:
                current = 0

        return max_streak

    def longest_loss_streak(self):
        max_streak = 0
        current = 0

        for b in self.bets:
            if not b["win"]:
                current += 1
                max_streak = max(max_streak, current)
            else:
                current = 0

        return max_streak