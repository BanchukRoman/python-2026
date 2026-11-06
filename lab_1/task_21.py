import time as t

def timing(func):
    def wrapper():
        start = t.perf_counter()
        func()
        stop = t.perf_counter()
        print(f'Время выполнения {(stop - start) * 1000} ms')
    return wrapper
@timing
def function():
    text = input('Введите ваш текст: ')
    print(f'{text}\n' * 100)

function()