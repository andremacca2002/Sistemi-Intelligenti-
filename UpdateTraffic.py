import random

def update_traffic(graph, hour, nNodi, checkbox_var):
    # Aggiorna i pesi dei collegamenti in base all'ora corrente
    if checkbox_var:
        i = random.randrange(1, nNodi - 1)
    else:
        i = -1

    count = 0
    
    for u, v, weight in graph.edges(data='weight', default=1):
        pedestrian=graph[u][v].get('passaggi_pedonali', 0) # Raddoppia il peso durante le ore di punta
        stops=graph[u][v].get('stops', 0)

        # Aggiorna il peso in base all'ora corrente
        if 7 <= hour <= 9 or 17 <= hour <= 18:
            pedestrian *= 2
            stops *= 2

        # Aumenta il peso della tratta in base al numero di passaggi pedonali e agli stop
        weight += pedestrian * 0.2  # Aggiungi 0.1 al peso per ogni passaggio pedonale
        weight += stops * 0.5  # Aggiungi 0.5 al peso per ogni stop
 
        if i == v:
            weight = float("inf")

            if count <= 0 :
                print("Al nodo " + str(v) + " è presente un incidente")
                graph.nodes[v]['incident'] = True  # Imposta un attributo "incident" al nodo 
                count += 1
 
        graph[u][v]['weight'] = weight