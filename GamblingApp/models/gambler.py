class Gambler:
    def __init__(self, name, email, initial_stake, win_threshold, loss_threshold):
        self.name = name
        self.email = email
        self.initial_stake = initial_stake
        self.current_stake = initial_stake
        self.win_threshold = win_threshold
        self.loss_threshold = loss_threshold