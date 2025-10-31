
import copy
from more_itertools import strip
from sistema.arquivo import leitura
from sistema.cadastro import cadastrar, lista_cadastro, mostrar

def buscar_dados(arquivo):
   while True:
      try:
         nome = input("Digite o nome que deseja buscar ou 'sair'>> ").strip()
         if nome.lower() == "sair" or nome.lower() == "s":
            print("Saindo de busca...")
            break

         leitura(arquivo)
         lista_busca = []
         for registro in lista_cadastro:
            if nome.lower() in registro[1].lower():
               lista_busca.append(registro)

         if lista_busca:

            mostrar(lista_busca, "Dados filtrado")
         else:
            print("Contato não encontrado")
            while True:
               opc = input("Deseja cadastrar novo contato? [s/n]>> ").strip().lower()
               if opc == "s":
                  cadastrar(arquivo)
                  continue
               else:
                  break
            while True:
                  continuar = input("Deseja buscar outro contato [s/n] >>").strip().lower()
                  if continuar in ("s", "n"):
                     break
                  print("Responde somente 's' ou 'n'")
                  if continuar == "n":
                     print("Saindo da busca...")
                     break

      except KeyboardInterrupt:
         print("usuario tentou copiar na tecla ctrl + 'c' sem querer")
    

