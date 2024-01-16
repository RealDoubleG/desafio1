contatos = []

def ver_contatos(contatos):
  for indice, contato in enumerate(contatos, start=1):
    favorito = "✓" if contato["favorito"] else " "
    nome = contato["nome"]
    telefone = contato["telefone"]
    email = contato["email"]
    print(f"{indice}. [{favorito}] nome: {nome}, telefone: {telefone}, email: {email}")
  return

def atualizar_dados(nome, telefone, email, contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if(indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos)):
    contatos[indice_contato_ajustado]["nome"] = nome
    contatos[indice_contato_ajustado]["email"] = email
    contatos[indice_contato_ajustado]["telefone"] = telefone
    print("Contato atualizado")    
  else:
    print("Contato inexistente")
  return

def favoritar_desfavoritar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  status_contato_favorito = contatos[indice_contato_ajustado]["favorito"]
  if(status_contato_favorito):
    contatos[indice_contato_ajustado]["favorito"] = False
    print("Contato desfavoritado")
  else:
    contatos[indice_contato_ajustado]["favorito"] = True
    print("Contato favoritado")
  return

def deletar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  contato = contatos[indice_contato_ajustado]
  if(indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos)):
    contatos.remove(contato)
    print("Contato removido")    
  else:
    print("Contato inexistente")
  return

def criar_contato(nome, email, telefone, contatos):
  contato = {"nome": nome, "email": email, "telefone": telefone, "favorito": False }
  contatos.append(contato)
  print("contato adicionado")
  return  

while True:
  print("\n Gerenciador de contatos")
  print("1. Add contato")
  print("2. Ver contatos")
  print("3. Favoritar/defavoritar contato")
  print("4. Apagar contato")
  print("5. Editar contato")
  print("6. Sair")

  escolha = input("Digite a escolha: ")

  match escolha: 
    case "1":
      nome_contato = input("digite o nome do contato que quer adicionar: ")
      email_contato = input("digite o email do contato que quer adicionar: ")
      telefone_contato = input("digite o telefone do contato que quer adicionar: ")
      criar_contato(contatos=contatos, email=email_contato, nome=nome_contato, telefone=telefone_contato)
      print("Contato criado com sucesso")
    case "2":
      ver_contatos(contatos=contatos)
    case "3":
      indice_contato = input("Digite o indice do contato: ")
      favoritar_desfavoritar_contato(indice_contato=indice_contato, contatos=contatos)
    case "4":
      indice_contato = input("Digite o indice do contato")
      deletar_contato(indice_contato=indice_contato, contatos=contatos)
    case "5":
      indice_contato = input("digite o indice do contato que quer editar: ")
      nome_contato = input("digite o nome do contato que quer adicionar: ")
      email_contato = input("digite o email do contato que quer adicionar: ")
      telefone_contato = input("digite o telefone do contato que quer adicionar: ")
      
      atualizar_dados(indice_contato=indice_contato, contatos=contatos, email=email_contato, nome=nome_contato, telefone=telefone_contato)
    case "6":
      break
    case _: 
      print("Escolha uma opção existente")
      break
  
print("programa finalizado")


