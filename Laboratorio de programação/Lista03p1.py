disciplinalista = []
#lista de disciplinas

import os.path

#arquivos
def lista_para_strings(disciplinas):
    file = open('lista_disciplinas.csv', 'w', newline='', encoding='utf-8')
    for disc in disciplinas:
        # disciplina = ((codigo, Nome, periodo, professor, alunos, carga_disc), (dias_disc, horarios_disc))
        codigo = disc[0][0]
        Nome = disc[0][1]
        periodo = disc[0][2]
        professor = ""
        if len(disc[0][3]) > 0:
            for professor in disc[0][3]:
                cod = professor[0]
                nome = professor[1]
                professor += str(cod)+"#"+nome+";"
            professor = professor[0:-1]
        else:
            professor = " "
        alunos = ""
        if len(disc[0][4]) > 0:
            for aluno in disc[0][4]:
                matrc = aluno[0]
                nome = aluno[1]
                curso = aluno[2]
                notas = ""
                if len(aluno[3]) > 0:
                    list_notas = aluno[3]
                    n1 = list_notas[0]
                    n2 = list_notas[1]
                    n3 = list_notas[2]
                    notas = str(n1)+"-"+str(n2)+"-"+str(n3)
                else:
                    notas = " "
                alunos += str(matrc)+"#"+nome+"#"+curso+"#"+notas+";"
            alunos = alunos[0:-1]
        else:
            alunos = " "
        carga_disc = disc[0][5]
        if len(disc[1][0]) == 2:
            dias_disc = str((disc[1][0])[0])+";"+str((disc[1][0])[1])
        else:
            dias_disc = str((disc[1][0])[0])+";"+str((disc[1][0])[1])+";"+str((disc[1][0])[2])
        horarios_disc = disc[1][1]
        nova_disc = str(codigo)+","+str(Nome)+","+str(periodo)+","+professor+","+alunos+","+str(carga_disc)+","+dias_disc+","+str(horarios_disc)
        file.write(nova_disc+"\n")
    file.close()

def strings_para_lista(disciplinas):
    if os.path.isfile('lista_disciplinas.csv'):
        file = open('lista_disciplinas.csv', 'r', newline='', encoding='utf-8')
    else:
        file = open('lista_disciplinas.csv', 'w', newline='', encoding='utf-8')
        return
    discs = file.readlines()
    for disc in discs:
        each = disc.split(",")
        cod_disc = each[0]
        nome_disc = each[1]
        semestre_disc = each[2]
        professores = []
        if each[3] != " ":
            list_profs = each[3].split(";")
            for prof in list_profs:
                list_infos = prof.split("#")
                professor = (int(list_infos[0]), list_infos[1])
                professores.append(professor)
        alunos = []
        if each[4] != " ":
            list_alunos = each[4].split(";")
            for aluno in list_alunos:
                list_infos = aluno.split("#")
                notas = list_infos[3]
                notas_aluno = []
                if notas != " ":
                    list_notas = notas.split("-")
                    for nota in list_notas:
                        notas_aluno.append(float(nota))
                aluno = (list_infos[0], list_infos[1], list_infos[2], notas_aluno)
                alunos.append(aluno)
        carga_disc = each[5]
        dias_disc = []
        list_dias = each[6].split(";")
        for dia in list_dias:
            dias_disc.append(int(dia))
        horarios_disc = (each[7])[:1]
        disciplina = ((int(cod_disc), nome_disc, semestre_disc, professores, alunos, int(carga_disc)), (dias_disc, int(horarios_disc)))
        disciplinas.append(disciplina)
    file.close()

