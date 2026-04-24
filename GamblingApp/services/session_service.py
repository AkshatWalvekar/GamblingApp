import time
from models.session import Session
from services.betting_service import BettingService
from repository.gambler_repository import GamblerRepository

class SessionService:

    def __init__(self):
        self.bet_service = BettingService()
        self.gambler_repo = GamblerRepository()
        self.active_sessions = {}

    # START SESSION
    def start_session(self, gambler_id):
        if gambler_id in self.active_sessions:
            print("⚠️ Session already running")
            return

        session = Session(gambler_id)
        self.active_sessions[gambler_id] = session

        print("▶️ Session started")

    # AUTO PLAY
    def play_session(self, gambler_id, bet_amount, probability=0.5, delay=1):
        if gambler_id not in self.active_sessions:
            print("❌ Start session first")
            return

        session = self.active_sessions[gambler_id]

        while session.is_active:
            gambler = self.gambler_repo.find_by_id(gambler_id)

            # STOP CONDITIONS
            if gambler["current_stake"] >= gambler["win_threshold"]:
                print("🎯 WIN LIMIT REACHED")
                break

            if gambler["current_stake"] <= gambler["loss_threshold"]:
                print("❌ LOSS LIMIT REACHED")
                break

            # PLACE BET
            self.bet_service.place_bet(gambler_id, bet_amount, probability)

            session.games_played += 1

            time.sleep(delay)  # simulate real play

        session.end_session()
        print("⏹️ Session ended")

        self.show_summary(session)

        del self.active_sessions[gambler_id]

    # SUMMARY
    def show_summary(self, session):
        print("\n===== SESSION SUMMARY =====")
        print(f"Gambler ID: {session.gambler_id}")
        print(f"Games Played: {session.games_played}")
        print(f"Duration: {session.duration():.2f} seconds")