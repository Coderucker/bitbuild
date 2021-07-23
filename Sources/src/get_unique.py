def get_unique(_list: list):
    unique_list = []

    for x in _list:
        if x not in unique_list:
            unique_list.append(x)
    
    return unique_list