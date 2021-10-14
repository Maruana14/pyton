mod = [10, 123.3, 543, 43, 25.2, 253.4, 28, 667, 33.4, 234,
       543, 345.6, 5796, 793, 308, 865, 17, 65, 3.6, 65]


def prices(mod_list):
    for i in mod:
        i = str(i)
        new = i.split('.')
        if len(new) > 1:
            if int(new[1]) < 10:
                new.append('0' + new.pop(1))
        else:
            new.append('00')
        print(f'{new[0]} рублей {new[1]} копеек')


prices(mod)
print('id до сортировки = ', id(mod), '\n')
mod.sort()
print('id после сортировки =', id(mod), '\n')
prices(mod)
mod_decreasing = sorted(mod, reverse=True)
print(mod_decreasing)
mod.reverse()
mod = mod[0:5]
mod.reverse()
prices(mod)
