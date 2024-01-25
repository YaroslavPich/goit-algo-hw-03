from datetime import datetime


def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return "error"
    current_date = datetime.today().date()
    diff_date = current_date - date
    return diff_date.days


date = input("Enter a date to calculate the difference of days 'YYYY-MM-DD': ")

while get_days_from_today(date) == "error":
    print("Incorrect data entry!")
    date = input("Enter a date of format 'YYYY-MM-DD': ")
else:
    if get_days_from_today(date) == 1 or get_days_from_today(date) == -1:
        print(f"The difference is: {get_days_from_today(date)} day")
    else:
        print(f"The difference is: {get_days_from_today(date)} days")
