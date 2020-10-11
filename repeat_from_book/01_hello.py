from datetime import datetime
import os as o
import sys as s
# noinspection PyCompatibility
import html
import time
import random
import pprint

if __name__ == '__main__':
    # hello world?
    # times = 5
    # odds = [i for i in range(1, 60) if i % 2 == 1]
    # for i in range(5):
    #     time.sleep(random.randint(1, 3))
    #     right = datetime.today().minute
    #     if right in odds:
    #         print('odd minute')
    #     else:
    #         print('not odd minute')

    # play with os
    print(o.getcwd())
    print(type(o.environ))
    a = dict(o.environ)
    pprint.pprint(a)
    print(f'NUMBER_OF_PROCESSORS:{o.getenv("NUMBER_OF_PROCESSORS")}')
    print(f'{s.platform} and {s.version}')
    print(datetime.date(datetime.today()).isoformat())
    # HTML first interception
    print(html.escape('1) <script></script>'))
    print(html.unescape('2) &hearts;'))
