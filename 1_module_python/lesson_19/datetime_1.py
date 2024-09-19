from datetime import datetime, timedelta

current_datetime = datetime.now()
print(type(current_datetime))
print(current_datetime)

yesterday = current_datetime + timedelta(days=1)
print(yesterday)

yesterday_str = datetime.strftime(yesterday, '%Y/%m/%d %H:%M:%S')
print(yesterday_str)
