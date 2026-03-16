def emailProvider( email ):
    do_znak = email.index("@")
    return email[do_znak + 1:]