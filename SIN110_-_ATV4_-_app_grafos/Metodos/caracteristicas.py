def criaListaAdjacencias(matriz):
    listaAdj = {}
    
    for i in range(len(matriz)):
        lista=[]
        for j in range(len(matriz[i])):
                        while matriz[i][j]>= 1:
                           lista.append(j) #adiciona as arestas
                           matriz[i][j]-=1
        listaAdj[i]=lista
    return print(listaAdj)
def tipoGrafoLista(listaAdj):
    laco = False 
    arestaMultipla = False
    direcionado = False

    #for aninhado para verificar as caracteristicas do grafo
    for x in listaAdj:
        for y in listaAdj:
            if y in  listaAdj[x] and x==y:
                laco = True
            if y in listaAdj[x] and not (x in listaAdj[y]):
                    direcionado=True
            if listaAdj[x].count(y) > 1: #verifica se possui arestas multiplas
                arestaMultipla = True 
 
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
def calcDensidadeLista(listaAdj):
    densidade = 0
    qtdVertices = len(listaAdj) #descobre quantidade de vertices
    qtdArestas= 0


    #calcula quantidade de arestas
    for vi in range(0, qtdVertices):  # Para cada vértice vi
        qtdArestas+=len(listaAdj[vi]) # soma quantidade de arestas

    densidade = qtdArestas/(qtdVertices  *(qtdVertices-1))
    #se grafo não for digrafo calcula densidade de outro jeito
    #qtdArestas=qtdArestas/2 #dividi por dois para não mudar a formula do grafo da densidade, já que anteriormente já foi somado as arestas 
    #densidade = (2 * qtdArestas)/(qtdVertices * (qtdVertices-1))
    
    densidadeFormatada = "{:.3f}".format(densidade) #formata densidade parad tres casas decimais
    return print(float(densidadeFormatada))
def insereArestaLista(listaAdj, vi, vj):

    listaAdj[vi].append(vj) #adicionando aresta ao vertice vi
    listaAdj[vi].sort()
    # Se o grafo é não-direcionado, adiciona aresta nos dois sentidos.
    listaAdj[vj].append(vi) #adicionando aresta ao vertice vj
    listaAdj[vj].sort()
  
    return print(listaAdj)
def insereVerticeLista(listaAdj):
    size= len(listaAdj)
    listaAdj[size] = [] #cria uma chave com uma lista vazia
   
    return print(listaAdj)
def removeArestaLista(listaAdj, vi, vj):
    listaAdj[vi].remove(vj) # remove a aresta inserida
    if vi in listaAdj[vj]:
        listaAdj[vj].remove(vi) #remove a outra aresta 

    return print(listaAdj)
def removeVerticeLista(listaAdj, vi):
    del listaAdj[vi] #deleta vértice da lista de adjacencia

    for v in listaAdj:
        for v2 in listaAdj[v]: # for para caso haja arestas multiplas, remover ambas
            if vi in listaAdj[v]:
                listaAdj[v].remove(vi) #remove cada aresta que contenha o vértice excluído 

    return print(listaAdj)
def verificaAdjacenciaLista(listaAdj, vi, vj):
    verticesAdjacentes = False
    if vj in listaAdj[vi]: # Se vj estiver em vi define adjacencia como true
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    return print(verticesAdjacentes)
