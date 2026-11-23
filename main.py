import os 

arquivo = open("arquivo.txt", mode="r+", encoding="utf-8")
compactado = open("compatactado.txt", mode="a+", encoding="utf-8")

txt = arquivo.readline()

def menu():
    while True:
        print("Menu do Sistema do Mini Compactador de arquivos de texto:\n(1) COMPACTAR\n(0) SAIR\n")
        op = int(input("Digite a opção: "))
        match(op):
            case 1:
                Compactar()
                break
            case _:
                print("Valor Inválido")


def Compactar():
    alfaNumerico = (
                    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
                    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 
                    "!", "@", "#", "$", "%", "&", "*", "?", "/", "°", "<", ">", " ", "ç", "Ç"
                )

    filtro = []
    for i in range(len(txt)):
        for j in range(len(alfaNumerico)):
            qnt = txt.count(alfaNumerico[j])
            if qnt != 0 and txt[i] == alfaNumerico[j] and (alfaNumerico[j] not in filtro):
                compactado.write(f"{qnt}{txt[i]}")
                filtro.append(alfaNumerico[j])
    compactado.write("\n")

menu()
