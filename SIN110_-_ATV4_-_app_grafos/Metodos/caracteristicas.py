'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

05/09/2022
===================================================='''


from collections import defaultdict as dd


def criaListaAdjacencias(matriz):
    listaAdj = dd(list) #cria lista do tipo defaultdict
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
                        while matriz[i][j]>= 1:
                           listaAdj[i].append(j) #adiciona as arestas
                           matriz[i][j]-=1
    return listaAdj

'''Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
Entrada: lista de adjacências 
Saída: 0 (Integer) se vi e vj NÃO são adjacentes; 1 se vi e vj são adjacentes'''
def verificaAdjacencia(listaAdj, vi, vj):
    if vj in listaAdj[vi]: # Se vj estiver em vi define adjacencia como true
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    return verticesAdjacentes

def tipoGrafo(listaAdj):
    laco = False 
    arestaMultipla = False
    direcionado = False

    #for aninhado para verificas as caracteristicas do grafo
    for x in listaAdj:
        if x in  listaAdj[x]:
            laco = True
        for y in listaAdj:
            if y in listaAdj[x] and not x in listaAdj[y]:
                    direcionado=True
            if listaAdj[x].count(y) > 1: #verifica se possui arestas multiplas
                arestaMultipla = True 
 
    if not laco and not arestaMultipla: #verifica se possui não tem arestas multiplas e nem laços: GRAFO SIMPLES
        return 0 #simples 
    if direcionado: #verifica se é direcionado: DÍGRAFO
        return 1 #dígrafo
    if not laco and arestaMultipla: #verifica se possui arestas multiplas e não possui laço: MULTIGRAFO
        return 2 # multigrafo 
    if laco and arestaMultipla: #verifica se não possui arestas multiplas e possui laço: PSEUDOGRAFO
        return 3 #pseudografo

def calcDensidade(listaAdj):
    densidade = 0
    qtdVertices = len(listaAdj) #descobre quantidade de vertices
    qtdArestas= 0
    
    x = tipoGrafo(listaAdj)
    digrafo = x==1

    #calcula quantidade de arestas
    for vi in range(0, qtdVertices):  # Para cada vértice vi
        qtdArestas+=len(listaAdj[vi]) # soma quantidade de arestas

    if digrafo:#se grafo digrafo calcula densidade de um jeito 
        densidade = qtdArestas/(qtdVertices  *(qtdVertices-1))
    else: #se grafo não for digrafo calcula densidade de outro jeito
        qtdArestas=qtdArestas/2 #dividi por dois para não mudar a formula do grafo da densidade, já que anteriormente já foi somado as arestas 
        densidade = (2 * qtdArestas)/(qtdVertices * (qtdVertices-1))
    
    densidadeFormatada = "{:.3f}".format(densidade) #formata densidade parad tres casas decimais
    return float(densidadeFormatada)

def insereAresta(listaAdj, vi, vj):
    x = tipoGrafo(listaAdj)
    digrafo = x==1
    listaAdj[vi].append(vj) #adicionando aresta ao vertice vi
    # Se o grafo é não-direcionado, adiciona aresta nos dois sentidos.
    if not digrafo:
        listaAdj[vj].append(vi) #adicionando aresta ao vertice vj
    return listaAdj

def insereVertice(listaAdj, vi):
    listaAdj[vi] = [] #cria uma chave com uma lista vazia
   
    return print(listaAdj)

def removeVertice(listaAdj, vi):
    del listaAdj[vi] #deleta vértice da lista de adjacencia

    for v in listaAdj:
        for v2 in listaAdj[v]: # for para caso haja arestas multiplas, remover ambas
            if vi in listaAdj[v]:
                listaAdj[v].remove(vi) #remove cada aresta que contenha o vértice excluído 

    return print(listaAdj)

def removeAresta(listaAdj, vi, vj):
    x = tipoGrafo(listaAdj) #verifica tipo de grafo
    digrafo = x==1
    
    listaAdj[vi].remove(vj) # remove a aresta inserida
    if not digrafo: #se não for digrafo
        listaAdj[vj].remove(vi) #remove a outra aresta 

    return listaAdj