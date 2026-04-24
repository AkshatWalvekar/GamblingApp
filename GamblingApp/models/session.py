import time

class Session:
    def __init__(self, gambler_id):
        self.gambler_id = gambler_id
        self.start_time = time.time()
        self.games_played = 0
        self.is_active = True

    def end_session(self):
        self.is_active = False
        self.end_time = time.time()

    def duration(self):
        if hasattr(self, "end_time"):
            return self.end_time - self.start_time
        return time.time() - self.start_time