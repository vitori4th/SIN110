import inputData as inp
import outputData as out

if __name__=='__main__':
  instance=input("Qual nome do arquivo que deseja selecionar?")
  result = inp.inputData(instance) #passando nome da intância como argumento 
  out.outputData(result)