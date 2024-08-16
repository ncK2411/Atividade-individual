def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios,
custo_pedagio): # define a função que vai calcular o custo da viagem para o usuário, processando todas as informações recebidas por parametro e fazendo todos os calculos desejados, no final retornando todos os resultados para o ponto onde foi chamada.

custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel

custo_pedagio_total = numero_pedagios * custo_pedagio

custo_total = custo_combustivel_total + custo_pedagio_total

return custo_total, custo_combustivel_total, custo_pedagio_total

#pega a informação fornecida pelo usuário e atribui cada uma a uma variavel, crucial para que o resultado seja exato.
distancia = float(input("Digite a distância da viagem (em km): "))
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): "))
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): "))
numero_pedagios = int(input("Digite o número de pedágios no percurso: "))
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): "))

#chama a função passando os parametros que serão ultilizados, para que os calculos sejam feitos.
custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia,
custo_combustivel,
consumo_veiculo, numero_pedagios,

custo_pedagio)

#informa ao usuário qual é o custo total de sua viagem de acordo com as informações fornecidas.
print(f"Custo total da viagem: R${custo_total:.2f}")
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}")
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}")