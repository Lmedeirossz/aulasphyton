def main():
  num1 = int(input("Digite  um numero: "))
  num2 = int(input("Digite outro número: "))

  soma = num1 + num2
  sub = num1 - num2
  mult = num1 * num2

  if num2 == 0:  
    div = "Não existe divisão por zero"
  else:
    div = num1 / num2

  print("A soma de ", num1, " + ", num2, "=", soma)
  print("A subtação de ", num1, " - ", num2, "=", sub)
  print("A multiplicação de ", num1, " * ", num2, "=", mult)
  print("A divisão de ", num1, " / ", num2, "=", div)
  return 0
main()