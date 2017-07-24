import datetime
import pytz
from matplotlib.mlab import rec2csv


def data_hora():
    print('Formato de entrada: (DD/MM/AAAA hh:mm)')
    tz = pytz.timezone('America/Maceio')
    data_hora_inicio = datetime.datetime.strptime(input('Data e Hora - Inicio: ') +
                                                  ' -0300', '%d/%m/%Y %H:%M %z')
    while data_hora_inicio == "" or data_hora_inicio < datetime.datetime.now(tz=tz):
        print('Data e Hora inicio invalida!')
        data_hora_inicio = datetime.datetime.strptime(input('Data e Hora - Inicio: ') +
                                                      ' -0300', '%d/%m/%Y %H:%M %z')

    data_hora_fim = datetime.datetime.strptime(input('Data e Hora - Fim: ') +
                                               ' -0300', '%d/%m/%Y %H:%M %z')
    while data_hora_fim == "" or data_hora_fim < data_hora_inicio:
        print('Data e Hora fim invalida!')
        data_hora_fim = datetime.datetime.strptime(input('Data e Hora - Fim: ') +
                                                   ' -0300', '%d/%m/%Y %H:%M %z')

    return data_hora_inicio, data_hora_fim


def cadastro(dadosUsuario):
    dicUsuario = {'usuario': dadosUsuario[0],
                  'email': dadosUsuario[1],
                  'nome': dadosUsuario[2],
                  'funcao': dadosUsuario[3],
                  'recurso': []}
    return dicUsuario

def cadastroAtividade(dadosAtividade):
    dicAtividade = {'tipoAtividade': dadosAtividade[0],
                    'titulo': dadosAtividade[1],
                    'descricao': dadosAtividade[2],
                    'participantes': dadosAtividade[3],
                    'materialApoio': dadosAtividade[4]}
    return dicAtividade

def cadastroRecurso(dadosRecurso):
    dicRecurso = {'responsavel': dadosRecurso[0],
                  'identificacao': dadosRecurso[1],
                  'tipoRecurso': dadosRecurso[2],
                  'dataInicio': dadosRecurso[3],
                  'dataFim': dadosRecurso[4],
                  'status': dadosRecurso[5],
                  'atividade': 'Sem'}
    return dicRecurso

def verificaUsuario(dicUsuarios):
    usuario = input('Usuário: ')
    dicOpcoes = {1: 'Entrar com outro usuário',
                 2: 'Cadastar usuário'}

    while not usuario in dicUsuarios:
        opcao = printMenu(dicOpcoes, tipo='Usuário Invaliido!')
        if opcao == 1:
            usuario = input('Usuário: ')
        elif opcao == 2:
            dicUsuarios = entradaDadosUsuario(dicUsuarios)
            usuario = input('Usuário: ')

    return usuario

def verificaRecurso(dicRecursos):
    tipoDeRecursos = {1: 'Sala de Aula',
                      2: 'Laboratórios',
                      3: 'Auditório',
                      4: 'Projetores'}

    recurso = tipoDeRecursos[printMenu(tipoDeRecursos, tipo='Qual recurso')]
    identificacao = input("Código de Identificação: ")
    while not (recurso, identificacao) in dicRecursos:
        print('Recurso não encontrado!')
        dicOpacoes = {1: 'Mostrar todos os Recursos',
                      2: 'Tente novamente'}
        opcao = printMenu(dicOpacoes)
        if opcao == 1:
            exibirRecursos(dicUsuarios)
        elif opcao == 2:
            verificaRecurso(dicRecursos)

    return recurso, identificacao


