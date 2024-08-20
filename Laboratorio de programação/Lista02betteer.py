import os.path

listaDisciplinas = [] 

my_file = open('memory.txt', mode='a')

def pesquisarDisciplina():
  print("Digite o codigo da disciplina que deseja pesquisar: ")
  codDis = int(input())
  for i in range(len(listaDisciplinas)):
    if listaDisciplinas[i][0] == codDis:
      print(f"Código: {listaDisciplinas[i][0]}")
      print(f"Nome: {listaDisciplinas[i][1]}")
      print(f"Semestre: {listaDisciplinas[i][2]}")
      print(f"Professores: ")
      for j in range(len(listaDisciplinas[i][3])):
        print(listaDisciplinas[i][3][j][1])
      print(f"Carga horaria: {listaDisciplinas[i][5]} horas")
      print("Dias: ")
      for j in range(len(listaDisciplinas[i][-1][0])):
        if listaDisciplinas[i][-1][0][j] == 1:
          print("Segunda ")
        if listaDisciplinas[i][-1][0][j] == 2:
          print("Terça ")
        if listaDisciplinas[i][-1][0][j] == 3:
          print("Quarta ")
        if listaDisciplinas[i][-1][0][j] == 4:
          print("Quinta ")
        if listaDisciplinas[i][-1][0][j] == 5:
          print("Sexta ")
        if listaDisciplinas[i][-1][0][j] == 6:
          print("Sábado ")
      print("Horários:")
      if listaDisciplinas[i][-1][-1] == 1:
        print("8 às 10h")
      if listaDisciplinas[i][-1][-1] == 2:
        print("10 às 12h")
      if listaDisciplinas[i][-1][-1] == 3:
        print("12 às 14h")
      if listaDisciplinas[i][-1][-1] == 4:
        print("14 às 16h")
      if listaDisciplinas[i][-1][-1] == 5:
        print("16 às 18h")
      if listaDisciplinas[i][-1][-1] == 6:
        print("18 às 20h")
      if listaDisciplinas[i][-1][-1] == 7:
        print("20 às 22h")
      break

def cadastreDisciplina():
  listaDias = []
  listaAlunos = []
  listaProfessores = []
  disciplina = ()
  print("Digite o codigo da disciplina:")
  codigo = int(input())
  for i in range(len(listaDisciplinas)):
    while (codigo == listaDisciplinas[i][0]):
      print("Não é permitido cadastrar disciplinas com o mesmo código.")
      print("Digite novamente: ")
      codigo = int(input())
  print("Digite o nome da disciplina:")
  nome = input()
  print("Digite o ano do período que está cursando: ")
  ano = input()
  print(
    "Digite qual semestre do ano que está cursando (1 - Primeiro semestre; 2 - Segundo Semestre): "
  )
  semestre = input()
  periodo = ano + "." + semestre
  print("Professores: ")
  print(listaProfessores)
  print("Digite a carga horária: ")
  cargah = int(input())
  print("Escolha quantos dias na semana possui disponibilidade:")
  print(
    "Digite '1' para a ocorrencia de um dia e '2' para de dois dias"
  )
  dias = int(input())
  while dias != 1 and dias != 2:
    print("Número incompatível. Tente novamente.")
    dias = int(input())
  if dias == 1:
    print("Escolha 1 dia da semana:")
    print(
      "1 - segunda, 2 - terça, 3 - quarta, 4 - quinta, 5 - sexta e 6 - sábado."
    )
    dia1 = int(input())
    listaDias.append(dia1)
  elif dias == 2:
    print("Escolha 2  dias da semana:")
    print(
      "1 - segunda, 2 - terça, 3 - quarta, 4 - quinta, 5 - sexta e 6 - sábado."
    )
    dia1 = int(input())
    dia2 = int(input())
    listaDias.append(dia1)
    listaDias.append(dia2)
  print('''Qual o horario da disciplina? 
     1 - 8 as 10
     2 - 10 as 12
     3 - 12 as 14
     4 - 14 as 16
     5 - 16 as 18
     6 - 18 as 20
     7 - 20 as 22 ''')
  horario = int(input())
  diasHorario = (listaDias, horario)
  disciplina = (codigo, nome, periodo, listaProfessores, listaAlunos, cargah, diasHorario)
  listaDisciplinas.append(disciplina)
  d = 'Codigo da disciplina: ' + str(codigo) + '; Nome: ' + str(nome) + '; Período: ' + str(periodo) + '; Professores (codigo e nome, respectivamente): ' + str(listaProfessores) + '; Alunos (matrícula, nome e curso, respectivamente): ' + str(listaAlunos) + '; Carga horária: ' + str(cargah) + '; Dias e horários: ' + str(diasHorario) + '\n'
  my_file = open('memory.txt', mode='a')
  my_file.write(d)
  my_file.close()

def cadastraProfessor():
  professor = ()
  print("Digite o codigo da disciplina em que deseja acessar:")
  codDis = int(input())
  for i in range(len(listaDisciplinas)):
    if listaDisciplinas[i][0] == codDis:
      print("Digite o codigo do(a) professor(a) que deseja cadastrar:")
      codigescolha = int(input())
      for x in range(len(listaDisciplinas)):
        for j in range(len(listaDisciplinas[x][3])):
          while (codigescolha == listaDisciplinas[x][3][j][0]):
            print("Não é permitido cadastrar professores com o mesmo código.")
            print("Digite novamente:")
            codigescolha = int(input())
      print("Digite o nome do(a) professor(a):")
      nomep = input()
      professor = (codigescolha, nomep)
      listaDisciplinas[i][3].append(professor)
      prof = "Codigo da disciplina em que o professor está inserido: " + str(codDis) + "; Codigo do professor: " + str(codigescolha) + "; Nome do Professor: " + str(nomep) + '\n'
      my_file = open('memory.txt', mode='a')
      my_file.write(prof)
      my_file.close()

