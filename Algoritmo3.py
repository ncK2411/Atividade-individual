def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial): #defini a função diagnosticar_diabetes com duas passagens de parametros.

if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200: # coloca uma condição para que seje retornado um certo valor, sendo ele positivo ou negativo.
return "Diabetes"
elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200: # coloca uma contra posição indicando um resultado contrarioa condição do (if).
return "Pré-diabetes"
else:
return "Normal"

#pede dois dados so usuário para que sejam atribuidos a duas diferentes variaveis.
glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): "))
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))

#efetua a conta e mostra o resultado na tela para o usuário.
resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial)
print(f"O diagnóstico é: {resultado}")