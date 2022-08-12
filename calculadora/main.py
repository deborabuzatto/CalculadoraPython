def main():
  operacao = int(input("digite o número da operação: "))
  if (operacao > 6):
     print("OPERACAO INVALIDA")
  else:
    n1 = float(input("digite o primeito número: "))
    n2 = float(input("digite o segundo número: "))
  if (operacao == 1):
    print(n1+n2)
  if (operacao == 2):
    print(n1-n2)
  if (operacao == 3):
    print(n1*n2)
  if (operacao == 4):
    print(n1/n2)
  if (operacao == 5):
    print(n1**n2)
  if (operacao == 6):
    print(n1**(1/n2))
  return 0 
if __name__ == "__main__":
    main()