from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """creating a tuple for greetings for the week"""
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            continue
        birthday_this_week = birthday_this_year - today
        # check on a working or weekend birthday
        if 0 <= birthday_this_week.days <= 7:
            # check if working
            if birthday_this_year.isoweekday() < 6:
                # add a tuple with the name and date of the greeting to the list
                upcoming_birthdays.append(
                    {
                        "name": user["name"],
                        "congratulation_date": datetime.strftime(
                            birthday_this_year, "%Y.%m.%d"
                        ),
                    }
                )
            else:
                # check if saturday
                if birthday_this_year.isoweekday() == 6:
                    birthday_this_year = birthday_this_year + timedelta(days=2)
                    # add a tuple with the name and date of the greeting to the list
                    upcoming_birthdays.append(
                        {
                            "name": user["name"],
                            "congratulation_date": datetime.strftime(
                                birthday_this_year, "%Y.%m.%d"
                            ),
                        }
                    )
                # check if sunday
                elif birthday_this_year.isoweekday() == 7:
                    birthday_this_year = birthday_this_year + timedelta(days=1)
                    # add a tuple with the name and date of the greeting to the list
                    upcoming_birthdays.append(
                        {
                            "name": user["name"],
                            "congratulation_date": datetime.strftime(
                                birthday_this_year, "%Y.%m.%d"
                            ),
                        }
                    )

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.26"},
    {"name": "Nick Darsel", "birthday": "1984.01.28"},
    {"name": "Ethan Williams", "birthday": "1970.01.30"},
    {"name": "Liam Smith", "birthday": "1995.01.20"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("This week's list of greetings:", upcoming_birthdays)
