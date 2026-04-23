def validate_gambler(stake, win_threshold, loss_threshold):
    if stake <= 0:
        raise ValueError("Stake must be positive")

    if win_threshold <= stake:
        raise ValueError("Win threshold must be greater than initial stake")

    if loss_threshold >= stake:
        raise ValueError("Loss threshold must be less than initial stake")