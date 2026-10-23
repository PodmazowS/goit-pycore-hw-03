from datetime import datetime

def get_days_from_today(date: str) -> datetime:
    while True:
        try:
            parsed_date = datetime.strptime(date, '%Y-%m-%d')
            
            todays_date = datetime.today()
            
            date_difference = parsed_date - todays_date
            
            return print(f"Day difference is: {date_difference.days}")
        
            
        except ValueError:
            print("Format isn't correct, please use the following format PPPP-MM-DD")

            date = input("Enter the date in following format(PPPP-MM-DD): ")
            
            
initial_date = input("Enter the date in following format(PPPP-MM-DD): ")

get_days_from_today(initial_date)
