
def adicionar_contato(nome_contato, telefone, email):
    contato = {"nome": nome_contato, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome_contato} adicionado com sucesso!")
    return

def ver_lista_contatos(contatos):
    print("Lista de Contatos: ")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "⭐" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"[{indice}].[{favorito}] [Nome: {nome_contato}] [Tel: {telefone}] [E-mail: {email}]")
    return

def editar_contato(indice_contato, novo_nome_contato, novo_telefone, novo_email):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len (contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome_contato
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone
        contatos[indice_contato_ajustado]["email"] = novo_email
        print(f"Nome de contato: {nome_contato} atualizado para {novo_nome_contato}")
        print(f"Telefone: {telefone} atualizado para {novo_telefone}")
        print(f"E-mail: {email} atualizado para {novo_email}")
    else:
        print("Índice de contato errado")
    return

def marcar_desmarcar_favorito(indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len (contatos):
        contatos[indice_contato_ajustado]["favorito"] = True
        print(f"Contato {indice_contato} favoritado!")
    return

def ver_lista_contatos_favoritos(contatos):
    print("Lista de Contatos Favoritos: ")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"] == True:
            favorito = "⭐" if contato["favorito"] else " "
            nome_contato = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            print(f"[{indice}].[{favorito}] [Nome: {nome_contato}] [Tel: {telefone}] [E-mail: {email}]")
    return

def apagar_contato(indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len (contatos):
        contatos.pop(indice_contato_ajustado)
    return

contatos = []
while True:
    print("1. Adicionar Contato")
    print("2. Visualizar Lista de Contatos")
    print("3. Editar Contato")
    print("4. Marcar/Desmarcar Favorito")
    print("5. Lista de Contatos Favoritos")
    print("6. Apagar contato")
    print("7. Sair do Programa")

    escolha = input("Digite a opção que deseja: ")

    if escolha == "1":
        nome_contato = input("Digite o Nome do Contato: ")
        telefone = input("Digite o telefone do Contato: ")
        email = input("Digite o E-mail do Contato: ")
        adicionar_contato(nome_contato, telefone, email)
    
    elif escolha == "2":
        ver_lista_contatos(contatos)

    elif escolha == "3":
        ver_lista_contatos(contatos)
        indice_contato = input("Digite o qual contato você deseja atualizar: ")
        novo_nome_contato = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")
        novo_email = input ("Digite o novo E-mail do contato:")
        editar_contato(indice_contato, novo_nome_contato, novo_telefone, novo_email)

    elif escolha == "4":
        ver_lista_contatos(contatos)
        indice_contato = input("Digite o qual contato você deseja atualizar: ")
        marcar_desmarcar_favorito(indice_contato)
    
    elif escolha == "5":
        ver_lista_contatos_favoritos(contatos)

    elif escolha == "6":
        ver_lista_contatos(contatos)
        indice_contato = input("Digite o contato que deseja apagar: ")
        apagar_contato(indice_contato)

    elif escolha == "7":
        print("Fechando programa...")
        break