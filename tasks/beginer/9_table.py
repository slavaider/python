if __name__ == '__main__':
    # y = -0.23x2 + x
    min = float(input('min='))
    max = float(input('max='))
    step = float(input('step='))
    while min < max + 1:
        print(f'x = {min}', 'y = ', f'{(-0.23 * (min ** 2) + min):5.2f}')
        min += step
