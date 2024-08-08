def _get_data(how_much):
    with open('test2.txt', 'r') as f:
        return f.read(how_much)


def get_avg(how_much):
    data = _get_data(how_much)
    numbers = [int(x) for x in data]
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    print(get_avg(3))
