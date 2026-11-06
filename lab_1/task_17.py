def dict_merge(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1 and isinstance(dict1[key], dict) and isinstance(value, dict):
            dict_merge(dict1[key], dict2[key])
        else:
            dict1[key] = value
    return dict1

dict_a = {'a': 1, 'b': {'c': 1, 'f': 4}}
dict_b = {'d': 1, 'b': {'c': 2, 'e': 3}}
dict_merge(dict_a, dict_b)
print(dict_a)