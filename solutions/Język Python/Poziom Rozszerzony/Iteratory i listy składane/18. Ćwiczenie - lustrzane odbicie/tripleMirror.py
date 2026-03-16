def tripleMirror( triple_data ):
    return [[i[::-1] for i in x[::-1]] for x in  triple_data[::-1]]