# Задание 1
duration = int(input())
min = duration // 60
hour = duration // 3600
day = duration // 86400
if duration < 60:
    sec = duration
    print(duration, 'сек')
elif 3600 > duration >=60:
    sec = duration % 60 
    print(min,'мин',sec, 'сек')
elif 86400 > duration >= 3600:
    sec = duration % 60 
    min = min % 60 
    print(hour, 'час', min , 'мин', sec, 'сек')
else:
    sec = duration % 60 
    min = m % 60 
    hour = duration % 86400 // 3600
    print(day, 'дни', hour, 'час', min, 'мин', sec, 'ceк')