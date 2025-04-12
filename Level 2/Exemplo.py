eu = "professor frota"
clima = "sol"
atividade = "tomar sorvete"
ligacao_mamae = False

if (clima == "sol"):
    print(eu, "vai", atividade)
else:
    print(eu, "não vai", atividade, "ele vai ficar em casa codando.")
    
while atividade == "tomar sorvete":
    celular = "disponível"
    if (ligacao_mamae == True):
        celular = "mamae ligou"
        print (celular)
        celular = "Ocupado"
        break
    
    
if (celular == "disponível"):
    print("a carina pode me ligar")
elif (celular == "Ocupado"):
    print("sua chamada foi encaminhada para caixa postal, deixe uma mensagem após o sinal")
    print("beeeeep!")
        