from time import time


def speed_test(func):
    def wrapper():
        start = time()
        func()
        end = time()
        print(f'Function takes {round((end - start),10)}')

    return wrapper
@speed_test
def big_loop():
    for i in range(1, 20000):
        print(i)


big_loop()
