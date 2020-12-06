if __name__ == '__main__':
    d1 = {'year': 2003, 'month': 12}
    d2 = {'year': 2014, 'month': 6}
    du = {'year': int(input('Год: ')), 'month': int(input('Месяц: '))}
    if d1['year'] < du['year'] < d2['year']:
        print('Да')
    elif du['year'] == d1['year']:
        if du['month'] >= d1['month']:
            print('Да')
        else:
            print('Нет')
    elif du['year'] == d2['year']:
        if du['month'] <= d2['month']:
            print('Да')
        else:
            print('Нет')
    else:
        print('Нет')
