import os

def readStreets():
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, 'archi.txt')

    with open(file_path, 'r') as file:
        lines = file.readlines()

    arches = []

    # Itera su ogni riga letta
    for line in lines:
        # Rimuovi i caratteri di spazio bianco iniziali e finali e suddividi la riga in base alle virgole
        parts = line.split('/')
        
        # Estrai i valori di ogni tupla dalla stringa e convertili nel tipo di dato appropriato
        tupla = (int(parts[0]), int(parts[1]), eval(parts[2]))
        
        # Aggiungi la tupla alla lista
        arches.append(tupla)

    return arches