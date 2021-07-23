# Get items in a list that only appears once
def get_unique(_list: list):
    unique_list = []

    # First comparison
    for x in _list:
        if not _list.count(x) >= 2:
            unique_list.append(x)
    
    return unique_list

print(get_unique([
    "./man",
    "./dir",
    "conde",
    "ccc",
    "conde",
    "ccc"
]))