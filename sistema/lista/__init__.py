from sistema.cadastro import *
from sistema.formatacao import aviso
def listar(nome):
    try:
        with open(nome, 'rt') as arquivo:
            lista_cadastro.clear()
            vazio = True
            escreva = ""
            for linha in arquivo:
                linha = linha.strip()
                if linha == "" or ";" not in linha:
                    continue
                vazio = False
                id, nome, idade, telefone, email, endereco, observacao = linha.split(";")
                exite = False
                for cadastro in lista_cadastro:
                    if cadastro == telefone:
                        exite = True
                        break
                if not exite:
                    lista_cadastro.append((id, nome, idade, telefone, email, endereco, observacao))
                else:
                    print(f"\033[33mEsse numero ja contem, cite a sua propria!\033[0m")

    except Exception as erro:
        print(f"\033[31mErro ao ler o arquivo {erro}!")
    else:   
        mostrar(lista_cadastro)
        if escreva != "":
            aviso(escreva)
        else:
            lista_cadastro
