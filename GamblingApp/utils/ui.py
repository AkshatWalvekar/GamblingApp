class UI:

    @staticmethod
    def display_menu():
        print("\n" + "=" * 40)
        print(" GAMBLING APP MENU")
        print("=" * 40)
        print("1. Create Gambler")
        print("2. View Gambler")
        print("3. Update Gambler")
        print("4. View Statistics")
        print("5. Validate Gambler")
        print("6. Reset Gambler")
        print("7. Exit")
        print("8. Deposit")
        print("9. Withdraw")
        print("10. Transaction History")
        print("11. Place Bet")
        print("12. Start Session")
        print("13. Auto Play Session")
        print("14. View Analytics")
        print("=" * 40)

    @staticmethod
    def display_gambler(data):
        print("\n===== GAMBLER DETAILS =====")
        for k, v in data.items():
            print(f"{k}: {v}")

    @staticmethod
    def display_statistics(stats):
        print("\n===== STATISTICS =====")
        print(f"Current Stake: {stats['current_stake']}")
        print(f"Win Rate: {stats['win_rate']:.2f}%")

    @staticmethod
    def display_transactions(transactions):
        print("\n===== TRANSACTION HISTORY =====")
        for tx in transactions:
            print(f"{tx['transaction_type']} | Amount: {tx['amount']} | Balance: {tx['balance_after']}")

    @staticmethod
    def display_analytics(result):
        print("\n===== ANALYTICS =====")
        print(f"Total Bets: {result['total_bets']}")
        print(f"Wins: {result['wins']}")
        print(f"Losses: {result['losses']}")
        print(f"Win Rate: {result['win_rate']:.2f}%")
        print(f"Net Profit: {result['net_profit']}")
        print(f"Longest Win Streak: {result['longest_win_streak']}")
        print(f"Longest Loss Streak: {result['longest_loss_streak']}")