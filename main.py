import time as t
import os as o


def Menu():
    while True:
        print("Menu do Sistema do Mini Compactador de arquivos de texto:\n(1) LER ARQUIVO\n(2) COMPACTAR\n(3) DESCOMPACTAR\n(4) COMPARAR\n(0) SAIR")
        op = input("Digite uma opção: ")
        print("")
        
        
        match(op):
            case "0":
                Sair(True)
                break
            case "1":
                Ler_Arquivo()
                break
            case "2":
                Compactar()
                break
            case "3":
                Descompactar()
                break
            case "4":
                Comparar()
                break
            case _:
                print("Valor Inválido\n")
                
def Ler_Arquivo():
    while True:
        print("Deseja abrir qual arquivo: \n(1) COMPACTADO\n(2) DESCOMPACTADO\n(0) SAIR")
        op = input("Digite uma opção: ")
        print("")


        match(op):
            case "0":
                Sair(False)
                break
            case "1":
                try:
                    compactado = open("compactado.txt", mode="r", encoding="utf-8")
                    print(f"Seu arquivo compactado:\n{compactado.read()}\n")
                    compactado.close()
                except FileNotFoundError:
                    print("O arquivo 'compactado.txt' ainda não existe!\n")
                Continuar()
                break
            case "2":
                try:
                    descompactado = open("descompactado.txt", mode="r", encoding="utf-8")
                    print(f"Seu arquivo descompactado:\n{descompactado.read()}\n")
                    descompactado.close()
                except FileNotFoundError:
                    print("O arquivo 'descompactado.txt' ainda não existe!\n")
                Continuar()
                break
            case _:
                print("Valor Inválido\n")

def Continuar():
    while True:
            print("Deseja Continuar?\n(1) Sim\n(0) Não")
            p = input("Digite uma opção: ")
            print("")
            
            match(p):
                case "0":
                    Desejo_Do_Usuario()
                    break
                case "1":
                    Ler_Arquivo()
                    break
                case _:
                    print("Valor Inválido\n")
                
            
def Desejo_Do_Usuario():
    while True:
        print("Deseja voltar ao menu?\n(1) Sim\n(0) Não")
        d = input("Digite uma opção: ")
        print("")
        
        match(d):
            case "0":
                Sair(True)
                break
            case "1":
                Sair(False)
                break
            case _:
                print("Valor Inválido\n")
                
                
def Descompactar():
    compactado = open("compactado.txt", "r+", encoding="utf-8")
    conteudo = compactado.read()
    compactado.close()
    descompactado = open("descompactado.txt", "w+", encoding="utf-8")
    qnt = ""


    for caractere in conteudo:
        if caractere.isdigit():
            qnt += caractere
        else:
            descompactado.write(caractere * int(qnt))
            qnt = ""

    descompactado.close()
    print("Arquivo Descompactado Com Sucesso!\n")
    Desejo_Do_Usuario()
    
    
def Sair(s):
    if s == True:
        print("Saindo do Sistema...")
        t.sleep(1)
    elif s == False:
        print("Voltando ao Menu...")
        t.sleep(1)
        Menu()


def Comparar():
    arq_ori = open("arquivo.txt", "r+", encoding="utf-8")
    txt_ori = arq_ori.read()
    arq_ori.close()
    arq_comp = open("compactado.txt", "r+", encoding="utf-8")
    txt_comp = arq_comp.read()
    arq_comp.close()

    cara_ori = len(txt_ori)
    cara_comp = len(txt_comp)
    bytes_ori= o.path.getsize("arquivo.txt")
    bytes_comp = o.path.getsize("compactado.txt")
    
    print("COMPARAÇÃO DE TAMANHO")
    print(f"Original: {cara_ori} caracteres e {bytes_ori} bytes")
    print(f"Compactado: {cara_comp} caracteres e {bytes_comp} bytes")


    if bytes_ori > 0:
        bytes_eco = ((bytes_ori - bytes_comp) / bytes_ori) * 100
        carac_eco = ((cara_ori - cara_comp)/ bytes_ori) * 100
        print(f"Diferença: {bytes_ori - bytes_comp} bytes ({bytes_eco:.2f}% de redução)")
        print(f"Diferença: {cara_ori - cara_comp} bytes ({carac_eco:.2f}% de redução)\n")
    
    Desejo_Do_Usuario()
        

def Compactar():
    arquivo = open("arquivo.txt", mode="r+", encoding="utf-8")
    txt = arquivo.read()
    compactado = open("compactado.txt", "w+", encoding="utf-8")
    
    if len(txt) > 0:
        qnt = 1
        carac = txt[0]
        for i in range(1, len(txt)):
            if txt[i] == carac:
                qnt += 1
            else:
                compactado.write(f"{qnt}{carac}")
                carac = txt[i]
                qnt = 1
        compactado.write(f"{qnt}{carac}")
    compactado.close()
    print("Arquivo Compactado Com Sucesso!\n")
    Desejo_Do_Usuario()

Menu()
