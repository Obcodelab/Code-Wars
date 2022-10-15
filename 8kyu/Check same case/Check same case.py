def same_case(a, b):
    if a.isupper():
        if b.isupper():
            return 1
        elif b.islower():
            return 0
    elif a.islower():
        if b.islower():
            return 1
        elif b.isupper():
            return 0
    while not type(a) is str or type(b) is str:
        return -1
        break
