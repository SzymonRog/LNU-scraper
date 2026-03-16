import csv

def count_total_eclipses():
    total_eclipse = 1
        
    with open('zacmienia_XXIw.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        
        for row in reader:
            year = int(row[1])
            eclipse_type = row[8]
            
            
            
            if "T" in eclipse_type or "N" in eclipse_type:
                total_eclipse += 1
                
    
    return total_eclipse