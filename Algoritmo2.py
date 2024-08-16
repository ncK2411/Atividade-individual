def calcular_area_comodos(): #cria uma função.
total_area = 0 #atribui um valor a uma variavel.

while True: #informa uma condição para que o programa continue rodando.

#pede para o usuario informar dois valores para atribuir a uma variavel.
largura = float(input("Digite a largura do cômodo (em metros): "))
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

#efetua o calculo.
area_comodo = largura * comprimento
#mostra ao usuario um resultado da conta efetuada.
print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.")

total_area += area_comodo

#pede para que o usuário informe se tem mais comodos para efetuarcalculo.
mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower()
if mais_comodos != 's': #traz a condição de encerramento do programa, caso não tenha mais comodos para calculo.
break

# retorna um valor desejado.
return total_area

area_total = calcular_area_comodos()
print(f"A área total da casa é: {area_total:.2f} metros quadrados.") #mostra para o usuário qual o resultado obtido.