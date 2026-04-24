from models.gambler import Gambler
from services.gambler_service import GamblerService
from services.stake_service import StakeService
from services.betting_service import BettingService
from services.session_service import SessionService
from services.analytics_service import AnalyticsService
from exceptions.custom_exceptions import ValidationException
from utils.ui import UI

gambler_service = GamblerService()
stake_service = StakeService()
betting_service = BettingService()
session_service = SessionService()
analytics_service = AnalyticsService()


while True:
    UI.display_menu()
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

            print(" Gambler Created")

        elif choice == "2":
            gid = int(input("Enter gambler ID: "))
            data = gambler_service.get_gambler(gid)

            if data:
                UI.display_gambler(data)
            else:
                print(" Gambler not found")

        elif choice == "3":
            gid = int(input("Enter gambler ID: "))
            name = input("New name: ")
            email = input("New email: ")

            gambler_service.update_gambler(gid, name, email)
            print(" Updated")

        elif choice == "4":
            gid = int(input("Enter gambler ID: "))
            stats = gambler_service.get_statistics(gid)
            UI.display_statistics(stats)

        elif choice == "5":
            gid = int(input("Enter gambler ID: "))
            result = gambler_service.validate_gambler(gid)
            print("Eligible" if result else "Not Eligible")

        elif choice == "6":
            gid = int(input("Enter gambler ID: "))
            gambler_service.reset_gambler(gid)
            print(" Reset Done")

        elif choice == "7":
            print(" Exiting...")
            break

        elif choice == "8":
            gid = int(input("Enter gambler ID: "))
            amt = float(input("Enter amount: "))
            stake_service.deposit(gid, amt)

        elif choice == "9":
            gid = int(input("Enter gambler ID: "))
            amt = float(input("Enter amount: "))
            stake_service.withdraw(gid, amt)

        elif choice == "10":
            gid = int(input("Enter gambler ID: "))
            transactions = stake_service.repo.get_transactions(gid)
            UI.display_transactions(transactions)

        elif choice == "11":
            gid = int(input("Enter gambler ID: "))
            amt = float(input("Enter bet amount: "))
            prob = float(input("Enter probability (0-1): "))

            betting_service.place_bet(gid, amt, prob)

        elif choice == "12":
            gid = int(input("Enter gambler ID: "))
            session_service.start_session(gid)

        elif choice == "13":
            gid = int(input("Enter gambler ID: "))
            amt = float(input("Enter bet amount: "))
            prob = float(input("Enter probability (0-1): "))

            session_service.play_session(gid, amt, prob)

        elif choice == "14":
            gid = int(input("Enter gambler ID: "))
            result = analytics_service.get_full_analysis(gid)
            UI.display_analytics(result)

        else:
            print(" Invalid choice")

    except ValidationException as ve:
        print(" Validation Error:", ve)

    except Exception as e:
        print(" System Error:", e)