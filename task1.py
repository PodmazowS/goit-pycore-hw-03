from datetime import datetime, date

def get_days_from_today(date: str) -> datetime:
    try:
        parsed_date = datetime.strptime(date, '%Y-%m-%d').date()

        todays_date = datetime.now().date()

        date_difference = todays_date - parsed_date
            
        return date_difference.days
            
    except (ValueError, TypeError):
        return None
            
            
days = get_days_from_today('2021-01-24')

print(days)
