from datetime import datetime

def get_birthday_day():
    print("Welcome to 'Find My Birthday Day'!")
    
    while True:
        try:
            date_input = input("Enter your birthdate (YYYY-MM-DD): ")
            birthday = datetime.strptime(date_input, "%Y-%m-%d")
            day_of_week = birthday.strftime("%A")
            print(f"You were born on a {day_of_week}!")
            
            another_try = input("Would you like to try another date? (yes/no): ").strip().lower()
            if another_try != 'yes':
                print("Thank you for using 'Find My Birthday Day'! Goodbye!")
                break
        except ValueError:
            print("Invalid date format! Please enter the date in YYYY-MM-DD format.")

# Run the program
if __name__ == "__main__":
    get_birthday_day()