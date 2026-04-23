from models.gambler import Gambler
from services.gambler_service import GamblerService

service = GamblerService()

def menu():
    print("\n===== GAMBLING APP =====")
    print("1. Create Gambler")
    print("2. View Gambler")
    print("3. Update Gambler")
    print("4. View Statistics")
    print("5. Validate Gambler")
    print("6. Reset Gambler")
    print("7. Exit")

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
            service.create_gambler(g)
            print(" Gambler Created")

        elif choice == "2":
            gid = int(input("Enter gambler ID: "))
            print(service.get_gambler(gid))

        elif choice == "3":
            gid = int(input("Enter gambler ID: "))
            name = input("New name: ")
            email = input("New email: ")
            service.update_gambler(gid, name, email)
            print(" Updated")

        elif choice == "4":
            gid = int(input("Enter gambler ID: "))
            print(service.get_statistics(gid))

        elif choice == "5":
            gid = int(input("Enter gambler ID: "))
            print("Eligible:", service.validate_gambler(gid))

        elif choice == "6":
            gid = int(input("Enter gambler ID: "))
            service.reset_gambler(gid)
            print(" Reset Done")

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

    except Exception as e:
        print(" Error:", e)