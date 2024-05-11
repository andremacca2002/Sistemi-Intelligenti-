import osmnx as ox
import matplotlib.pyplot as plt

# Aggiungi dei punti alla mappa
coordinate_punti = [(45.5118783, 10.2792341),#santa eufemia 
    (45.5215785, 10.2632404),
    (45.5023621, 10.2746251),
    (45.5247029, 10.2435765),
    (45.5198489, 10.1956535),
    (45.5368811, 10.2028181),
    (45.5383315, 10.2318613),
    (45.5273072, 10.1761407),
    (45.5420940, 10.1842370),
    (45.5639428, 10.2314365)]#UNIBS 
    

def plotOsmnx(percorso, grafo):
    # Definisci le coordinate del centro dell'area di interesse
    lat, lon = 45.5368, 10.2170  #coordinate di Brescia centro

    # Definisci la distanza (in metri) dalla posizione centrale per definire l'area
    dist = 5000  # Ad esempio, 5 km di raggio

    # Crea il grafo della rete stradale per l'area di interesse senza utilizzare la cache
    G = ox.graph_from_point((lat, lon), dist=dist, dist_type='bbox', network_type='drive', )
    _, ax = ox.plot_graph(G, node_size=1, node_color='k', edge_linewidth=1, show=False, close=False, bgcolor='w', edge_color='grey', figsize=(15,15))
    
    #le cordinate vengono associate al nodo più vicino e rappresentati sulla mappa 
    for node in grafo.nodes():
        if 'incident' in grafo.nodes[node]:
            nodo = ox.nearest_nodes(G, coordinate_punti[node][1], coordinate_punti[node][0])
            ax.scatter(G.nodes[nodo]['x'], G.nodes[nodo]['y'], c='red', s=100, zorder = 3) #nodo con incidente diventa rosso 
        else:            
            nodo = ox.nearest_nodes(G, coordinate_punti[node][1], coordinate_punti[node][0])
            ax.scatter(G.nodes[nodo]['x'], G.nodes[nodo]['y'], c='blue', s=100, zorder=3) #i restanti nodi sono blue 

    shortest_path = []

    i = 0
    for p in percorso[:-1]: #percorso è stato trovato da A-star e passato alla funzione, l'ultimo elemento è escluso
        nodo1 = coordinate_punti[percorso[i]] #associamo i nodi alle rispettive coordinate 
        nodo2 = coordinate_punti[percorso[i+1]]

        partenza = ox.nearest_nodes(G, nodo1[1], nodo1[0]) #associa il nodo più vicinio
        destinazione = ox.nearest_nodes(G, nodo2[1], nodo2[0])

        perc = ox.shortest_path(G, partenza, destinazione)

        for n in perc[1:]:
          shortest_path.append(n)
        i += 1
    _, ax = ox.plot_graph_route(G, shortest_path, ax=ax, route_linewidth=2, route_alpha=1.0) #colora di rosso il percorso ottimale 
    plt.show()

def getNumeroNodi():
    return len(coordinate_punti)
