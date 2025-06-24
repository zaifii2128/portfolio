def atm_system():
    correct_pin = "1234"
    balance = 10000  # Initial balance
    
    # Asking for PIN
    pin = input("Enter PIN: ")
    if pin != correct_pin:
        print("Incorrect PIN. Access denied.")
        return
    
    while True:
        # Display menu
        print("\n1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print(f"Your balance is: {balance}")
        
        elif choice == "2":
            amount = int(input("Enter withdrawal amount: "))
            
            if amount > balance:
                print("Insufficient balance.")
            elif amount % 500 != 0:
                print("Amount must be a multiple of 500.")
            else:
                balance -= amount
                print(f"Transaction successful! Remaining balance: {balance}")
        
        elif choice == "3":
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the ATM system
atm_system()
