space_dict = {'global': []}


def request(method: str, space: str, var: str):
    if method == 'get':
        get(space, var)
    elif method == 'create':
        create(space, var)
    elif method == 'add':
        add(space, var)
    else:
        return 'Не верный формат'


def get(space: str, var: str):
    if space in space_dict:
        space_dict[space] += var


def create(var: str, space: str):
    if space in space_dict:
        space_dict[space] += 


def add(space: str, var: str):
    if space in space_dict:
        space_dict[space] += var



if __name__ == '__main__':
    n = int(input())
    for num_req in range(n):
        request(*input().split())
