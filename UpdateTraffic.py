import random

def update_traffic(graph, hour):
    # Aggiorna i pesi dei collegamenti in base all'ora corrente
   
    i = random.randrange(1, 8, 1)
    count = 0
   
    for u, v, weight in graph.edges(data='weight', default=1):
        pedestrian=graph[u][v].get('passaggi_pedonali', 0) # Raddoppia il peso durante le ore di punta
        stops=graph[u][v].get('stops', 0)
        # Aggiorna il peso in base all'ora corrente
        if 7 <= hour <= 9 or 17 <= hour <= 18:
            pedestrian*=2
            stops*=2
        # Aumenta il peso della tratta in base al numero di passaggi pedonali e agli stop
        weight += pedestrian* 0.1  # Aggiungi 0.1 al peso per ogni passaggio pedonale
        weight += stops* 0.5  # Aggiungi 0.5 al peso per ogni stop
 
        if i == u:
            weight *= 4
            #char = chr(ord(str(u)) + 17)
            print("Al nodo " + str(u) + " è presente un incidente")
            graph.nodes[u]['incident'] = True  # Imposta un attributo "incident" al nodo   
            #if count <= 0:
                #print("Al nodo " + char + " è presente un incidente")
                #count += 1
                #graph.nodes[u]['incident'] = True  # Imposta un attributo "incident" al nodo
 
        graph[u][v]['weight'] = weight