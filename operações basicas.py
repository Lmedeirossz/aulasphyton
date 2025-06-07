def main():
  num1 = int(input("Digite  um numero: "))
  num2 = int(input("Digite outro número: "))

  soma = num1 + num2
  sub = num1 - num2
  mult = num1 * num2
  div = num1 / num2

  print("A soma de ", num1, " + ", num2, "=", soma)
  print("A soma de ", num1, " - ", num2, "=", sub)
  print("A soma de ", num1, " * ", num2, "=", mult)
  print("A soma de ", num1, " / ", num2, "=", div)
  return 0
main()