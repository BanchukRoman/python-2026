import inspect
import time as t


def log_calls(func):
    def wrapper(word):
        file = open('text.txt', 'w')
        file.write(f'{t.ctime()}\t')
        file.write(f'{func.__name__}\t')
        file.write(f'{inspect.signature(func)}\t\n')
        func(word)
        file.close()
    return wrapper
@log_calls
def function(word):
    print(word)
function('hello')