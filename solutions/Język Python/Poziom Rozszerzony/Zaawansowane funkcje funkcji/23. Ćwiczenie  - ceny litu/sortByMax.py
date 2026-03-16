def m(x):
    return max(x)
def sortByMax(lists):
    return sorted(lists, key= m, reverse = True)
