list_item = [1, 2, 3, 4, 5]


def chop(listx):
    del listx[0]
    del listx[-1]


chop(list_item)


def middle(new_list):
    return new_list


print(middle(list_item))