def cadastraAluno():
  listaNotas = []
  aluno = ()
  print("Digite o codigo da disciplina em que deseja cadastrar:")
  codDis = int(input())
  for i in range(len(listaDisciplinas)):
    if listaDisciplinas[i][0] == codDis:
      print("Digite a matrícula do aluno:")
      matriculaAluno = int(input())
      for x in range(len(listaDisciplinas)):
        for j in range(len(listaDisciplinas[x][4])):
          while (matriculaAluno == listaDisciplinas[x][4][j][0]):
            print("Não é permitido cadastrar alunos com a mesma martrícula.")
            print("Digite novamente:")
            matriculaAluno = int(input())
      print("Digite o nome do aluno:")
      nomeAluno = input()
      print("Digite o curso do aluno:")
      cursoAluno = input()
      aluno = (matriculaAluno, nomeAluno, cursoAluno, listaNotas)
      listaDisciplinas[i][4].append(aluno)
      al = "Codigo da disciplina em que o aluno está inserido: " + str(codDis) + "; Matrícula: " + str(matriculaAluno) + "; Nome do aluno: " + str(nomeAluno) + "; Curso do aluno: " + str(cursoAluno) + "; Notas do aluno: " + str(listaNotas) + '\n'
      my_file = open('memory.txt', mode='a')
      my_file.write(al)
      my_file.close()

def listarProfessores():
  print("Digite o código da disciplina que deseja acessar: ")
  codDis = int(input())
  print("Lista de professores da disciplina: ")
  for i in range(len(listaDisciplinas)):
    if listaDisciplinas[i][0] == codDis:
      for j in range(len(listaDisciplinas[i][3])):
        print(f"Professor: {listaDisciplinas[i][3][j][1]}")
        print(f"Código: {listaDisciplinas[i][3][j][0]}")
      print(listaDisciplinas[i][3])

def listarAlunos():
  print("Digite o código da disciplina que deseja acessar: ")
  codDis = int(input())
  print("Lista de alunos da disciplina: ")
  for i in range(len(listaDisciplinas)):
    if listaDisciplinas[i][0] == codDis:
      for j in range(len(listaDisciplinas[i][4])):
        print(f"Aluno: {listaDisciplinas[i][4][j][1]}")
        print(f"Matricula: {listaDisciplinas[i][4][j][0]}")
        print(f"Curso: {listaDisciplinas[i][4][j][2]}")


def lancarNotas():
  print("Digite o codigo da disciplina que deseja acessar:")
  codDis = int(input())
  print("Digite a matricula do aluno que deseja acessar")
  matriculaAluno = int(input())
  for i in range(len(listaDisciplinas)):
    for j in range(len(listaDisciplinas[i][4])):
      if listaDisciplinas[i][0] == codDis and listaDisciplinas[i][4][j][
          0] == matriculaAluno:
        print("Digite as 3 (três) notas do aluno:")
        nota1 = float(input())
        nota2 = float(input())
        nota3 = float(input())
        listaDisciplinas[i][4][j][3].append(nota1)
        listaDisciplinas[i][4][j][3].append(nota2)
        listaDisciplinas[i][4][j][3].append(nota3)

def listarNota():
  print("Digite o codigo da disciplina que deseja acessar:")
  codDis = int(input())
  for i in range(len(listaDisciplinas)):
    if listaDisciplinas[i][0] == codDis:
      for j in range(len(listaDisciplinas[i][4])):
        print(f"O aluno {listaDisciplinas[i][4][j][1]} possui:")
        print(f"Notas: {listaDisciplinas[i][4][j][3]}")


escolha = 0 
while (escolha != 9):
  print('''
1 - Cadastrar disciplina
2 - Pesquisar disciplina
3 - Listar disciplinas cadastradas
4 - Cadasttrar professor em disciplina
5 - Matricular aluno em disciplina
6 - Lançar notas do aluno em uma disciplina
7 - Listar alunos de uma disciplina
8 - Listar notas dos alunos de uma disciplina
9 - sair ''')

  print("Digite sua escolhação:")
  escolha = int(input())

  if escolha == 1:
    cadastreDisciplina()
    print("Cadastro realizado com sucesso!")
  elif escolha == 2:
    pesquisarDisciplina()
  elif escolha == 3:
    for i in range(len(listaDisciplinas)):
      if len(listaDisciplinas) > 0:
        print(f"Disciplina: {listaDisciplinas[i][1]}")
        print(f"Codigo: {listaDisciplinas[i][0]}")
      else:
        print("Não há disciplinas cadastradas!")
  elif escolha == 4:
    cadastraProfessor()
  elif escolha == 5:
    cadastraAluno()
  elif escolha == 6:
    lancarNotas()
    print("Lançamento de notas realizado com sucesso!")
  elif escolha == 7:
    listarAlunos()
  elif escolha == 8:
    listarNota()
  elif escolha==9:
    my_file = open('memory.txt', mode='r')
    for linha in my_file:
      print(linha)
    print("Deseja apagar o arquivo salvo com a memoria que foi cadastrados? (1-Sim; 2-Não): ")
    resp2 = int(input())
    if(resp2 == 2):
      print('Sistema finalizado.')
      break
    else:
      if os.path.exists("memory.txt"):
        os.remove("memory.txt")
        print("Arquivo apagado!")
print('Programa encerrado, obrigado!!')