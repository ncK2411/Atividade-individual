# define uma função que vai retornar um valor esperado.
# variavel(taxa_juros_diaria) recebe um valor para ser usado.
def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso):
taxa_juros_diaria = taxa_juros_anual / 365 / 100

#variavel juros recebe o calculo de juros para completar o valor da conta.
juros = valor_principal * taxa_juros_diaria * dias_atraso

#valor_total é uma variavel que recebe o resultado final e o armazena para poder apresenta-lo
valor_total = valor_principal + juros
#retorna o valor da variavel para onde a função foi chamada
return valor_total, juros

#valores são atribuidos as variaveis para que a conta seja efetuada.
valor_principal = 1000.00
taxa_juros_anual = 5.0
dias_atraso = 30
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso)
print(f"Valor total a ser pago: R${valor_total:.2f}") #mostra para o usuário qual o valor a ser pago com acréscimo do juros.
print(f"Valor dos juros: R${juros:.2f}") #mostra ao usuário apenas o valor do juros que foi acrescentado.