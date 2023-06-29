import datetime


def ask_for_date():
    while True:
        try:
            date_input = input("Please enter a date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_input, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format. Please try again.")
