# em produção aguarde

nome_usr = "Professor Frota"
id_conta = 21
c_debito = True
c_credito = False
c_outro = False
din_conta = 720.46
din_fisico = 46.00
result = ""
# pode copiar essa função, não sou carrasco :P 
def printMenu():
    print("")
    print("Olá ", nome_usr)
    print("")
    print("Menu principal. (digite 0 para voltar aqui)")
    print("1. Sacar") 
    print("2. Depositar") 
    print("3. Pedir cartão de débito")
    print("4. Pedir cartão de crédito")
    print("5. Pedir cartão de outro tipo")  
    print("")
    print("Qual operação quer realizar hoje? ")

def printConfirma():
    print("Tem certeza que deseja realizar essa operação ? ")
    print("1. Sim")
    print("2. Não")

printMenu()
if result == "0":
    printMenu()
    result = input()
elif result == "1":
    usr_valor = input ("Digite valor deseja sacar : ")
    printConfirma()
    usr_resposta = input()
    if usr_resposta == "1":
        din_conta = din_conta - usr_valor
        din_fisico = din_fisico + usr_valor
    else:
        print("Tudo bem, voltando para o menu...")
        print("")
        printMenu()
        result = input()