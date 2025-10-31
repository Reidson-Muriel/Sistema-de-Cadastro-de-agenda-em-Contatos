
from sistema.excluir import excluir
from sistema.cadastro import cadastrar
from sistema.formatacao import formatar
from sistema.lista import *
from sistema.arquivo import *
from sistema.buscar import buscar_dados, cadastrar
from sistema.editar import editar
arq = "listaPessoa.txt"
if not arqExiste(arq):
    criar(arq)
def menu():
    while True:
        formatar("Menu-Cadastro de Contatos")
        print(f"1-Cadastrar\n2-listar\n3-Buscar\n4-Editar\n5-Excluir\n6-Sair do sistema")
        print("-"*30)
        try:
            opcao = int(input("Digite a opcao: "))
        except ValueError:
            print("\033[31mErro, somente numero da opcao\033[0m")
        except KeyboardInterrupt:
            print("\033[33mUsuario selecionou tecla copiar sem querer\033[0m")
            continue
        
        
        if opcao == 1:
            cadastrar(arq)
        elif opcao == 2:
            listar(arq)
        elif opcao == 3:
                try:
                    buscar_dados(arq)
                except KeyboardInterrupt:
                    print(f"\033[33mUsuario tentou clicar no ctrl + c para copiar\033[0m")
        elif opcao == 4:
            editar(arq)
        elif opcao == 5:
            excluir(arq)
        elif opcao:
            if opcao == 6:
                print("Encerrando com Sucesso!")
                break
            else:
                print("nao temos esse opcao")
                continue 