def cadastreDisciplina():
  listadedias = []
  listaalunos = []
  listaprofessores = []
  disciplina = ()
  print("Digite o codigo da disciplina:")
  codigo = int(input())
  for i in range(len(disciplinalista)):
    while (codigo == disciplinalista[i][0]):
      print("Não é permitido cadastrar disciplinas com o mesmo código.")
      print("Digite novamente: ")
      codigo = int(input())
  print("Digite o nome da disciplina:")
  nome = input()
  print("Digite o ano do período que está cursando: ")
  anoPeriodo = input()
  print(
    "Digite qual periodo do ano que está cursando (1 - Primeiro periodo; 2 - Segundo periodo): "
  )
  periodo = input()
  periodo = anoPeriodo + "." + periodo
  print("Professores: ")
  print(listaprofessores)
  print("Digite a carga horária total(em horas): ")
  cargah = int(input())
  print("Quantos dias semanais serão neccessarios para a disciplina:")
  print(
    "Digite '1' para um dia de disponibilidade; '2' para três dias de disponibilidade:"
  )
  dias = int(input())
  while dias != 1 and dias != 2:
    print("Número incompatível. Tente novamente.")
    dias = int(input())
  if dias == 1:
    print("Escolha 2 (dois) dias da semana:")
    print('''Qual o dia da disciplina? 
     1 - Segunda
     2 - Terça
     3 - Quarta
     4 - Quinta
     5 - Sexta
     6 - Sabado ''')
    dia1 = int(input())
    listadedias.append(dia1)
  elif dias == 2:
    print("Escolha 3 (três) dias da semana:")
    print(
      "1 - segunda, 2 - terça, 3 - quarta, 4 - quinta, 5 - sexta e 6 - sábado."
    )
    dia1 = int(input())
    dia2 = int(input())
    listadedias.append(dia1)
    listadedias.append(dia2)
  print("Escolha em qual horário (apenas um) possui disponibilidade: ")
  print('''Qual o horario da disciplina? 
     1 - 8 as 10
     2 - 10 as 12
     3 - 12 as 14
     4 - 14 as 16
     5 - 16 as 18
     6 - 18 as 20
     7 - 20 as 22 ''')
  horario = int(input())
  diasHorario = (listadedias, horario)
  disciplina = (codigo, nome, periodo, listaprofessores, listaalunos, cargah,
                diasHorario)
  disciplinalista.append(disciplina)
  print("Disciplina cadastrada com sucesso!")
f = open('lista_disciplinas.csv', 'a', newline='', encoding='utf-8')
f.write(disciplinalista+"\n")
f.close()


def pesquisarDisciplina():
  print("Digite o codigo da disciplina que deseja pesquisar: ")
  codDis = int(input())
  for i in range(len(disciplinalista)):
    if disciplinalista[i][0] == codDis:
      print(f"Código: {disciplinalista[i][0]}")
      print(f"Nome: {disciplinalista[i][1]}")
      print(f"periodo: {disciplinalista[i][2]}")
      print(f"Professores:")
      for j in range(len(disciplinalista[i][3])):
        print(disciplinalista[i][3][j][1])
      print(f"Carga horaria: {disciplinalista[i][5]} horas")
      print("Dias: ")
      print("Dias: ")
      for j in range(len(disciplinalista[i][-1][0])):
        if disciplinalista[i][-1][0][j] == 1:
          print("Segunda ")
        if disciplinalista[i][-1][0][j] == 2:
          print("Terça ")
        if disciplinalista[i][-1][0][j] == 3:
          print("Quarta ")
        if disciplinalista[i][-1][0][j] == 4:
          print("Quinta ")
        if disciplinalista[i][-1][0][j] == 5:
          print("Sexta ")
        if disciplinalista[i][-1][0][j] == 6:
          print("Sábado ")
      print("Horários:")
      if disciplinalista[i][-1][-1] == 1:
        print("8 às 10h")
      if disciplinalista[i][-1][-1] == 2:
        print("10 às 12h")
      if disciplinalista[i][-1][-1] == 3:
        print("12 às 14h")
      if disciplinalista[i][-1][-1] == 4:
        print("14 às 16h")
      if disciplinalista[i][-1][-1] == 5:
        print("16 às 18h")
      if disciplinalista[i][-1][-1] == 6:
        print("18 às 20h")
      if disciplinalista[i][-1][-1] == 7:
        print("20 às 22h")

def cadastraProfessor():
  professor = ()
  print("Digite o codigo da disciplina em que deseja acessar:")
  codDis = int(input())
  for i in range(len(disciplinalista)):
    if disciplinalista[i][0] == codDis:
      print("Digite o codigo do(a) professor(a) que deseja cadastrar:")
      codigop = int(input())
      for x in range(len(disciplinalista)):
        for j in range(len(disciplinalista[x][3])):
          while (codigop == disciplinalista[x][3][j][0]):
            print("Não é permitido cadastrar professor com o mesmo código.")
            print("Digite novamente:")
            codigop = int(input())
      print("Digite o nome do(a) professor(a):")
      nomep = input()
      professor = (codigop, nomep)
      disciplinalista[i][3].append(professor)


