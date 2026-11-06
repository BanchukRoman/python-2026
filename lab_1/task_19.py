

def cache(func):
    cache_dict = dict()
    def wrapper(*args):
        if args in cache_dict.keys():
            return cache_dict[args]
        else:
            cache_dict[args] = func(*args)
            return cache_dict[args]
    return wrapper
@cache
def math(a, b):
    result = ((a * b) ** a)
    return result


print(math(2, 10))
print(math(4, 2))
print(math(2, 10))

