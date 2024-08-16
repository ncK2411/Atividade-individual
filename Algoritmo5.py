def calcular_imc(peso, altura): #definição da função que executara o programa/ contas do algoritmo.

#atribui valor a variavel que irá armazenar o imc do usuário, retornando esse resultado para o ponto onde a função foi chamada.
imc = peso / (altura ** 2)
return imc

def classificar_imc(imc): #definição de uma outra função, responsavel por outra parte do algoritmo.

#definição da condição para os imc de pessoas que estão no peso ideal, abaixo ou acima dele, retornando o resultado esperado.
if imc < 18.5:
return "Abaixo do peso"
elif 18.5 <= imc < 24.9:
return "Peso normal"
elif 25 <= imc < 29.9:
return "Sobrepeso"
elif 30 <= imc < 34.9:
return "Obesidade grau 1"
elif 35 <= imc < 39.9:
return "Obesidade grau 2"
else:
return "Obesidade grau 3"

def sugestao_atividade_fisica(classificacao_imc): # definição de nova função para recomendação de algo ao usuário.

#É atribuido um resultado diferente  de acordo com o resultado do imc do usuário, retornando sugestões diferentes para cada caso.
if classificacao_imc == "Abaixo do peso":
return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em
proteínas e calorias."
elif classificacao_imc == "Peso normal":
return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e
natação, junto a um treino de força moderado."
elif classificacao_imc == "Sobrepeso":
return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além
de exercícios de resistência."
elif classificacao_imc == "Obesidade grau 1":
return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um
programa de reeducação alimentar."
elif classificacao_imc == "Obesidade grau 2":
return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e
acompanhamento nutricional."
else:
return "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica,
fisioterapia, e consultas regulares com um nutricionista."

#variaveis tem valores atribuidos pelo usuário, para que os calculos de imc sejam feitos.
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

#funções são chamadas para que todas as contas e resultados sejam processados e informados ao usuário.
imc = calcular_imc(peso, altura)
classificacao_imc = classificar_imc(imc)
sugestao = sugestao_atividade_fisica(classificacao_imc)

#É informado na tela do usuário seu imc, classificação(como sobre peso, ideal ou abaixo) e uma sugestão para a melhora do caso ou mantelo como está.
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao_imc}")
print(f"Sugestão de atividade física: {sugestao}")