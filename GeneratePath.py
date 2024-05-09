import networkx as nx
import matplotlib.pyplot as plt
from AstarV2 import AStar
from tkinter import messagebox
import UpdateTraffic
import getGRAFO as draw

class PathGenerator:
    def __init__(self, orario_input):
        self.orario_input = orario_input

    def generate_path(self):
        orario = self.orario_input
        try:
            # Verifica se l'orario è nel formato corretto
            hour, minute = map(int, orario.split(':'))
            if not 0 <= hour < 24 or not 0 <= minute < 60:
                raise ValueError("Formato non supportato") #genera eccezione se l'orario non è nel formato adeguato 

            # Creazione del grafo
            grafo = nx.DiGraph()

            # Aggiunta degli archi al grafo con attributi peso, passaggi pedonali e fermate
            archi = [(0, 1, {'weight': 2.5, 'passaggi_pedonali': 6, 'stops': 2}),
                     (0, 2, {'weight': 8, 'passaggi_pedonali': 0, 'stops': 0}),
                     (1, 3, {'weight': 1.8, 'passaggi_pedonali': 8, 'stops': 0}),
                     (1, 5, {'weight': 3.5, 'passaggi_pedonali': 21, 'stops': 3}),
                     (2, 4, {'weight': 1.7, 'passaggi_pedonali': 0, 'stops': 0}),
                     (2, 5, {'weight': 4.6, 'passaggi_pedonali': 19, 'stops': 7}),
                     (3, 5, {'weight': 1.8, 'passaggi_pedonali': 11, 'stops': 2}),
                     (5, 6, {'weight': 4.8, 'passaggi_pedonali': 21, 'stops': 1}),
                     (4, 6, {'weight': 7.2, 'passaggi_pedonali': 12, 'stops': 3})]

            grafo.add_edges_from(archi)

            # Converti l'ora e i minuti in un'unica rappresentazione dell'ora del giorno
            current_time = hour + minute / 60

            # Aggiorna i pesi dei collegamenti in base al traffico ( se è stata inserito un orario tra le 7-9 oppure 17-19 )
            UpdateTraffic.update_traffic(grafo, current_time)

            #istanza classe Astar
            astar = AStar(grafo)

            # Trova il percorso ottimale utilizzando l'algoritmo A*
            percorso_ottimale = astar.solve(0, 6)

            #stampo i nodi per cui passa il percorso 
            print("Percorso ottimale:", percorso_ottimale)

            #visualizzo la mappa 
            draw.plotOsmnx(percorso_ottimale, grafo)

        except ValueError as e:
            messagebox.showerror("Errore", "Formato supportato: 'HH:mm'") #messaggio in uscita se viene sollevata l'eccezione sul formato