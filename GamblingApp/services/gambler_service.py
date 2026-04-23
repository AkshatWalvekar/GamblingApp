from repository.gambler_repository import GamblerRepository
from utils.validators import validate_gambler
from models.statistics import GamblerStatistics

class GamblerService:

    def __init__(self):
        self.repo = GamblerRepository()

    def create_gambler(self, gambler):
        validate_gambler(
            gambler.initial_stake,
            gambler.win_threshold,
            gambler.loss_threshold
        )
        self.repo.save(gambler)

    def update_gambler(self, gambler_id, name, email):
        self.repo.update(gambler_id, name, email)

    def get_gambler(self, gambler_id):
        return self.repo.find_by_id(gambler_id)

    def get_statistics(self, gambler_id):
        data = self.repo.find_by_id(gambler_id)

        stats = GamblerStatistics(
            data["total_bets"],
            data["total_wins"],
            data["total_losses"],
            data["current_stake"]
        )

        return {
            "win_rate": stats.win_rate(),
            "current_stake": stats.current_stake
        }

    def validate_gambler(self, gambler_id):
        data = self.repo.find_by_id(gambler_id)

        if data["current_stake"] <= 0:
            return False
        return True

    def reset_gambler(self, gambler_id):
        self.repo.reset(gambler_id)