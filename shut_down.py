while True:
    choice = input("Do you want to continue? (yes/no): ").lower()
    
    if choice == 'no':
        print("closing!")
        break 
    elif choice == 'yes':
        print("Continuing...")
    else:
        print("Please enter 'yes' or 'no'")