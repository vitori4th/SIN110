import numpy

def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj]> 0:
        verificaAdjacentes = True
    else:
        verificaAdjacentes = False
    return print(verificaAdjacentes)

def tipoGrafo(matriz):
    laco = False 
    arestaMultipla = False
    direcionado = False
    qtdVertices = np.shape(matriz)[0] #descobre dimensão da matriz
    for vi in range(0, qtdVertices):  # Para cada vértice vi
        if matriz[vi][vi]>=1:
            laco = True #verifica se possui laço
        for vj in range(0, qtdVertices): # Para cada vértice vj
            controle = matriz[vi][vj]
            if matriz[vi][vj]>1:  #verifica se possui arestas multiplas
                    arestaMultipla = True  
                
            while controle > 0: # Adiciona a quantidade de arestas paralelas ou peso da aresta
                if (matriz[vi][vj])!=(matriz[vj][vi]): #verifica se é um grafo direcionado
                    direcionado=True
                if controle>1:  #verifica se possui arestas multiplas
                    arestaMultipla = True  
                controle -= 1

    if not laco and not arestaMultipla and not direcionado: #verifica se não tem arestas multiplas e nem laços: GRAFO SIMPLES
        return print(0) #simples 
    if not laco and arestaMultipla and direcionado: #verifica se possui arestas multiplas e não possui laço: MULTIGRAFO
        return print(21) # multigrafo dirigido
    if not laco and arestaMultipla and not direcionado: #verifica se possui arestas multiplas e não possui laço: MULTIGRAFO
        return print(20) # multigrafo 
    if laco and not direcionado: #verifica se não possui arestas multiplas e possui laço: PSEUDOGRAFO
        return print(30) #pseudografo
        
    if laco and direcionado : #verifica se não possui arestas multiplas e possui laço: PSEUDOGRAFO
        return print(31) #pseudografo dirigido
      
    
    if direcionado and not laco and not arestaMultipla: #verifica se é direcionado: DÍGRAFO
        return print(1) #dígrafo
def calcDensidade(matriz):
    densidade = 0
    qtdVertices = np.shape(matriz)[0] #descobre quantidade de vertices
    qtdArestas=0
  
    #calcula quantidade de arestas
    for vi in range(0, qtdVertices):  # Para cada vértice vi
        for vj in range(vi+1, qtdVertices): # Para cada vértice vj
            controle = matriz[vi][vj]
            while controle > 0: 
                qtdArestas+=1
                controle -= 1

    densidade = (2 * qtdArestas)/(qtdVertices * (qtdVertices-1))

    
    densidadeFormatada = "{:.3f}".format(densidade) #formata densidade parad tres casas decimais
    return print(float(densidadeFormatada))
def insereAresta(matriz, vi, vj):
    matriz[vj][vi] +=1 #soma um na posição(aresta) desejada
    matriz[vi][vj] +=1
    return print(matriz)
def insereVertice(matriz):
    matriz = np.array(matriz)
    vi = [] #define vi como um array vazio
    size=np.shape(matriz) #decobre tamanho da matriz
    x=size[0]

    #adiciona valores ao vetor
    while x>0:
        vi.append(0) 
        x-=1
    npArray=np.array(vi) #traforma um array em um array numpy
    lastRow =matriz.shape[0]
    #adiciona linha a matriz numpy
    matriz = np.insert(matriz,lastRow,[npArray],axis= 0)  
    vi.append(0) #adicionando mais um zero para completar a coluna, já que foi inserido uma nova linha

    colunaAdicionada = np.array(vi)
    #adiciona coluna a matriz numpy
    matriz = np.column_stack((matriz, colunaAdicionada))
   
    return print(matriz)
def removeVertice(matriz, vi):

    x=0
    size = len(matriz[vi])
    while x< size:
        matriz[vi][x]= -1 
        matriz[x][vi]= -1 
        x+=1

    m=np.array(matriz)
    return print(m)
def removeAresta(matriz, vi, vj):
    if matriz[vi][vj]>=1: #subtrai um na posição(aresta) desejada se existir aresta(maior que zero)
        matriz[vi][vj] -=1
    if matriz[vj][vi]>=1: #subtrai um na posição(aresta) desejada se existir aresta(maior que zero)
        matriz[vj][vi] -=1
    return print(matriz)
