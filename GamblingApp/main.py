from models.gambler import Gambler
from services.gambler_service import GamblerService
from services.stake_service import StakeService

gambler_service = GamblerService()
stake_service = StakeService()


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


while True:
    menu()
    choice = input("Enter choice: ")

    try:
        # 1. Create
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            stake = float(input("Enter initial stake: "))
            win = float(input("Enter win threshold: "))
            loss = float(input("Enter loss threshold: "))

            g = Gambler(name, email, stake, win, loss)
            gambler_service.create_gambler(g)

            print(" Gambler Created Successfully")

        # 2. View
        elif choice == "2":
            gid = int(input("Enter gambler ID: "))
            data = gambler_service.get_gambler(gid)

            if data:
                print("\n--- Gambler Details ---")
                for k, v in data.items():
                    print(f"{k}: {v}")
            else:
                print(" Gambler not found")

        # 3. Update
        elif choice == "3":
            gid = int(input("Enter gambler ID: "))
            name = input("Enter new name: ")
            email = input("Enter new email: ")

            gambler_service.update_gambler(gid, name, email)
            print(" Updated successfully")

        # 4. Statistics
        elif choice == "4":
            gid = int(input("Enter gambler ID: "))
            stats = gambler_service.get_statistics(gid)

            print("\n--- Statistics ---")
            print(f"Current Stake: {stats['current_stake']}")
            print(f"Win Rate: {stats['win_rate']:.2f}%")

        # 5. Validate
        elif choice == "5":
            gid = int(input("Enter gambler ID: "))
            result = gambler_service.validate_gambler(gid)

            print("Eligible:" if result else "Not Eligible")

        # 6. Reset
        elif choice == "6":
            gid = int(input("Enter gambler ID: "))
            gambler_service.reset_gambler(gid)
            print(" Gambler Reset Done")

        # 7. Exit
        elif choice == "7":
            print(" Exiting Application...")
            break

        # 8. Deposit
        elif choice == "8":
            gid = int(input("Enter gambler ID: "))
            amount = float(input("Enter deposit amount: "))

            stake_service.deposit(gid, amount)

        # 9. Withdraw
        elif choice == "9":
            gid = int(input("Enter gambler ID: "))
            amount = float(input("Enter withdraw amount: "))

            stake_service.withdraw(gid, amount)

        # 10. History
        elif choice == "10":
            gid = int(input("Enter gambler ID: "))
            print("\n--- Transaction History ---")
            stake_service.get_history(gid)

        else:
            print(" Invalid choice. Try again.")

    except Exception as e:
        print(" Error:", e)