def alterarStatusRecurso(dicRecursos, dicUsuarios, usuario):
    dicStatus = {1: 'Alocado',
                 2: 'Em Andamento',
                 3: 'Concluído'}
    chaveRecurso = verificaRecurso(dicRecursos)
    #usuario = verificaUsuario(dicUsuarios)
    status = printMenu(dicStatus, 'Alterar Status para')
    if status == 1 and dicRecursos[chaveRecurso]['status'] == 'Em processo de alocação':
        if dicUsuarios[usuario]['funcao'] == 'Administrador':
            dicRecursos[chaveRecurso]['status'] = dicStatus[status]
            print('Status alterado com sucesso!')
            return dicRecursos
        else:
            print('Status não pode ser alterado!')
            return dicRecursos

    elif status == 2 and dicRecursos[chaveRecurso]['status'] == 'Alocado':
        for rec in dicRecursos:
            if dicRecursos[rec]['status'] == 'Em Andamento' and dicRecursos[rec]['responsavel'] == usuario:
                print('Usuário contém recurso em andamento!')
                return dicRecursos

        if dicUsuarios[usuario]['funcao'] == 'Administrador' or dicUsuarios[usuario]['usuario'] == usuario:
            dicRecursos[chaveRecurso]['atividade'] = atividade(dicUsuarios, dicRecursos[chaveRecurso])
            dicRecursos[chaveRecurso]['status'] = dicStatus[status]
            print('Status alterado com sucesso!')
            return dicRecursos
        else:
            print('Usuário não pode alterar recurso!')
            return dicRecursos

    elif status == 3 and dicRecursos[chaveRecurso]['status'] == 'Em Andamento':
        if dicUsuarios[usuario]['funcao'] == 'Administrador':
            dicRecursos[chaveRecurso]['status'] = dicStatus[status]
            print('Status alterado com sucesso!')
            return dicRecursos
        else:
            print('Usuário não pode alterar recurso!')
            return dicRecursos

    else:
        print('Status não pode ser alterado!')
        return dicRecursos

def consultarUsuario(dicUsuarios, dicRecursos):
    dic = {'email': 'E-mail',
           'nome': 'Nome',
           'usuario': 'Usuário',
           'funcao': 'Função',
           'recurso': 'Recurso Alocados:'}
    usuario = verificaUsuario(dicUsuarios)
    print('==========%s==========' % usuario)
    for aux in dicUsuarios[usuario]:
        if aux == 'recurso':
            print(dic[aux])
            for recurso in dicUsuarios[usuario][aux]:
                ativ = dicRecursos[recurso]['atividade']
                if ativ == 'Sem':
                    print('%s (%s)' % recurso)
                    print('Atividade: %s' % ativ)
                else:
                    print('%s (%s)' % recurso)
                    print('Atividade: %s' % ativ['tipoAtividade'])
        else:
            print('%s: %s' % (dic[aux], dicUsuarios[usuario][aux]))

def consultarRecurso(dicRecursos):
    dic = {'responsavel': 'Responsável',
           'identificacao': 'Código do Recurso',
           'tipoRecurso': 'Recurso',
           'dataInicio': 'Data e Hora de Inicio',
           'dataFim': 'Data e Hora de Fim',
           'status': 'Status',
           'atividade': 'Atividade'}
    recurso = verificaRecurso(dicRecursos)
    print('==========%s(%s)==========' % recurso)
    for aux in dicRecursos[recurso]:
        if aux == 'atividade':
            ativ = dicRecursos[recurso][aux]
            if ativ == 'Sem':
                print('%s: %s' % (dic[aux], ativ))
            else:
                print('%s: %s' % (dic[aux], ativ['tipoAtividade']))
        else:
            print('%s: %s' % (dic[aux], dicRecursos[recurso][aux]))
    print("==========================")

def exibirUsuarios(dicUsuarios):
    print('==========Usuários==========')
    dic = {'email': 'E-mail',
           'nome': 'Nome',
           'usuario': 'Usuário',
           'funcao': 'Função',
           'recurso': 'Recurso Alocados:'}
    for usuario in dicUsuarios:
        print('==========%s==========' % usuario)
        for aux in dicUsuarios[usuario]:
            print('%s: %s' % (dic[aux], dicUsuarios[usuario][aux]))
        print("======================")


