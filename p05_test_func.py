def func(string):
    str_string = str(string)[::2]
    str_string = int(str_string) *2
    return int(str_string)

print(func(123))