#373
import datetime

total = '1 day, 41:00:00'


total = total.split(' ')[2].split(':')
print(total)

print(datetime.timedelta(minutes=373))