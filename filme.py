def main():
  idade = int(input("digite sua idade: "))

  if idade >= 18:
    print("Entrada liberada!")
  elif idade >= 16:
    acompanhante = input("Você está acompanhado? (s/n): ")
    if acompanhante == "s" or acompanhante == "S"
      print("Entrada liberada")
    else:
      print("Entrada proibida!")
  else:
      print("Entrada proibida!")
    
  return 0
main()