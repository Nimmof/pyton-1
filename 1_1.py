duration = 90000
day = duration // 86400
sec_for_hours = duration % 86400
hours = sec_for_hours // 3600
sec_for_min = sec_for_hours - (hours * 3600)
min = sec_for_min // 60
sec = sec_for_min - (min * 60)
if duration >= 90000:
    print(f'{day} дн {hours} час {min} мин {sec} сек')
elif duration >= 3600:
    print(f'{hours} час {min} мин {sec} сек')
elif duration >= 60:
    print(f'{min} мин {sec} сек')
else:
    print(f'{sec} сек')
