EMPTY = 0
RESERVED = 1
def display_menu():
 print("UCC Signature Express Limited")
 print("Reservation Options:")
 print(" First Class (F/f)")
 print(" Business Class (B/b)")
 print(" Economy Class (E/e)")
 print(" Quit or Cancel (Q/q)")
 return input("Please select an option: ").upper()
def make_reservation(class_capacity, seats_array):
 row_number = int(input("Enter the row number: "))
 column_number = int(input("Enter the column number: "))
 if row_number <= 0:
 print("Number must be positive or greater than zero!")
 return
 if seats_array[row_number - 1][column_number - 1] == RESERVED:
 print(f"Seat {row_number} column {column_number} is already reserved. Please 
choose another seat.")
 return
 print(f"Reserving seat: row {row_number} column {column_number}")
 seats_array[row_number - 1][column_number - 1] = RESERVED
def count_reserved_seats(seats_array):
 count = sum(row.count(RESERVED) for row in seats_array)
 return count
def main():
 first_class_seats = [[EMPTY] * 2 for _ in range(27)]
 business_class_seats = [[EMPTY] * 2 for _ in range(38)]
 economy_class_seats = [[EMPTY] * 2 for _ in range(56)]
 while True:
 user_choice = display_menu()
 if user_choice == "F":
 make_reservation(27, first_class_seats)
 elif user_choice == "B":
 make_reservation(38, business_class_seats)
 elif user_choice == "E":
 make_reservation(56, economy_class_seats)
 elif user_choice == "Q":
 print("Reservation Type:")
 print("Total number of seats:", 27 + 38 + 56)
 print("Total number of seats reserved:", count_reserved_seats(first_class_seats) +
 count_reserved_seats(business_class_seats) + 
count_reserved_seats(economy_class_seats))
 print("Goodbye!")
 break
 else:
 print("Invalid choice! Please select a valid option.")
if __name__ == "__main__":
 main()
