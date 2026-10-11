guests = {}

def check_in():
    name = input("Enter guest name: ")
    room_no = input("Enter room number: ")
    days = int(input("Number of days staying: "))
    rate = float(input("Rate per day: "))
    total_bill = days * rate
    guests[room_no] = {'Name': name, 'Days': days, 'Rate': rate, 'Total': total_bill}
    print(f"\n{name} checked into Room {room_no}. Total Bill: ₹{total_bill:.2f}\n")

def check_out():
    room_no = input("Enter room number to check out: ")
    if room_no in guests:
        print(f"\nGuest {guests[room_no]['Name']} checked out. Bill: ₹{guests[room_no]['Total']:.2f}\n")
        del guests[room_no]
    else:
        print("No guest found in that room.\n")

def view_guests():
    if not guests:
        print("No current guests.\n")
        return
    print("\nCurrent Guests:")
    for room, info in guests.items():
        print(f"Room {room}: {info['Name']} - ₹{info['Total']:.2f}")
    print()

def main():
    while True:
        print("------ Hospitality Management ------")
        print("1. Check-in")
        print("2. Check-out")
        print("3. View Guests")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            check_in()
        elif choice == '2':
            check_out()
        elif choice == '3':
            view_guests()
        elif choice == '4':
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
