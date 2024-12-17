import os
import csv
import random
def read_csv_data():
    file_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = f"{file_dir}/subs.csv"
    data = []
    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file) # uso de la funcion dictreader que crea un diccionario del csv q le pasemos.
        for row in reader:
            if row["status"] == "activo":
                data.append(row)
                print(row)
    return data

def select_winners(data: list) -> list:
    if len(data) < 3:
        raise ValueError("el numero de elementos debe ser minimo 3.")
    return random.sample(data, 3)

def display_winners(winners):
    prizes = ["Suscripcion", "Descuento", "Libro"]
    for winner, prize in zip(winners, prizes):
        print(f"{prize}: {winner['email']} (ID:{winner['id']})")

try:
    data= read_csv_data()
    winners= select_winners(data)
    #print(winners) comentar
    display_winners(winners)
except Exception as e:
    print(e)