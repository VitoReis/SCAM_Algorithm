from igraph import *
import matplotlib.pyplot as plt

def main():
    graph = Graph.Read_Ncol("myGraph.ncol", directed=False)     # Lendo o grafo
    # plot(graph, target=plt.axes())

    for vertex in graph.vs:              # Encontra o index de S e de T
        if vertex['name'] == 's':
            s = vertex.index
        elif vertex['name'] == 't':
            t = vertex.index

    print('**************')     # Mostrando o grafo inicial na tela
    print('Initial graph:')
    print('**************')
    print(graph)
    print('**************\n\n')
    # plot(graph, layout='circle')

    deleted = []
    connected = True

    path = graph.get_all_simple_paths(s, t)     # Verifica se existe um caminho de S a T
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
        vertexValue(graph)
        deleteVertex(graph, deleted)
        # plot(graph, target=plt.axes())
        if graph.is_connected() == True:    # Verifica se o grafo é conexo
            connected = True
        else:
            connected = False

    print('************')       # Mostrando o grafo final na tela
    print('Final graph:')
    print('************')
    print(graph)
    print('************')
    print(f'Deleted vertex: {deleted}')
    print('************')
    # plot(graph, layout='circle')

def vertexValue(graph):
    # Encontra o index de S e de T
    for vertex in graph.vs:
        if vertex['name'] == 's':
            s = vertex.index
        elif vertex['name'] == 't':
            t = vertex.index

    # Determina o valor dos vertices
    paths = graph.get_all_simple_paths(s, t)
    print(f'Paths by value: {paths}')
    graph.vs['value'] = 0
    for path in paths:    # Para cada caminho existente, se o vertice não é 'S' ou 'T', e esta em algum caminho...
        for vertex in path:
            if graph.vs[vertex]['name'] != 's' and graph.vs[vertex]['name'] != 't':
                graph.vs[vertex]['value'] += 1                                     # ...adiciona 1 ao valor do vertice
    print(f'Vertice values: {graph.vs["value"]}')

def deleteVertex(graph, deleted):
    # Encontra o vertice de maior valor
    greater = -1
    greaterIndex = -1
    for vertex in graph.vs:
        if vertex['name'] != 's' and vertex['name'] != 't':
            if vertex['value'] > greater:
                greaterName = vertex['name']
                greater = vertex['value']
                greaterIndex = vertex.index
    print(f'Deleting vertex: {greaterName}')
    print('***************\n\n')

    # Salva o nome dos vertices deletados em uma lista para melhor visualização posteriormente
    deleted.append(greaterName)
    # Deleta o vertice de maior valor
    graph.delete_vertices(graph.vs(greaterIndex))

if __name__ == '__main__':
    main()