workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in workers:
    i = i.split(' ')
    print('Привет, ' + i.pop().title() + '!')
