from faulty_lib import faulty_generator

with open("wynik.txt","w") as file:
    
    for i in faulty_generator():
        file.write(i)
        file.write("\n")
        