def findPeople( data ):
    people_name = list(filter(lambda i: i[0].isupper(),data.split()))
    return people_name