import os 

arquivo = open("arquivo.txt", mode="r+", encoding="utf-8")

txt = arquivo.read()

def menu():
    while True:
        print("Menu do Sistema do Mini Compactador de arquivos de texto:\n(0) SAIR\n(1) LER ARQUIVO\n(2) COMPACTAR\n(3) DESCOMPACTAR\n")
        op = int(input("Digite a opção: "))
        match(op):
            case 0:
                #sair()
                break
            case 1:
                #ler_arquivo()
                break
            case 2:
                Compactar()
                break
            case 3:
                #Descompactar()
                break
            case 4:
                #Salvar()
                break
            case _:
                print("Valor Inválido")


def Compactar():
    with open("compactado.txt", "w", encoding="utf-8") as compactado:
        qnt = 1
        caractere = txt[0]
        for i in range(1, len(txt)):
                if txt[i] == caractere:
                    qnt += 1
                else:
                    compactado.write(f"{qnt}{caractere}")
                    caractere = txt[i]
                    qnt = 1
        compactado.write(f"{qnt}{caractere}")

menu()
