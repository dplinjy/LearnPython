lis = [2, 3, 5, 4, 9, 6]

new_list = []

def get_min(lis):
    a = min(lis)
    lis.remove(a)
    new_list.append(a)
    if len(lis) > 0:
        get_min(lis)
    return new_list

print(get_min(lis))