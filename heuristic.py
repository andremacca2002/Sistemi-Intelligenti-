import geopy.distance as gd

def heuristic(start, end):
    geodesic = gd.geodesic(start, end) #funione che calcola la distanza in linea d'aria date le coordinate 
    distanza = str(geodesic) #distanza linea d'aria 
    distanza = distanza[0:4] #tengo solo i km 
    distanza = float(distanza) 
    return distanza # Ritorna la distanza in linea d'aria dal nodo corrente al nodo G
