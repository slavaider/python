if __name__ == '__main__':
    student1 = {'first_name': 'student', 'last_name': '1', 'bal': 1}
    student2 = {'first_name': 'student', 'last_name': '2', 'bal': 3}
    student3 = {'first_name': 'student', 'last_name': '3', 'bal': 2}
    list_items = [student1, student2, student3]
    res_sum = sum([i['bal'] for i in list_items]) / len(list_items)
    for i in list_items:
        if i['bal'] >= res_sum:
            print(i['first_name'], i['last_name'], i['bal'], '- Выше среднего')
        else:
            print(i['first_name'], i['last_name'], i['bal'], '- Ниже среднего')
