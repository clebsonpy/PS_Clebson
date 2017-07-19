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

def cadastroRecurso(dadosRecurso):
	

def printMenu(dicFuncoes, tipo = ''):
	print('%s: ' % tipo)
	for i in dicFuncoes:
		print('%s - %s' % (i, dicFuncoes[i]))
	opcao = input('Digite a opção: ')
	while opcao == '':
		print('Opção Invalida!')
		opcao = input('Digite a opção: ')
	return int(opcao)

def entradaDadosUsuario(usuarios):
	usuario = input("Usuário: ")
	while (usuario in usuarios or usuario == ""):
		print('Usuário Invalido!')
		usuario = input("Usuário: ")
	email = input("E-mail: ")
	while email == "":
		print('Email invalido!')
		email = input("E-mail: ")
	nome = input("Nome: ")
	while nome == "":
		print('Nome Invalido!')
		nome = input("Nome: ")

	dicTipoUsuario = {1: 'Aluno', 2: 'Professor', 3: 'Administrador', 4: 'Pesquisador'}
	tipoUsuarioId = printMenu(dicFuncoes=dicTipoUsuario, tipo = 'Tipo de Usuário:')
	if dicTipoUsuario[tipoUsuarioId] == 'Aluno':
		dicAluno = {1: 'Graduação', 2: 'Mestrado', 3: 'Doutorado'}
		tipoAluno = printMenu(dicFuncoes=dicAluno, tipo = 'Tipo de Aluno:')
		tipoUsuario = 'Aluno de ' + dicAluno[tipoAluno]
	else:
		tipoUsuario = dicTipoUsuario[tipoUsuarioId]
	dadosUsuario = (usuario, email, nome, tipoUsuario)
	usuarios[usuario] = cadastro(dadosUsuario=dadosUsuario)
	return usuarios

def alocacaoRecurso(recursos, usuarios):
	tipoDeRecursos = {1: 'Sala de Aula',
					2: 'Laboratórios',
					3: 'Auditório',
					4: 'Projetores'}

	usuario = input("Usuário Responsável")
	while not usuario in usuarios:
		print('Usuário não existe!')
		usuario = input("Usuário Responsável")
	if usuarios[usuario]['funcao'].split("")[0] == 'Aluno':
		print('Usuário não pode alocar recursos!')
		return recursos

	recurso = tipoDeRecursos[printMenu(tipoDeRecursos, tipo = 'Alocação de:')]
	identificacao = input("Código de Identificação: ")
	while identificacao == '':
		print('Digite o Código de Identificação!')
		identificacao = input("Código de Identificação: ")
	data = data_hora()

	return identificacao, data[0], data[1]

def menu():
	opcoes = {1: 'Cadastro de Usuário',
			2: 'Alocação de Recursos',
			9: 'Sair'}
	opcao = printMenu(opcoes, tipo = 'Deseja realizar: ')
	return opcao

if __name__ == '__main__':
	opcao = menu()
	usuarios = {'baldoino':{'usuario': 'baldoino',
							'email': 'baldoino@algo.com',
							'nome': 'Baldoino Fonseca',
							'funcao': 'Professor'},
				'clebsonpy':{'usuario': 'clebsonpy',
							'email': 'clebson2007.farias@gmail.com',
							'nome': 'Clebson Carvalho',
							'funcao': 'Aluno de Graduação'}}
	recursos = {}
	while(opcao != 9):
		if opcao == 1:
			usuarios = entradaDadosUsuario(usuarios)
		elif opcao == 2:
			recursos = entradaDadosRecurso(recursos)
		opcao = menu()
	print(usuarios)
