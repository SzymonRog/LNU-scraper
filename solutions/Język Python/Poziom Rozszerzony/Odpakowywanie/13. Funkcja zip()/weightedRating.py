def weightedRating( rating, weight ):
    lis = []
    for ocena, waga in zip(rating, weight):
        lis.append(round(ocena * waga, 1))
    return lis
    