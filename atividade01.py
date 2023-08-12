# Resposta das atividades

 1 .Escreva um script python que define duas variáveis do tipo inteiro (int) e atribui um valor positivo para elas. Imprima as duas variáveis.
 Resposta:
 num1 = 10
  num2 = 5
  print(num1,num2)

2. Seja x = 2 + 4j, descubra qual é tipo associado a essa variável pelo interpretador.
Resposta : classe complexa.

3. Experimente a inicialização de variáveis como segue:

urnas = {}
sessao = {"escola municipal", 103}
descubra qual é o tipo da variável urnas e da variável sessao. Explique se necessário a razão dos tipos serem distintos.

Resposta: dicionários e conjuntos. O primeiro guarda valores por chave-valores e o segundo é uma lista de lementos que nao permite duplicatas em seus valores.


4.Nas definições de nomes de variáveis abaixo quais têm nomes válidos e quais são invalidos

ola = "mundo" = válido
_ola = "mundo" = válido
_1_ola = "mundo" =  válido
1_ola = "mundo" = inválido
ola_1 = "mundo"  = válido
meu mundo = "ola" = inválido
aponte as razões para os nomes inválidos, indicando o item e a razão da violação das regras de nomeação de variável.
No numero 4 não pode iniciar variaveis com numeros. No numero 6 não podem conter espaços. Se tiver deve ser feito por meu_mundo ou meuMundo.

5.No seguinte comando de atribuição
casa, senha = "minha", "ola"
casa, senha = "minha"
casa = "minha"
Quais foram as atribuições que funcionaram e quais não funcionaram? Explique a razão dos problemas.
Resposta :
válido. Cada variavel retornou seu valor correspondente.
inválido. Esperava mais argumentos.
válido.

6. Considere as seguintes operações matemáticas, e indique o resultado de cada uma:

(10 - 6)**2
10 - 6**2
10 - 3 // 2
10 - 3 / 2
Resposta:
# 16
# -26
# 9
# 8.5

7.Qual a importância de se criar ambiente virtuais para o desenvolvimentos de projetos usando Python?
Resposta:
Para caso seja necessário instalar pacotes ou realizar alterações especificas, as mudanças fiquem somente nesse ambiente, não necessáriamente levando as alterações para outros projetos.

8.Descubra e responda qual versão do python está instalado no seu ambiente de desenvolvimento. Que comando você usou para obter essa informação?
Resposta:
python --version
Python 3.11.4

9.Uma tupla é um tipo imutável, portanto qualquer variável desse tipo pode ser alterada desde que os seus elementos sejam individualizados, como no código abaixo:

comprado = ("carro", "GM", "20K")

comprado[1] = "Ford"

você concorda com essa afirmação? justifique sua resposta.
Resposta: Não podemos atribuir informações aos  elementos da tupla separadamente,uma vez ela declarada. O que pode ser feito caso seja necessário é reescrever a tupla raiz, coma informação alterada.


10. Considere o código abaixo:

numero = input()

print(numero*3)

se o valor 3(três) for informado como entrada e armazenado na variável número.
Resposta:
numero = input(3)
print(numero*3)
#O resultado será 3.

11.Revise o código disponibilizado em src/primeiro.py. Em seguida altere o programa para que ele se torne generalista, i.e., aceite qualquer quantidade de notas que cada aluno pode ter.
Resposta: 


