def has_equal_ends(a):
    new = []
    for i in a:
        new.append(i)
    return new[0] == new[5]

print(has_equal_ends([7, 80, 66, 34, 44, 7]))
