import sys
from sistema.formatacao import formatar_tabela
from sistema.arquivo import salvar
from time import sleep

lista_cadastro = list()



def novo_cadastro(id, nome, idade, telefone, email, endereco, observacao):
        dupla = (id, nome, idade, telefone, email, endereco, observacao)
        lista_cadastro.append(dupla)
        print(f"\033[32mAdicionado com sucesso!\033[0m")
def cadastrar(arq):
    id = len(lista_cadastro) + 1
    while True:
        texto = "Correto"
        try:
            nome = str(input("digite o nome: ")).strip()
            if nome == "":
                print("nao pode ser vazio")
                continue
            break
        except KeyboardInterrupt:
            print("\033[33mUsuario preferiu não colocar o nome\033[0m")
            return  

    while True:   
        try:
            idad = input("Digite a idade: ")
            idade = int(idad)   
            print("\033[32m" + texto + "\033[0m", end="")
            sys.stdout.flush()
            sleep(1)
            sys.stdout.write("\r" + " " * len(texto) + "\r")
            sys.stdout.flush()
            break
        except ValueError:
            print("\033[31mErro, somente em numero\033[0m")
        except KeyboardInterrupt:
            print("\033[33mUsuario preferiu nao colocar nada\033[0m")
            return
        
    while True:
        try:
            fone = input("Digite o numero do Telefone: ")
            if not fone.isdigit() or len(fone) != 11:
                print("\033[31mError, deve conter 11 numero, DDD + numero\033[0m")
                continue
            else:
                ddd = fone[0:2]
                numero = fone[2:]
                telefone = f"({ddd}){numero[0]}  {numero[1:5]}-{numero[5:]}"
                print("\033[32m" + texto + "\033[0m", end="")
                sys.stdout.flush()
                sleep(1)
                sys.stdout.write("\r"+ " " * len(texto) + "\r")
                sys.stdout.flush()
                break
        except ValueError:
            print(f"\033[31mErro, somente em numero\033[0m")
        except KeyboardInterrupt:
            print("\033[33mUsuario preferiu não colocar\033[0m")
            break
        
    while True:
        try:
            nome_email = input("Digite o E-mail: ")
            email = str(nome_email)
            if "@" not in email or "." not in email.split("@")[-1]:
                print(f"\033[31mError, deve conter '@' e depois '.'\033[0m")
                continue
            else:
                print("\033[32m"+ texto +"\033[0m", end="")
                sys.stdout.flush()
                sleep(1)
                sys.stdout.write("\r" + " " * len(texto)+ "\r")
                sys.stdout.flush()
                break
        except ValueError:
            print("\033[31mErro, somente em numero\033[0m")
        except KeyboardInterrupt:
            print("\033[33mUsuario preferiu não colocar")
            break
        
    endereco = str(input("Digite o Endereço")) 
    observacao = str(input("Digite a OBS: "))
    salvar(arq,id, nome, idade, telefone, email, endereco, observacao)
    novo_cadastro(id, nome, idade, telefone, email, endereco, observacao)


def mostrar(txt, titulo="Dados Cadastrado"):
    res = sorted(txt, key=lambda x: x[0].lower())
    if not txt:
        print("Nenhum registro para exibir")
        return 
    formatar_tabela(titulo)
    print(f"{'Id':^5}{'Nome':^15}|{'Idade':^10}|{'Telefone':^25}|{'Email':^25}|{'Endereco':^25}|{'Observação':^30}")
    print("-"*130)

    for id, nome, idade, telefone, email, endereco, observacao in res:
        print(f"{id:^5}{nome:^15}|{idade:^10}|{telefone:^25}|{email:^25}|{endereco:^25}|{observacao:^30}")
    