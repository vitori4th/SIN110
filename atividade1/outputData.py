
#saída de dados
def outputData(result):
  file = open("C:/Vit/Unifei/Semestre4/SIN110/atividade1/result.txt", "a+") #local de criação e nome do arquivo / Modo de escrita: a=append(acescenta)    
  finalResult = f'{result[0]} {result[1][0]} {result[1][1]}' #concatenando as informações da  matriz no formato: nome_instância qtd_linhas qtd_colunas.
  print(finalResult)
  file.writelines(finalResult+'\n') #escrevendo no arquivo as informações: nome e quantidade de linhas/colunas
  file.close() #fecha arquivo após escrita