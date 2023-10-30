def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."

def calculadora(operacao, x, y):
    operacoes = {
        '1': somar,
        '2': subtrair,
        '3': multiplicar,
        '4': dividir
    }

    if operacao in operacoes:
        return operacoes[operacao](x, y)
    else:
        return "Operação inválida."

print("Selecione a operação:")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

escolha = input("Digite 1, 2, 3 ou 4: ")

if escolha in ('1', '2', '3', '4'):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = calculadora(escolha, num1, num2)
    print(f"Resultado: {resultado}")

else:
    print("Escolha inválida.")
