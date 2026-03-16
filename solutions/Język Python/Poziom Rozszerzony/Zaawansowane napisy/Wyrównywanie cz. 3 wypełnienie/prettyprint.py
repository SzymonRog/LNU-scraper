def table_of_contents( chapters ):
    strona = 1
    for i in chapters:
        print(f"{strona:.<5}{i:.>10}")
        strona += 1