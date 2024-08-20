from datetime import datetime

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

    disciplinadados = dict()
    alunodados = dict()

    if(escolha == 1):
       print(f"Cadastrar disciplina")
       disciplinadados['Código'] = int(input('Codigo da disciplina: '))
       disciplinadados['nome'] = str(input('Nome: '))[255]
       disciplinadados['Semestre'] = datetime.now().year
       disciplinadados['Cargah'] = int(input('Carga horaria'))
       dia = input('''Qual o dia da disciplina? 
     1 - Segunda
     2 - Terça
     3 - Quarta
     4 - Quinta
     5 - Sexta
     6 - Sabado ''')
    dia_escolhido = int(dia)

    if(dia_escolhido == 1):
        disciplinadados['dia'] = str('segunda')
    if(dia_escolhido == 2):
        disciplinadados['dia'] = str('terça')
    if(dia_escolhido == 3):
        disciplinadados['dia'] = str('Quarta')
    if(dia_escolhido == 4):
        disciplinadados['dia'] = str('Quinta')
    if(dia_escolhido == 5):
        disciplinadados['dia'] = str('sexta')
    if(dia_escolhido == 6):
        disciplinadados['dia'] = str('sabado')
    horario = input('''Qual o horario da disciplina? 
     1 - 8 - 10
     2 - 10 - 12
     3 - 12 - 14
     4 - 14 - 16
     5 - 16 - 18
     6 - 18 - 20
     7 - 20 - 22 ''')
    horario_escolhido = int(horario)
    if(horario_escolhido == 1):
        disciplinadados['horas'] = str('1 horário')
    if(horario_escolhido == 2):
        disciplinadados['horas'] = str('2 horário')
    if(horario_escolhido == 3):
        disciplinadados['horas'] = str('3 horário')
    if(horario_escolhido == 4):
        disciplinadados['horas'] = str('4 horário')
    if(horario_escolhido == 5):
        disciplinadados['horas'] = str('5 horário')
    if(horario_escolhido == 6):
        disciplinadados['horas'] = str('6 horário')
    if(horario_escolhido == 7):
        disciplinadados['horas'] = str('7 horário')
    lista_disciplinas = []
    lista_disciplinas.append([(disciplinadados['codigo']),disciplinadados['semestre'],disciplinadados['cargah'],disciplinadados['dia'],disciplinadados['horas']])

    for k, v in disciplinadados.items():
        print(f' - {k} tem o valor {v}')
    if(escolha == 2):
        busca = input('código buscado: ')
        for i , lista_disciplinas.__sizeof__ in lista_disciplinas():
         if(busca == disciplinadados['codigo']):
            print(disciplinadados)
    if(escolha == 3):
        print(lista_disciplinas)
    if(escolha == 4):
       print(f"Cadastrar disciplina")
       disciplinadados['nome'] = str(input('Nome: '))
       disciplinadados['Código'] = int(input('Codigo da disciplina: '))
    if(escolha == 5):
        print(f"Cadastrar aluno na disciplina")
        alunodados = dict()
        alunodados['codidisciplina'] = int(input('Codigo da disciplina: '))
        alunodados['Matricula'] = str(input('Nome: '))[11]
        alunodados['Nome'] = str(input('Nome: '))[255]
        alunodados['Curso'] = str(input('Nome: '))[255]
        lista_alunos = []
        lista_alunos.append([(alunodados['codidisciplina']),alunodados['matricula'],alunodados['Nome'],alunodados['Curso']])

    if(escolha == 6):
        nota1 = input('qual a nota 1: ')
        nota2 = input('qual a nota 2: ')
        nota3 = input('qual a nota 3: ')
        aluno_notas = [nota1, nota2, nota3]
        lista_notas = []
        lista_notas.append = [aluno_notas]
    if(escolha == 7):
        busca = input('código buscado: ')
        lista_disciplinas.__sizeof__ = k
        for i, k in lista_disciplinas.items():
         if(busca == ['codigo']):
             print(lista_alunos)
    if(escolha == 8):
        busca = input('código buscado: ')
        lista_disciplinas.__sizeof__ = k
        for i, k in lista_disciplinas.items():
         if(busca == ['codigo']):
             print(lista_notas)
print("programa encerrado, obrigado!")