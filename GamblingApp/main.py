from models.gambler import Gambler
from services.gambler_service import GamblerService
from services.stake_service import StakeService
from services.betting_service import BettingService
from services.session_service import SessionService
from services.analytics_service import AnalyticsService
from exceptions.custom_exceptions import ValidationException

gambler_service = GamblerService()
stake_service = StakeService()
betting_service = BettingService()
session_service = SessionService()
analytics_service = AnalyticsService()


def menu():
    print("\n===== GAMBLING APP =====")
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
    print("14. View Performance Analytics")


while True:
    menu()
    choice = input("Enter choice: ")

    try:
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            stake = float(input("Enter initial stake: "))
            win = float(input("Enter win threshold: "))
            loss = float(input("Enter loss threshold: "))

            g = Gambler(name, email, stake, win, loss)
            gambler_service.create_gambler(g)

            print(" Gambler Created Successfully")

        elif choice == "2":
            gid = int(input("Enter gambler ID: "))
            data = gambler_service.get_gambler(gid)

            if data:
                print("\n--- Gambler Details ---")
                for k, v in data.items():
                    print(f"{k}: {v}")
            else:
                print(" Gambler not found")

        elif choice == "3":
            gid = int(input("Enter gambler ID: "))
            name = input("Enter new name: ")
            email = input("Enter new email: ")

            gambler_service.update_gambler(gid, name, email)
            print(" Updated successfully")

        elif choice == "4":
            gid = int(input("Enter gambler ID: "))
            stats = gambler_service.get_statistics(gid)

            print("\n--- Statistics ---")
            print(f"Current Stake: {stats['current_stake']}")
            print(f"Win Rate: {stats['win_rate']:.2f}%")

        elif choice == "5":
            gid = int(input("Enter gambler ID: "))
            result = gambler_service.validate_gambler(gid)

            print("Eligible" if result else "Not Eligible")

        elif choice == "6":
            gid = int(input("Enter gambler ID: "))
            gambler_service.reset_gambler(gid)
            print(" Gambler Reset Done")

        elif choice == "7":
            print(" Exiting Application...")
            break

        elif choice == "8":
            gid = int(input("Enter gambler ID: "))
            amount = float(input("Enter deposit amount: "))
            stake_service.deposit(gid, amount)

        elif choice == "9":
            gid = int(input("Enter gambler ID: "))
            amount = float(input("Enter withdraw amount: "))
            stake_service.withdraw(gid, amount)

        elif choice == "10":
            gid = int(input("Enter gambler ID: "))
            print("\n--- Transaction History ---")
            stake_service.get_history(gid)

        elif choice == "11":
            gid = int(input("Enter gambler ID: "))
            amount = float(input("Enter bet amount: "))
            prob = float(input("Enter win probability (0-1): "))
            betting_service.place_bet(gid, amount, prob)

        elif choice == "12":
            gid = int(input("Enter gambler ID: "))
            session_service.start_session(gid)

        elif choice == "13":
            gid = int(input("Enter gambler ID: "))
            bet_amount = float(input("Enter bet amount: "))
            prob = float(input("Enter win probability (0-1): "))
            session_service.play_session(gid, bet_amount, prob)

        elif choice == "14":
            gid = int(input("Enter gambler ID: "))
            result = analytics_service.get_full_analysis(gid)

            print("\n===== ANALYTICS =====")
            print(f"Total Bets: {result['total_bets']}")
            print(f"Wins: {result['wins']}")
            print(f"Losses: {result['losses']}")
            print(f"Win Rate: {result['win_rate']:.2f}%")
            print(f"Net Profit: {result['net_profit']}")
            print(f"Longest Win Streak: {result['longest_win_streak']}")
            print(f"Longest Loss Streak: {result['longest_loss_streak']}")

        else:
            print(" Invalid choice. Try again.")

    except ValidationException as ve:
        print(" Validation Error:", ve)

    except Exception as e:
        print(" System Error:", e)