def exibirRecursos(dicRecursos):
    print('==========Recursos==========')
    dic = {'responsavel': 'Responsável',
           'identificacao': 'Código do Recurso',
           'tipoRecurso': 'Recurso',
           'dataInicio': 'Data e Hora de Inicio',
           'dataFim': 'Data e Hora de Fim',
           'status': 'Status',
           'atividade': 'Atividade'}
    for recurso in dicRecursos:
        print('==========%s(%s)==========' % recurso)
        for aux in dicRecursos[recurso]:
            print('%s: %s' % (dic[aux], dicRecursos[recurso][aux]))
        print("==========================")


def printMenu(dicFuncoes, tipo=''):
    print('%s: ' % tipo)
    for i in dicFuncoes:
        print('%s - %s' % (i, dicFuncoes[i]))
    opcao = input('Digite a opção: ')
    while opcao == '':
        print('Opção Invalida!')
        opcao = input('Digite a opção: ')
    return int(opcao)


def entradaDadosUsuario(dicUsuarios):
    print('==========Cadastro de Usuário==========')
    usuario = input("Usuário: ")
    while (usuario in dicUsuarios or usuario == ""):
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

    dicTipoUsuario = {1: 'Aluno',
                      2: 'Professor',
                      3: 'Administrador',
                      4: 'Pesquisador'}
    tipoUsuarioId = printMenu(dicFuncoes=dicTipoUsuario, tipo='Tipo de Usuário')
    if dicTipoUsuario[tipoUsuarioId] == 'Aluno':
        dicAluno = {1: 'Graduação',
                    2: 'Mestrado',
                    3: 'Doutorado'}
        tipoAluno = printMenu(dicFuncoes=dicAluno, tipo='Tipo de Aluno')
        tipoUsuario = 'Aluno de ' + dicAluno[tipoAluno]
    else:
        tipoUsuario = dicTipoUsuario[tipoUsuarioId]
    dadosUsuario = (usuario, email, nome, tipoUsuario)
    dicUsuarios[usuario] = cadastro(dadosUsuario=dadosUsuario)
    print('==========Usuário Cadastrado==========')
    return dicUsuarios


def alocacaoRecurso(dicRecursos, dicUsuarios, usuario):
    tipoDeRecursos = {1: 'Sala de Aula',
                      2: 'Laboratórios',
                      3: 'Auditório',
                      4: 'Projetores'}

    while dicUsuarios[usuario]['funcao'].split(" ")[0] == 'Aluno':
        print('Usuário não pode alocar recursos!')
        return dicRecursos

    chaveRecurso = verificaRecurso(dicRecursos)
    data = data_hora()
    if dicUsuarios[usuario]['funcao'] == 'Administrador':
        usuarioResponsavel = verificaUsuario(dicUsuarios)
    else:
        usuarioResponsavel = usuario

    dadosRecurso = (usuarioResponsavel, chaveRecurso[1], chaveRecurso[0], data[0], data[1], 'Em processo de alocação')
    dicRecursos[chaveRecurso] = cadastroRecurso(dadosRecurso)
    dicUsuarios[usuarioResponsavel]['recurso'].append(chaveRecurso)
    print('Processo de alocação realizado com sucesso!')
    return dicRecursos

def atividade(dicUsuarios, recurso):
    dicAtividades = {1: 'Aula Tradicional',
                     2: 'Apresentações',
                     3: 'Laboratório'}

    usuario = recurso['responsavel']
    tipoAtividade = printMenu(dicAtividades, tipo='Tipo de Atividade')
    if (tipoAtividade == 1 or tipoAtividade == 3) and dicUsuarios[usuario]['funcao'] == 'Professor':
        titulo = input('Título: ')
        descricao = input('Descrição: ')
        participantes = input('Participantes: ')
        materialApoio = input('Material de Apoio: ')
        dadosAtividade = (dicAtividades[tipoAtividade], titulo, descricao, participantes, materialApoio)
        return cadastroAtividade(dadosAtividade)

    elif tipoAtividade == 2:
        titulo = input('Título: ')
        descricao = input('Descrição: ')
        participantes = input('Participantes: ')
        materialApoio = input('Material de Apoio: ')
        dadosAtividade = (dicAtividades[tipoAtividade], titulo, descricao, participantes, materialApoio)
        return cadastroAtividade(dadosAtividade)

    else:
        print('Atividade restrita a professores!')
        atividade(dicUsuarios, recurso)


