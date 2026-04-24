from repository.bet_repository import BetRepository
from models.win_loss_stats import WinLossStats

class AnalyticsService:

    def __init__(self):
        self.bet_repo = BetRepository()

    def get_full_analysis(self, gambler_id):
        bets = self.bet_repo.get_bets_by_gambler(gambler_id)

        stats = WinLossStats(bets)

        return {
            "total_bets": stats.total_bets(),
            "wins": stats.total_wins(),
            "losses": stats.total_losses(),
            "win_rate": stats.win_rate(),
            "net_profit": stats.net_profit(),
            "longest_win_streak": stats.longest_win_streak(),
            "longest_loss_streak": stats.longest_loss_streak()
        }