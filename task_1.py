from datetime import datetime

def get_days_from_today(date_input:str):
    curent_date = datetime.now().date()
    try:
        date_today = datetime.strptime(date_input, '%Y-%m-%d').date()
    except ValueError:
        print(f'{date_input} does not match forma, must be "YYYY-MM-DD"')
    except UnboundLocalError:
        print(f"{date_input} is not corect")
    days = (date_today - curent_date).days
    return days

print(get_days_from_today('2020-10-01'))