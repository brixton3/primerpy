import os
import csv

def read_csv_data():
    file_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = f"{file_dir}/subs.csv"
    data = []
    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file) # uso de la funcion dictreader que crea un diccionario del csv q le pasemos
        for row in reader:
            if row["id"] == "2":
                data.append(row)
    return data

print(read_csv_data())