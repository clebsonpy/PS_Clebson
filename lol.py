import datetime

def data_hora():
	data_hora_inicio = datetime.datetime.strptime(input('Data e Hora(AAAA/MM/DD hh:mm): '), '%d/%m/%Y %H:%M')
	data_hora_fim = datetime.datetime.strptime(input('Data e Hora(AAAA/MM/DD hh:mm): '), '%d/%m/%Y %H:%M')
	return data_hora_inicio, data_hora_fim

def cadastro(dadosUsuario):
	dicUsuario = {'usuario': dadosUsuario[0],
				'email': dadosUsuario[1],
				'nome': dadosUsuario[2],
				'funcao': dadosUsuario[3]}
	return dicUsuario

def entradaDadosUsuario(atividade, usuarios=None, recursos=None):
	if atividade == 1:
		usuario = input("Usuário: ")
		while usuario in usuarios:
			print('Usuário Invalido!')
			usuario = input("Usuário: ")
		email = input("E-mail: ")
		nome = input("Nome: ")
		funcao = input("Função: ")
		dadosUsuario = (usuario, email, nome, funcao)
		usuarios[usuario] = cadastro(dadosUsuario=dadosUsuario)
		return usuarios

	elif atividade == 2:
		identificacao = input("Identificação: ")
		usuario = input("Usuário Responsável")
		data = data_hora()
		return identificacao, data[0], data[1]

def menu():
	print('1 - Cadastro de Usuário')
	print('2 - Registrar Novo Recurso')
	print('0 - Sair')
	opcao = int(input("Digite a opção desejada: "))
	return opcao

if __name__ == '__main__':
	opcao = menu()
	usuarios = {}
	recursos = {}
	while(opcao != 0):
		usuarios = entradaDadosUsuario(opcao, usuarios)
		opcao = menu()
