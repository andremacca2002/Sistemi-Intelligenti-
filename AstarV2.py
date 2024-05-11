from queue import PriorityQueue
from heuristic import heuristic

coordinate = []

with open(r'c:\Users\fabio\Desktop\prog\Sistemi-Intelligenti-\coordinate.txt') as file:
        # Leggo le linee del file e le aggiungo alla lista
        for l in file.readlines():
            coordinate.append(l)


geo_coord = [
    tuple(map(float, point.strip('()\n ').split(',')))
    for point in coordinate
]

print(geo_coord)

class AStar:
    

    def __init__(self, grafo):
        self.graph = grafo

    def solve(self, start, goal):
        frontier = PriorityQueue() #è una coda di priorità che tiene traccia dei nodi da esaminare. Inizia con il nodo di partenza.
        frontier.put((0, start))
        
        came_from = {} #è un dizionario che tiene traccia dei nodi precedenti durante la ricerca del percorso ottimale.

        g_score = {nodi: float("inf") for nodi in self.graph} #è un dizionario che tiene traccia del costo del percorso più breve fino a ogni nodo dal nodo di partenza.
        g_score[start] = 0 #è un dizionario che tiene traccia della stima del costo totale dal nodo di partenza al nodo di destinazione
        #passando attraverso un certo nodo, calcolato sommando il costo effettivo (g_score) e una stima del costo rimanente (heuristic).
        f_score = {node: float("inf") for node in self.graph} #passando attraverso un certo nodo, calcolato sommando il costo effettivo (g_score) 
        #e una stima del costo rimanente (heuristic).
        f_score[start] = heuristic(geo_coord[start], geo_coord[goal]) #che verrà utilizzato per memorizzare i valori dei punteggi f (la somma del punteggio 
        #g e del punteggio euristico h) durante l'esecuzione dell'algoritmo A*.

        while not frontier.empty(): #viene ricostruito il percorso ottimale seguendo gli archi inversi salvati nel dizionario came_from
            _, corrente = frontier.get() #fino a quando la coda di priorità non è vuota
        #print(current)
            if corrente == goal:
                path = []
                while corrente in came_from:
                    path.append(corrente) #aggiungo nodo corrente
                    corrente = came_from[corrente] #il nodo corrente viene aggiornato al suo predecessore tramite came_from[current]
                path.append(start) 
                path.reverse()
                return path

            for neighbor in self.graph[corrente]: #prendo il nodo corrente nel grafo
                tentative_g_score = g_score[corrente] + self.graph[corrente][neighbor].get("weight", 1)   #print(graph[current][neighbor]) #{'weight': 4.1, 'passaggi_pedonali': 6, 'stops': 2}
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = corrente
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(geo_coord[neighbor], geo_coord[goal])
                    frontier.put((f_score[neighbor], neighbor)) #uso f come priorità (somma euristica e il costo fino a quel momento e il costo per arrivare al nodo corrente)

        return None
    
    
