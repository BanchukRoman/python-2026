def type_check(*types):
    def decorator(func):
        def wrapper(*args):
            for arg, arg_type in zip(args, types):
                if not isinstance(arg, arg_type):
                    raise TypeError(
                    f"Аргумент {arg} не соответствует типу {arg_type.__name__}"
                    )
            result = func(*args)
            return result
        return wrapper

    return decorator

@type_check(int, int)
def math(a, b):
    return a * b

print(math(7, 9))
