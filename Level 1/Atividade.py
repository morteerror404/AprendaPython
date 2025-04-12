# A sua missão é corrigir o erro do código (Preste atenção aos detalhes)

nome = "carteira"
quant_cartoes = 6
valor_notas = 77        
valor_moedas = 1.25

# Aqui temos a soma total de valores em espécie, mas temos um problema relacionado aos tipos de variaveis.
valortotal = valor_notas + valor_moedas 

print("A variavel nome é do tipo:", type(nome))
print("A variavel quant_cartoes é do tipo:", type(quant_cartoes)) 
print("A variavel valor_notas é do tipo:", type(valor_notas))
print("A variavel valor_moedas é do tipo:", type(valor_moedas))
print("A variavel valor_moedas é do tipo:", type(valortotal))
print ()

# aqui temos um problema, como podemos printar o valor total sem erro (DICA: pense fora da caixa, você pode alterar minhas variáveis) ?

print("o valor total de Notas e Moédas é: ", valortotal)


