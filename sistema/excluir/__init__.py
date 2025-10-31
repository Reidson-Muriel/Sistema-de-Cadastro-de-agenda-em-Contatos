
from ..arquivo import salvar
from ..cadastro import mostrar


def excluir(txt):
    from sistema.arquivo import leitura
    from sistema.cadastro import lista_cadastro
    leitura(txt)
    if not lista_cadastro:
        print("Nenhum contato encontrado para excluir ")
        return
    mostrar(lista_cadastro)

    id_excluir = input("Digite o Id que deseja excluir >> ")

    nova_lista = []
    cont = 0
    for cont in lista_cadastro:
        if cont[0] != id_excluir:
            nova_lista.append(cont)

    if len(nova_lista) == len(lista_cadastro):
        print("Contato nao encontrado")
        return
    
    lista_atualizado = []
    for novoId, cont in enumerate(nova_lista, start=1):
        novo_id = (str(novoId),)+cont[1:]
        lista_atualizado.append(novo_id)

    lista_cadastro.clear()
    lista_cadastro.extend(lista_atualizado)

    with open(txt, "w") as arquivo:
        for cont in lista_cadastro:
            salvar(arquivo, *cont)
    print("Contato excluido com sucesso")