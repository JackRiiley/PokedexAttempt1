import csv
from sqlalchemy.orm import Session
from models import Pokemon

def parse_data(db: Session):
    csv_file = "/Pokemon.csv"
    
    #Opens the CSV file and reads it
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            number = int(row["#"])
            name = row["Name"]
            type1 = row["Type 1"]
            type2 = row["Type 2"]
            generation = int(row["Generation"])
            legendary = row["Legendary"] == "True"
            
            #create instance of Pokemon Model and populate data
            pokemon = Pokemon(number=number, name=name, type1=type1, type2=type2, generation=generation)
            
            db.add(pokemon)
            db.commit()