#menu.py
from waitlist import WaitList
def main():
    waitlist = WaitList()
    while True:
        print("""
        Welcome to the Restaurant Reservation System!
        ==========================3=================
        Please select an option:
        1. Add a customer to the waitlist
        2. Seat the next customer
        3. Change the time of a customer's reservation
        4. Peek at the next customer
        5. Print the reservation list
        6. Quit
        """)
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            name = input("Enter the customer's name: ")
            time = input("Enter the time of the reservation (HH:MM): ")
            waitlist.add_customer(name, time)
        elif choice == '2':
            waitlist.seat_customer()
        elif choice == '3':
            name = input("Enter the customer's name to change the reservation: ")
            old_time = input("Enter the old time of the reservation (HH:MM): ")
            new_time = input("Enter the new time of the reservation (HH:MM): ")
            waitlist.change_reservation(name, old_time, new_time)
        elif choice == '4':
            message = waitlist.peek_next_customer()
            print(message)
        elif choice == '5':
            waitlist.print_reservation_list()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()