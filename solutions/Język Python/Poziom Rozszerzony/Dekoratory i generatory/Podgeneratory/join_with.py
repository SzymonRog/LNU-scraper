def join_with(iterators, sep):
    first = True
    for i in iterators:
        if first:
            first = False
        else:
            yield from sep
            
        yield from i