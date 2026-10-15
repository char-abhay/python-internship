balance = 1000

while True:

    print("\n----- ATM -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(f"Balance = £{balance}")

    elif choice == "2":
        amount = float(input("Deposit Amount: £"))
        balance += amount
        print("Money Deposited")

    elif choice == "3":
        amount = float(input("Withdraw Amount: £"))

        if amount <= balance:
            balance -= amount
            print("Please collect your cash.")
        else:
            print("Insufficient Balance")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")