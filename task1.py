from datetime import datetime

def get_days_from_today(date: str) -> datetime:
    try:
        parsed_date = datetime.strptime(date, '%Y-%m-%d')
            
        todays_date = datetime.today()
            
        date_difference = parsed_date - todays_date
            
        return print(f"Day difference is: {date_difference.days}")
            
    except (ValueError, TypeError):
        return None
            
            
get_days_from_today('2021-01-24')
