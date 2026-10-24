from datetime import datetime, date, timedelta

def get_upcoming_birthdays(persons: list[dict[str, any]]) -> list[dict[str, any]]:
    new_list = []

    current_date = date.today()
    for person in persons:
        
        persons_birthday = datetime.strptime(person["birthday"], "%Y.%m.%d").date()

        birthday_this_year = persons_birthday.replace(year=current_date.year)
        
        #Checking if birthday already passed
        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year=current_date.year+1)
            
            
        
        #Here we are calcucating the difference between current date and birthday date this year
        difference = birthday_this_year - current_date
        days_until = difference.days


        #Here we are checking if birthday is in range of 7 days
        if days_until in range(0,7):
            if birthday_this_year.weekday() == 5 :
                birthday_this_year = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                birthday_this_year = birthday_this_year + timedelta(days=1)


            dict_for_congrats = {"name": person["name"],
                                  "congraturation_date": birthday_this_year.strftime("%Y.%m.%d")}

            new_list.append(dict_for_congrats) ## appending list with a dictionarries with the name and date to congrat

    return new_list


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jonatan Smith", "birthday": "1990.10.23"},
    {"name": "Kevin", "birthday": "1990.01.03"}

]

new_list = get_upcoming_birthdays(users)

print(new_list)
