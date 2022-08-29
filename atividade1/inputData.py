import numpy as np

#entrada de dados
def inputData(instance): #nome do dataset(inst) e identificador da instância(id)
  path = "C:/Vit/Unifei/Semestre4/SIN110/atividade1/instances/" + instance +'.txt' #caminho 
  array=np.loadtxt(path) #carregando dados do arquivo e colocando numa matriz tipo numpy
  return instance, array.shape #retornando nome do arquivo e a dimensão da matriz