def birthdayDict( users ):
    return { i[11:] : i[:10] for i in users}