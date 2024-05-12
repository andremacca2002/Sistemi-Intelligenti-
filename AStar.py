from queue import PriorityQueue
from heuristic import heuristic
import importCoord

geo_coord, _ = importCoord.readCoord()

class AStar:
    def __init__(self, grafo):
        self.graph = grafo

    def solve(self, start, goal):
        frontier = PriorityQueue() #coda di priorità che tiene traccia dei nodi da esaminare. Inizia con il nodo di partenza.
        frontier.put((0, start))
        
        came_from = {} #dizionario che tiene traccia dei nodi precedenti durante la ricerca del percorso ottimale.

        g_score = {nodi: float("inf") for nodi in self.graph} #dizionario che tiene traccia della somma del costo tra ogni nodo dal nodo di partenza.
        g_score[start] = 0

        #costo calcolato sommando il costo della tratta (g_score) e una stima del costo rimanente per arrivre a destinazione (heuristic).
        f_score = {node: float("inf") for node in self.graph} 
        f_score[start] = heuristic(geo_coord[start], geo_coord[goal])

        while not frontier.empty(): 
            _, corrente = frontier.get() #fino a quando la coda di priorità non è vuota

            if corrente == goal:
                path = []

                while corrente in came_from:
                    path.append(corrente)  #aggiungo nodo corrente
                    corrente = came_from[corrente]   #il nodo corrente viene aggiornato al suo predecessore tramite came_from[current]

                path.append(start) 
                path.reverse()  #viene ricostruito il percorso ottimale seguendo gli archi inversi salvati nel dizionario came_from

                return path

            for neighbor in self.graph[corrente]: #prendo i vicini del nodo corrente nel grafo
                tentative_g_score = g_score[corrente] + self.graph[corrente][neighbor].get("weight")   #sommo al costo complessivo della tratta in quel momento, il costo della tratta futura
                
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = corrente
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(geo_coord[neighbor], geo_coord[goal])
                    frontier.put((f_score[neighbor], neighbor)) #uso f come priorità

        return None
    
    
