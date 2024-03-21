from datetime import datetime, timedelta
import pytz
IST = pytz.timezone('Asia/Kolkata')
current_time=datetime.now(IST).replace(tzinfo=None)
print(current_time)
current_time =  str(current_time - timedelta(hours=5,minutes=30))
print(current_time)

date_time_start_index = current_time.find('(') + 1
date_time_end_index = current_time.find('.', date_time_start_index)
date_time = current_time[date_time_start_index:date_time_end_index]
print(type(date_time))
date_time = datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S')

print(date_time)