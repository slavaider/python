def search4vowels(phrase: str) -> set:
    """Выводит гласные в слове"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Ищет буквы из letters в phrase"""
    return set(sorted(set(letters).intersection(set(phrase))))  # извращенец


if __name__ == '__main__':
    print(search4vowels(input('word = ')))
    print(search4letters(letters='xyz', phrase='galaxy'))