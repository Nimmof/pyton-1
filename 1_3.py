for i in range(1, 1001):
    number = i
    if number > 20:
        number = number % 10
    if number == 1:
        percent = 'процент'
    elif number > 1 and number < 5:
        percent = 'процента'
    elif number > 4 and number < 20:
        percent = 'процентов'
    print(f'{i} {percent}')
