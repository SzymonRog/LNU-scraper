def reverse(s):
    y =""
    x = ""
    for x in range(len(s), 0 , -1):
        y += s[x-1]
    return y