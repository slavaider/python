import pprint

if __name__ == '__main__':
    people = {'Ford': {
        'Name': 'Ford',
        'Gender': 'Male',
        'Occupation': 'Researcher',
        'Home Planet': 'Betelgeuse Seven'
    }, 'Arthur': {
        'Name': 'Arthur Dent',
        'Gender': 'Male',
        'Occupation': 'Sandwich-maker',
        'Home Planet': 'Earth'
    }, 'Tristan': {
        'Name': 'Tristan McMilan',
        'Gender': 'Female',
        'Occupation': 'Mathematical',
        'Home Planet': 'Earth'
    }, 'Robot': {
        'Name': 'Marvin',
        'Gender': 'Unknown',
        'Occupation': 'Paranoid Android',
        'Home Planet': 'Unknown'
    }}
    pprint.pprint(people)
