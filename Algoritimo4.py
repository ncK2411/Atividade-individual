def calcular_media_e_aprovacao(notas, nota_minima_aprovacao): # definia função que será ultilizada no código.
total_notas = 0 #atribui um valor inicial as variaveis.
num_alunos = len(notas)
aprovados = []
reprovados = []

#coloca uma condição que levara para certos resultados dependendo do valor informado.
for aluno, nota in notas.items():
total_notas += nota
if nota >= nota_minima_aprovacao: #recebe tal condição, para que possa passar uma informação adiante.
aprovados.append(aluno)
else: #uma contraposição que informa um resultado diferente o esperado.
reprovados.append(aluno)

media_turma = total_notas / num_alunos # valor do calculo/ conta feita é atribuido a uma variavel que vai guardar tal informação

#retorno de resultado por meio de uma função criada anteriormente.
return media_turma, aprovados, reprovados

#tabela feita com nome e nota dos alunos.
notas = {
"Alice": 85,
"Bruno": 72,
"Carlos": 60,
"Diana": 95,
"Eduardo": 55
}

#atribuição de valor a variavel que será usada como nota exemplo/ nota de corte.
nota_minima_aprovacao = 70

#passagem de parametros para a função.
media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)

#impresão na tela do usuário com alunos aprovados, reprovados e a média da turma.
print(f"Média da turma: {media_turma:.2f}")
print(f"Alunos aprovados: {', '.join(aprovados)}")
print(f"Alunos reprovados: {', '.join(reprovados)}")