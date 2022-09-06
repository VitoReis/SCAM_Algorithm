from igraph import *
import matplotlib.pyplot as plt

def main():
    # Lendo o grafo
    graph = Graph.Read_Ncol("myGraph.ncol", directed=False)
    # plot(graph, target=plt.axes())
    for vertice in graph.vs:              # Para cada vertice no grafo
        if vertice['name'] == 's':        # Encontra o index de S e de T
            s = vertice.index
        elif vertice['name'] == 't':
            t = vertice.index

    deleted = []
    # Mostrando o grafo inicial na tela
    print('**************')
    print('Initial graph:')
    print('**************')
    print(graph)
    print('**************\n\n')
    # plot(graph, layout='circle')

    # Removendo os vertices de maior valor até o grafo se tornar não conexo
    connected = True

    # Determina se existe um caminho de S a T
    path = graph.get_all_simple_paths(s, t)
    if len(path) >= 1:
        pathExist = True
    else:
        pathExist = False

    while(connected and pathExist):
        print('***************')
        print('Graph vertices:')
        print('***************')
        for v in graph.vs:
            print(f'Nome: {v["name"]} Index: {v.index}')
        print('***************')
        verticeValue(graph)
        deleteVertice(graph, deleted)
        # plot(graph, target=plt.axes())
        connected = verifyConnection(graph)

    # Mostrando o grafo final na tela
    print('************')
    print('Final graph:')
    print('************')
    print(graph)
    print('************')
    print(f'Deleted vertices: {deleted}')
    print('************')
    # plot(graph, layout='circle')

def verticeValue(graph):
    # Encontra o index de S e de T
    for vertice in graph.vs:
        if vertice['name'] == 's':
            s = vertice.index
        elif vertice['name'] == 't':
            t = vertice.index

    # Determinando o valor dos vertices
    paths = graph.get_all_simple_paths(s, t)
    print(f'Paths by value: {paths}')
    graph.vs['value'] = 0
    for path in paths:    # Para cada caminho existente, se o vertice não é 'S' ou 'T', e esta em algum caminho...
        for vertice in path:
            if graph.vs[vertice]['name'] != 's' and graph.vs[vertice]['name'] != 't':
                graph.vs[vertice]['value'] += 1                                     # ...adiciona 1 ao valor do vertice
    print(f'Vertice values: {graph.vs["value"]}')

def deleteVertice(graph, deleted):
    greater = -1
    greaterIndex = -1
    for vertice in graph.vs:                                # Para cada vertice no grafo
        if vertice['name'] != 's' and vertice['name'] != 't':   # Se o vertise não é o S e não é o T
            if vertice['value'] > greater:                    # Se a particopação dele é a maior
                greaterName = vertice['name']               # Define o nome do vertice de maior valor
                greater = vertice['value']                    # Define o maior como esse vertice
                greaterIndex = vertice.index                      # Define o index do maior como o desse vertice
    print(f'Deleting vertice: {greaterName}')
    print('***************\n\n')
    deleted.append(greaterName)
    graph.delete_vertices(graph.vs(greaterIndex))                 # Deleta o vertice de maior tamanho passando o index dele

def verifyConnection(graph):
    for vertice in graph.vs:
        if graph.is_connected(vertice.index) == False:
            return False
    return True

if __name__ == '__main__':
    main()