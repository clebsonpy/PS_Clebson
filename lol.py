def cadastro(dadosUsuario):

	dicUsuario = {'usuario': dadosUsuario[0], 
				'email': dadosUsuario[1], 
				'nome': dadosUsuario[2], 
				'funcao': dadosUsuario[3]}
	return dicUsuario

def entradaDadosUsuario():
	usuario = input("Usuario: ")
	email = input("E-mail: ")
	nome = input("Nome: ")
	funcao = input("Funcao: ")

	return usuario, email, nome, funcao

if __name__ == '__main__':
 	dadosUsuario = entradaDadosUsuario()
 	print(cadastro(dadosUsuario))