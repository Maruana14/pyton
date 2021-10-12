one = list(range(21, 92, 10)) + [1]
two = list(range(2, 5))
three = list(range(11, 15))
n = 1
end = n % 10
while n <= 100:
    if n in c:
        print(n, 'процентов')
        n += 1
        end = n % 10
    elif end in d:
        print(n, 'процента')
        n += 1
        end = n % 10
    elif end in a:
        print(n, 'процент')
        n += 1
        end = n % 10
    else:
        print(n, 'процентов')
        n += 1
        end = n % 10
