from sistema.arquivo import leitura, salvar
from sistema.cadastro import mostrar, lista_cadastro

def editar(arq):
        leitura(arq)
        if not lista_cadastro:
            print("Nenhum contato cadastrado para editar")
            return
        mostrar(lista_cadastro, "Contatos cadastrados")

        usuario = input("Digite o Id da lista do contato que deseja editar-los >> ").strip() 
        
        encontrado = False
        for indice, (id, nome, idade , telefone, email, enderenco, observacao) in enumerate(lista_cadastro):
            if id == usuario:
                encontrado = True     
                print("Contato encontrado!")

                novo_nome = input(f"Edita o nome [{nome}]: ") or nome
                nova_idade = input(f"Edita a idade [{idade}]: ") or idade
                novo_tel = input(f"Edita o telefone [{telefone}]: ") or telefone
                novo_email = input(f"Edita o email [{email}]: ") or email
                novo_end = input(f"Edita o enderenco [{enderenco}]: ") or enderenco
                novo_obs = input(f"Edita a observacao [{observacao}]: ") or observacao
                lista_cadastro[indice] = (id, novo_nome, nova_idade, novo_tel, novo_email, novo_end, novo_obs)
                with open(arq, "w") as arquivo:
                    for cont in lista_cadastro:
                        salvar(arquivo, *cont)
                print("Contato atualizado com sucesso!")
                break   

        if not encontrado:
             print("Contato nao encontrado")
