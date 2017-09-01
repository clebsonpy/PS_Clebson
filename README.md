# PS_Clebson
Nome:

Professor: Baldoino F. dos Santos Neto

Assunto do e-mail: [projeto] sistema de gestao

Atividade

A partir da visão geral do sistema apresentada abaixo, utilize a linguagem de
programação Python para implementar os requisitos funcionais.

Visão Geral do Sistema

O sistema de gestão de recursos objetiva o gerenciamento da alocação de laboratórios,
auditório, salas de aulas e projetores de uma unidade acadêmica, incluindo informações
sobre os usuários e as atividades realizadas.

Uma unidade acadêmica é formada pelos seguintes usuários: alunos de graduação,
mestrado e doutorado, professores, pesquisadores e o administrador do sistema,
o qual é responsável pela manutenção de todas as informações do sistema.

Os recursos de uma unidade acadêmica podem ser alocados a usuários. Recursos
possuem as seguintes informações básicas: identificação, data e hora de início,
data e hora de término e o responsável pelo recurso. O responsável pelo recurso
deve ser um professor, pesquisador ou administrador do sistema. O status inicial
da alocação de um recurso é “Em processo de alocação”. Após finalizado o processo
de alocação, ou seja, constarem todas as informações básicas a respeito da alocação,
o administrador pode iniciar a alocação, alterando seu status para “Alocado”.
Até o dia e hora de início da alocação do recurso o responsável deve confirmar
a alocação e o sistema deve alterar o status para “Em andamento”. A partir deste
momento, o status da alocação somente poderá ser alterado pelo administrador para
“Concluído”, e para que isto aconteça deve existir a descrição da atividade a ser
realizada utilizando o recurso em questão.

Os usuários podem alocar recursos para três tipos de atividades: aula tradicional,
apresentações e laboratório. Entretanto, somente os professores podem alocar
recursos para aulas tradicionais e laboratórios. Uma atividade deve ter título,
uma breve descrição, participantes e material de apoio ( por exemplo, arquivo
com apresentações ou código fonte).

Requisitos Funcionais

1. O sistema deve permitir a edição de uma alocação de recursos

  a. Associação de usuários. Deve existir pelo menus um professor, pesquisador
  ou administrador associado a um recurso. Um usuário não pode esta associado a
  mais de um recurso “em andamento”.

  b. Alteração do status

    i. “Em processo de alocação” para “Alocado”. O administrador deve poder
    iniciar uma alocação apenas se constarem todas as informações básicas.

    ii. “Alocado” para “Em andamento”. O responsável deve poder confirmar a
    alocação.

    iii. “Em andamento” para “Concluído”. O administrador deve poder alterar o
    status para “Concluído”, se existir a descrição da atividade realizada
    utilizando o recurso em questão

  c. O sistema deve permitir a inclusão de informações referentes às atividades.

  d. O sistema deve oferecer as seguintes consultas:

    i. Consulta por usuário: dado um usuário, o sistema deve apresentar suas
    informações: nome, e-mail, um histórico contendo a lista de recursos
    alocados e atividades realizadas.

    ii. Consulta por recurso: dado um recurso, o sistema deve apresentar todos
    os dados do associado ao recurso, incluindo os usuários e as atividades.

  e. O sistema deve fornecer um relatório de atividades da unidade acadêmica,
  contendo:

    i. Número de usuários

    ii. Número de recursos “Em processo de alocação”, “Alocado”, “Em andamento”
    ou “Concluído”.

    iii. Número de total de alocações.

    iv. Número de atividades de acordo com o seu tipo.