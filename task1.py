from datetime import datetime, timedelta

def get_days_from_today(date):
    current_date = datetime.now().date()
    try: 
        convirted_date = datetime.strptime(date, '%Y-%m-%d').date()
        delta = (current_date - convirted_date).days
        return int(delta)
    except ValueError:
        print("date should be a string in format 'YYYY-MM-DD'")

# test cases block - uncomment 2 last lines to check and compare with expected result
# exp.result: negative int /n positive int /n "date should be a string in format 'YYYY-MM-DD'"
# dates = ["2024-07-10", "2024-06-01", "12:12:2023"]
# for date in dates:
#   print(get_days_from_today(date))