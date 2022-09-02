from igraph import *
import matplotlib.pyplot as plt

def main():
    # Lendo o grafo
    graph = Graph.Read_Ncol("myGraph.ncol", directed=False)
    plot(graph, target=plt.axes())
    for vertice in graph.vs:              # Para cada vertice no grafo
        if vertice['name'] == 's':        # Encontra o index de S e de T
            s = vertice.index
        elif vertice['name'] == 't':
            t = vertice.index

    # Mostrando o grafo inicial na tela
    print('**************')
    print('Initial graph:')
    print('**************')
    print(graph)
    print('**************\n\n')
    plot(graph, layout='circle')

    # Removendo os vertices de maior valor até o grafo se tornar não conexo
    connected = True
    while(connected):
        print('***************')
        print('Graph vertices:')
        print('***************')
        for v in graph.vs:
            print(f'Nome: {v["name"]} Index: {v.index}')
        print('***************')
        verticeValue(graph)
        deleteVertice(graph)
        plot(graph, target=plt.axes())
        connected = verifyConnection(graph)

    # Mostrando o grafo final na tela
    print('************')
    print('Final graph:')
    print('************')
    print(graph)
    print('************')
    plot(graph, layout='circle')

def verticeValue(graph):
    # Encontra o index de S e de T
    for vertice in graph.vs:
        if vertice['name'] == 's':
            s = vertice.index
        elif vertice['name'] == 't':
            t = vertice.index

    # Determinando o valor dos vertices
    caminhos = graph.get_all_simple_paths(s, t)
    print(f'Paths by value: {caminhos}')
    graph.vs['value'] = 0
    for caminho in caminhos:    # Para cada caminho existente, se o vertice não é 'S' ou 'T', e esta em algum caminho...
        for vertice in caminho:
            if graph.vs[vertice]['name'] != 's' and graph.vs[vertice]['name'] != 't':
                graph.vs[vertice]['value'] += 1                                     # ...adiciona 1 ao valor do vertice
    print(f'Vertice values: {graph.vs["value"]}')

def deleteVertice(graph):
    maior = -1
    imaior = -1
    for vertice in graph.vs:                                # Para cada vertice no grafo
        if vertice['name'] != 's' and vertice['name'] != 't':   # Se o vertise não é o S e não é o T
            if vertice['value'] > maior:                    # Se a particopação dele é a maior
                maior = vertice['value']                    # Define o maior como esse vertice
                imaior = vertice.index                      # Define o index do maior como o desse vertice
    print(f'Deleting vertice: {maior}')
    print('***************\n\n')
    graph.delete_vertices(graph.vs(imaior))                 # Deleta o vertice de maior tamanho passando o index dele

def verifyConnection(graph):
    for vertice in graph.vs:
        if graph.is_connected(vertice.index) == False:
            return False
    return True

if __name__ == '__main__':
    main()