import random

if __name__ == '__main__':
    def rand_array(array, start_value, end_value):
        for i in range(len(array)):
            array[i] = random.randint(start_value, end_value)


    a = [0] * 10
    start = -1
    end = 10
    rand_array(a, start, end)
    print(a)
