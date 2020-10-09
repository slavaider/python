import time
import concurrent.futures


def div(divisor, limit):
    print(f"start {divisor}")
    result = 0
    for x in range(1, limit):
        if x % divisor == 0:
            result += x
            print(f'{divisor=} and {x=}')
        time.sleep(0.2)
    print('raise exception', end='\n')
    raise Exception('lol')
    return result


# if __name__ == '__main__':
#     print('main start')
#     with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
#         future = executor.submit(div, 3, 15)
#         time.sleep(5)
#         try:
#             res = future.result()
#         except Exception as ex:
#             print(repr(ex))
#     print('main end')

if __name__ == '__main__':
    print('main start')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        res_list = executor.map(div, (3, 15), (15, 25))
        while res_list:
            try:
                res = next(res_list)
            except StopIteration:
                print('stop')
                break
            except Exception as ex:
                print(repr(ex))
    print('main end')
