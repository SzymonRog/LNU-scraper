def short_list(numbers, k):
    for i in numbers:
        if i % k == 0:
            return
        else:
            yield i 