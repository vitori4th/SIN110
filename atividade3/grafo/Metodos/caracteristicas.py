'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

05/09/2022
===================================================='''

import numpy as np

'''Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
Entrada: matriz de adjacências (numpy.ndarray), vi (Integer), vj (Integer)
Saída: 0 (Integer) se vi e vj NÃO são adjacentes; 1 se vi e vj são adjacentes'''
def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0: # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes

def tipoGrafo(matriz):
    laco = False 
    arestaMultipla = False
    direcionado = False
    qtdVertices = np.shape(matriz)[0] #descobre dimensão da matriz
    for vi in range(0, qtdVertices):  # Para cada vértice vi
        if matriz[vi][vi]>=1:
                    laco = True #verifica se possui laço
        if matriz[vi][vi]>1:
                    arestaMultipla = True #verifica se possui arestas multiplas
        for vj in range(vi+1, qtdVertices): # Para cada vértice vj
            controle = matriz[vi][vj]
            while controle > 0: # Adiciona a quantidade de arestas paralelas ou peso da aresta
                if (matriz[vi][vj])!=(matriz[vj][vi]): #verifica se é um grafo direcionado
                    direcionado=True
                if controle>1:  #verifica se possui arestas multiplas
                    arestaMultipla = True  
                controle -= 1
    if not laco and not arestaMultipla: #verifica se possui não tem arestas multiplas e nem laços: GRAFO SIMPLES
        return 0 #simples 
    if direcionado: #verifica se é direcionado: DÍGRAFO
        return 1 #dígrafo
    if not laco and arestaMultipla: #verifica se possui arestas multiplas e não possui laço: MULTIGRAFO
        return 2 # multigrafo 
    if laco and arestaMultipla: #verifica se não possui arestas multiplas e possui laço: PSEUDOGRAFO
        return 3 #pseudografo

def calcDensidade(matriz):
    densidade = 0
    qtdVertices = np.shape(matriz)[0] #descobre quantidade de vertices
    qtdArestas=0
    x = tipoGrafo(matriz)
    simples = x==0
    digrafo = x==1

    #calcula quantidade de arestas
    for vi in range(0, qtdVertices):  # Para cada vértice vi
        for vj in range(vi+1, qtdVertices): # Para cada vértice vj
            controle = matriz[vi][vj]
            while controle > 0: 
                qtdArestas+=1
                controle -= 1

    if simples: #se grafo simples calcula densidade de um jeito 
        densidade = (2 * qtdArestas)/(qtdVertices * (qtdVertices-1))
    if digrafo:#se grafo digrafo calcula densidade de outro jeito 
        densidade = qtdArestas/(qtdVertices  *(qtdVertices-1))
    
    densidadeFormatada = "{:.3f}".format(densidade) #formata densidade parad tres casas decimais
    return float(densidadeFormatada)

def insereAresta(matriz, vi, vj):
    matriz[vi][vj] +=1 #soma um na posição(aresta) desejada
    return matriz

def insereVertice(matriz, vi):
    vi = [] #define vi como um array vazio
    size=np.shape(matriz) #decobre denisdade da matriz
    x=size[0]

    #adiciona valores ao vetor
    while x>0:
        vi.append(3) 
        x-=1
    npArray=np.array(vi) #traforma um array em um array numpy

    #adiciona linha a matriz numpy
    matriz = np.insert(matriz,matriz.shape[0],[npArray],axis= 0)  
    vi.append(0) #adicionando mais um zero para completar a coluna, já que foi inserido uma nova linha

    colunaAdicionada = np.array(vi)
    #adiciona coluna a matriz numpy
    matriz = np.column_stack((matriz, colunaAdicionada))
 
   
    return matriz

def removeVertice(matriz, vi):
    array = np.array(matriz) #define um array do tipo numpy 

    array = np.delete(array,vi, axis = 0) #deleta linha do vertice inserida pelo usuário
             
    result = np.delete(array, vi, 1)  #deleta coluna do vertice inserida pelo usuário

    return result

def removeAresta(matriz, vi, vj):
    if matriz[vi][vj]>=1: #subtrai um na posição(aresta) desejada se existir aresta(maior que zero)
        matriz[vi][vj] -=1
    return matriz
