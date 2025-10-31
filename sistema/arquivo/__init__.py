
def  arqExiste(nome):
    try:
        abre = open(nome, 'rt')
        abre.close()
        return True 
    except FileNotFoundError:
        return False
         
def criar(nome):
    try:
        abre = open(nome, 'wt+')
        abre.close()
    except:
        print("\033[31mHouve o erro na criação\033[0m")
    else:
        print(f"\033[32mArquivo {nome} criado com Sucesso!\033[0m")

def salvar(arq, id, nome, idade, telefone, email, endereco, observacao):
        linha = (f"{id};{nome};{idade};{telefone};{email};{endereco};{observacao}\n")
        if isinstance(arq, str):
            with open(arq, "a") as arquivo:
                arquivo.write(linha)
        else:
            arq.write(linha)
    
def leitura(arq):
    from sistema.cadastro import lista_cadastro
    with open(arq, "rt") as arquivo:
        lista_cadastro.clear()
        vazio = True
        for linha in arquivo:
            if linha == "" or ";" not in linha:
                continue
            vazio = False
            id, nome, idade, telefone, email, endereco, observacao = linha.split(";")
            exite = False
            for cadastro in lista_cadastro:
                if cadastro[3] == telefone:
                    exite = True
                    break
            if not exite:
                lista_cadastro.append((id, nome, idade, telefone, email, endereco, observacao))

            




