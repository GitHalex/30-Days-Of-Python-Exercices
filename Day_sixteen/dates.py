from datetime import datetime
now = datetime.now()
print(now)                      # 2024-07-08 07:34:46.549883
day = now.day                   # 18
month = now.month               # 8
year = now.year                 # 2024
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38