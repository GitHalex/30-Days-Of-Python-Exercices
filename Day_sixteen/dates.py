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
print("##############Nuevo año###################")
new_year = datetime(2020, 1, 1)
print(new_year)
dia = new_year.day
mes = new_year.month
print(dia, mes)
print("#######33esto es con la funciones strftime#############3")
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)