def listarProfessores():
  print("Digite o código da disciplina que deseja acessar: ")
  codDis = int(input())
  print("Lista de professor da disciplina: ")
  for i in range(len(disciplinalista)):
    if disciplinalista[i][0] == codDis:
      for j in range(len(disciplinalista[i][3])):
        print(f"Professor: {disciplinalista[i][3][j][1]}")
        print(f"Código: {disciplinalista[i][3][j][0]}")
      print(disciplinalista[i][3])


def cadastraAluno():
  listaNotas = []
  aluno = ()
  print("Digite o codigo da disciplina em que deseja cadastrar:")
  codDis = int(input())
  for i in range(len(disciplinalista)):
    if disciplinalista[i][0] == codDis:
      print("Digite a matrícula do aluno:")
      matriculaAluno = int(input())
      for x in range(len(disciplinalista)):
        for j in range(len(disciplinalista[x][4])):
          while (matriculaAluno == disciplinalista[x][4][j][0]):
            print("Não é permitido cadastrar alunos com a mesma martrícula.")
            print("Digite novamente:")
            matriculaAluno = int(input())
      print("Digite o nome do aluno:")
      nomeAluno = input()
      print("Digite o curso do aluno:")
      cursoAluno = input()
      aluno = (matriculaAluno, nomeAluno, cursoAluno, listaNotas)
      disciplinalista[i][4].append(aluno)

def listarAlunos():
  print("Digite o código da disciplina que deseja acessar: ")
  codDis = int(input())
  print("Lista de alunos da disciplina: ")
  for i in range(len(disciplinalista)):
    if disciplinalista[i][0] == codDis:
      for j in range(len(disciplinalista[i][4])):
        print(f"Aluno: {disciplinalista[i][4][j][1]}")
        print(f"Matricula: {disciplinalista[i][4][j][0]}")
        print(f"Curso: {disciplinalista[i][4][j][2]}")

def lancarNotas():
  print("Digite o codigo da disciplina que deseja acessar:")
  codDis = int(input())
  print("Digite a matricula do aluno que deseja acessar")
  matriculaAluno = int(input())
  for i in range(len(disciplinalista)):
    for j in range(len(disciplinalista[i][4])):
      if disciplinalista[i][0] == codDis and disciplinalista[i][4][j][
          0] == matriculaAluno:
        print("Digite as tres notas do aluno:")
        nota1 = float(input())
        nota2 = float(input())
        nota3 = float(input())
        disciplinalista[i][4][j][3].append(nota1)
        disciplinalista[i][4][j][3].append(nota2)
        disciplinalista[i][4][j][3].append(nota3)


def listarNota():
  print("Digite o codigo da disciplina que deseja acessar:")
  codDis = int(input())
  for i in range(len(disciplinalista)):
    if disciplinalista[i][0] == codDis:
      for j in range(len(disciplinalista[i][4])):
        media = 0.0
        soma = 0.0
        print(f"O aluno {disciplinalista[i][4][j][1]} possui:")
        print(f"Notas: {disciplinalista[i][4][j][3]}")
        for x in range(len(disciplinalista[i][4][j][3])):
          soma += disciplinalista[i][4][j][3][x]
        media = soma / 3
        print(f"Media: {media}")
opcao = int(input(''' 
1 - Cadastrar disciplina
2 - Pesquisar disciplina
3 - Listar disciplinas cadastradas
4 - Cadasttrar professor em disciplina
5 - Matricular aluno em disciplina
6 - Lançar notas do aluno em uma disciplina
7 - Listar alunos de uma disciplina
8 - Listar notas dos alunos de uma disciplina
9 - sair '''))
escolha = int(opcao)
while escolha != 9 :
 if(escolha == 1):
    cadastreDisciplina()
 if(escolha == 2):
     pesquisarDisciplina()
 if(escolha == 3):
    for i in range(len(disciplinalista)):
      if len(disciplinalista) > 0:
        print(f"Disciplina: {disciplinalista[i][1]}")
        print(f"Codigo: {disciplinalista[i][0]}")
      else:
        print("Não há disciplinas cadastradas!")
 if(escolha == 4):
    cadastraProfessor()
 if(escolha == 5):
    cadastraAluno()
 if(escolha == 6):
     lancarNotas()
 if(escolha == 7):
    listarAlunos()
 if(escolha == 8):
    listarNota()
print("programa encerrado, obrigado!")