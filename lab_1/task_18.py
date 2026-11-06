import time as t


def log_calls(func):
    def wrapper(*args):
        file = open('text.txt', 'w')
        file.write(f'Date: {t.ctime()}\t')
        file.write(f'Name: {func.__name__}\t')
        all_arg = [arg for arg in args]
        file.write(f'Arguments: {', '.join(all_arg)}\t\n')
        func(*args)
        file.close()
    return wrapper
@log_calls
def function(word):
    print(word)
function('hello')