def somaParaRelatorio(dicRecursos):
    epal = 0
    alocado = 0
    emAndamento = 0
    concluido = 0
    aulaTradicional = 0
    laboratorio = 0
    apresentacoes = 0
    for rec in dicRecursos:
        print(dicRecursos[rec]['atividade']['tipoAtividade'] == 'Aula Tradicional')
        if dicRecursos[rec]['status'] == 'Em processo de alocação':
            epal += 1
        elif dicRecursos[rec]['status'] == 'Alocado':
            alocado += 1
        elif dicRecursos[rec]['status'] == 'Em Andamento':
            emAndamento += 1
        elif dicRecursos[rec]['status'] == 'Concluído':
            concluido += 1

        if dicRecursos[rec]['atividade']['tipoAtividade'] == 'Aula Tradicional':
            aulaTradicional += 1
        elif dicRecursos[rec]['atividade']['tipoAtividade'] == 'Apresentações':
            apresentacoes += 1
        elif dicRecursos[rec]['atividade']['tipoAtividade'] == 'Laboratório':
            laboratorio += 1

    return epal, alocado, emAndamento, concluido, aulaTradicional, apresentacoes, laboratorio

def relatorio(dicRecursos, dicUsuarios):
    print('==========Relatório===========')
    print('Número de Usuários: %s' % len(dicUsuarios))
    print('Número Total de Alocações: %s' % len(dicRecursos))
    alocacoes = somaParaRelatorio(dicRecursos)
    print('Em Processos de Alocações: %s\n'
          'Alocado: %s\n'
          'Em Andamento: %s\n'
          'Concluído: %s\n'
          'Aulas Tradicionais: %s\n'
          'Apresentações: %s\n'
          'Laboratórios: %s' % alocacoes)
    print('===============================')

def menu():
    opcoes = {0: 'Cadastro de Usuário',
              1: 'Alocação de Recursos',
              2: 'Consulta Usuários',
              3: 'Consulta Recursos',
              4: 'Alteração de Status',
              5: 'Relatório',
              6: 'Alteração de Usuário',
              9: 'Sair'}
    opcao = printMenu(opcoes, tipo='Deseja realizar')
    return opcao

def main(dicRecursos, dicUsuarios, usuario):
    opcao = menu()
    while (opcao != 9):
        if opcao == 0:
            dicUsuarios = entradaDadosUsuario(dicUsuarios)
        elif opcao == 1:
            recursos = alocacaoRecurso(dicRecursos, dicUsuarios, usuario)
        elif opcao == 2:
            consultarUsuario(dicUsuarios, dicRecursos)
            #exibirUsuarios(dicUsuarios)
        elif opcao == 3:
            consultarRecurso(dicRecursos)
            #exibirRecursos(dicRecursos)
        elif opcao == 4:
            recursos = alterarStatusRecurso(dicRecursos, dicUsuarios, usuario)
        elif opcao == 5:
            relatorio(dicRecursos, dicUsuarios)
        elif opcao == 6:
            usuario = verificaUsuario(dicUsuarios)
        opcao = menu()

if __name__ == '__main__':
    dicUsuarios = {'baldoino': {'usuario': 'baldoino',
                                'email': 'baldoino@algo.com',
                                'nome': 'Baldoino Fonseca',
                                'funcao': 'Professor',
                                'recurso': []},

                'clebsonpy': {'usuario': 'clebsonpy',
                              'email': 'clebson2007.farias@gmail.com',
                              'nome': 'Clebson Carvalho',
                              'funcao': 'Administrador',
                              'recurso': []},

                'clara': {'usuario': 'clarinha',
                          'email': 'clara@algo.com',
                          'nome': 'Maria Clara Carvalho',
                          'funcao': 'Aluno de Graduação',
                          'recurso': []}}
    dicRecursos = {}
    usuario = verificaUsuario(dicUsuarios)
    main(dicRecursos, dicUsuarios, usuario)