import networkx as nx
from AStar import AStar
from tkinter import messagebox
import UpdateTraffic
import graph as draw
import importStreets
import importCoord

class PathGenerator:
    def __init__(self, orario_input):
        self.orario_input = orario_input

    def generate_path(self, checkbox_var):
        orario = self.orario_input
        print(orario)

        try:
            hour, minute = map(int, orario.split(':'))
            
            if not 0 <= hour < 24 or not 0 <= minute < 60:      # Verifica se l'orario è nel formato corretto
                raise ValueError("Formato non supportato")      #genera eccezione se l'orario non è nel formato adeguato 

            # Creazione del grafo
            graph = nx.DiGraph()
            archi = importStreets.readStreets()
            coord, _ = importCoord.readCoord()  
            nNodes=len(coord)

            graph.add_edges_from(archi)

            # Converti l'ora e i minuti in un'unica rappresentazione dell'ora del giorno
            current_time = hour + minute / 60

            # Aggiorna i pesi dei collegamenti in base al traffico ( se è stata inserito un orario tra le 7-9 oppure 17-19 )
            UpdateTraffic.update_traffic(graph, current_time, nNodes, checkbox_var)

            #istanza classe Astar
            astar = AStar(graph)

            # Trova il percorso ottimale utilizzando l'algoritmo A*
            percorso_ottimale = astar.solve(0, draw.getNumeroNodi() - 1)

            #stampo i nodi per cui passa il percorso 
            print("Percorso ottimale:", percorso_ottimale)

            #visualizzo la mappa 
            draw.plotOsmnx(percorso_ottimale, graph)

        except ValueError as e:
            print("Errore:", e)  # Stampa l'eccezione specifica
            messagebox.showerror("Errore", "Formato supportato: 'HH:mm'") #messaggio in uscita se viene sollevata l'eccezione sul formato