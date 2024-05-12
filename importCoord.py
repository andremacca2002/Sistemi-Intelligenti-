import os

def readCoord():
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, 'coordinate.txt')

    with open(file_path, 'r') as file:
        citta = file.readline().strip('()\n')
        lines = file.readlines()

    geo_coord = [
        tuple(map(float, point.strip('()\n ').split(',')))
        for point in lines
    ]

    return geo_coord, citta