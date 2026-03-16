import random


def rand_anagram(text: str) -> str:
    tekst = random.sample(text,len(text))
    napis = ""
    for i in tekst:
        napis += str(i)
    
    return napis