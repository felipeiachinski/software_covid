from time import sleep


class User:
    def init(self):
        self.nome = input('Nome: ')
        self.idade = int(input('Idade: '))

print('\nOlá! Este aplicativo te ajudará a informar-se melhor sobre a'
      '\nCOVID-19. Para começar, por favor, digite seu nome e idade.\n')
nome = input('Nome: ')
idade = int(input('Idade: '))


def menu():
    while True:
        print(100*'\n')
        print('\n************************************************************'
              '***********\n'
              'COVID-19\n'
              f'\nBoas vindas, {nome} ({idade} anos)! Selecione o que deseja,'
              ' sendo:\n'
              '(1) Quiz.\n'
              '(2) Teste de sintomas.\n'
              '(3) Orientações para o tratamento.\n'
              '(4) Sair.\n'
              '**************************************************************'
              '*********')
        option = int(input('\nDigite a opção: '))
        if option == 1:
            quiz()
        elif option == 2:
            teste()
        elif option == 3:
            orientacoes()
        elif option == 4:
            print(f'\nAté mais, {nome} ({idade} anos)!'
                  '\nEsperamos ter ajudado.')
            break
        else:
            print('\nOpção inválida. Digite novamente.')
            sleep(2)


def quiz():
    points = 0
    print(f'\nOk, {nome} ({idade} anos), quiz selecionado.'
          '\nCarregando...')
    sleep(2)
    while True:
        print(100*'\n')

        print('\n1) Não preciso me preocupar em higienizar as compras'
              '\ndo mercado, afinal, eu mesmo peguei da prateleira com\n'
              'as mãos limpas.')
        resposta = input('\nDigite, sendo as opções V (Verdadeiro) e F (Falso): ')
        if resposta in 'Ff':
            points += 1
            break
        elif resposta in 'Vv':
            break
        else:
            print('\nOpção inválida! Digite novamente.')
            sleep(2)
            continue
    while True:
        print('\n2) Os sintomas mais comuns da COVID-19 são: febre,'
              '\ntosse, cansaço, dor de cabeça e alteração do olfato.')
        resposta = input('\nDigite, sendo as opções V (Verdadeiro) e F (Falso): ')
        if resposta in 'Vv':
            points += 1
            break
        elif resposta in 'Ff':
            break
        else:
            print('\nOpção inválida! Digite novamente.')
            sleep(2)
            continue
    while True:
        print('\n3) Com mais de um ano de pandemia, já há medicamentos'
              '\nespecíficos e eficazes para o tratamento da COVID-19.')
        resposta = input('\nDigite, sendo as opções V (Verdadeiro) e F (Falso): ')
        if resposta in 'Ff':
            points += 1
            break
        elif resposta in 'Vv':
            break
        else:
            print('\nOpção inválida! Digite novamente.')
            sleep(2)
            continue
    while True:
        print('\n4) Mesmo uma pessoa sem sintomas da COVID-19 pode'
              '\ncontaminar outras.')
        resposta = input('\nDigite, sendo as opções V (Verdadeiro) e F (Falso): ')
        if resposta in 'Vv':
            points += 1
            break
        elif resposta in 'Ff':
            break
        else:
            print('\nOpção inválida! Digite novamente.')
            sleep(2)
            continue
    while True:
        print('\n5) A COVID-19 não deixa sequelas.')
        resposta = input('\nDigite, sendo as opções V (Verdadeiro) e F (Falso): ')
        if resposta in 'Ff':
            points += 1
            break
        elif resposta in 'Vv':
            break
        else:
            print('\nOpção inválida! Digite novamente.')
            sleep(2)
            continue
    if points == 5:
        print(100 * '\n')
        print('\nParabéns! Você acertou tudo, totalizando 5 pontos.'
              '\nVoltando ao menu principal...')
        sleep(3)
    else:
        print(100*'\n')
        print(f'Você conseguiu {points} pontos.'
              '\nPor favor, busque se esclarecer mais a respeito das'
              '\nmedidas preventivas e formas de tratamento.'
              '\nVoltando ao menu principal...')
        sleep(5)


def teste():
    print(f'\nOk, {nome} ({idade} anos), teste de sintomas selecionado.'
          '\nCarregando...')
    sleep(2)
    sintomas_covid = ['falta de paladar', 'perda de paladar', 'cansaço',
                      'tosse', 'dor no peito', 'pressão no peito',
                      'nariz entupido', 'perda de gosto', 'dor muscular',
                      'coriza', 'nariz trancado', 'tosse excessiva',
                      'tosse persistente', 'garganta inflamada', 'diarreia',
                      'congestão nasal', 'mal-estar', 'mal estar',
                      'dores no corpo', 'dor no corpo', 'perda de olfato',
                      'tosse seca', 'dor de garganta', 'febre', 'falta de ar',
                      'indisposição', 'dor de cabeça', 'olfato comprometido',
                      'paladar comprometido', 'dificuldade para respirar',
                      'tosse intensa', 'cansaço excessivo']
    sintomas_user = []
    while True:
        print(100 * '\n')
        print('\n************************************************************'
              '***********'
              '\nEscolha:\n'
              '\n(1) Inserir seus sintomas (um por vez).\n'
              '(2) Confirmar sintomas inseridos.\n'
              '(3) Voltar ao menu principal.')
        print('**************************************************************'
              '*********')
        option = int(input('\nDigite a opção: '))
        if option == 1:
            print(100*'\n')
            sintoma = input('Digite um dos sintomas te afetando: ')
            sintomas_user.append(sintoma.lower())
            print('Sintoma registrado.')
            sleep(1)
            print(100*'\n')
        elif option == 2:
            num = set(sintomas_covid) & set(sintomas_user)
            print(100*'\n')
            print(f'\nVocê possui {len(num)} sintoma(s) da COVID-19.')
            if len(num) == 0:
                print('Fique tranquilo! Tudo em ordem.'
                      '\nVoltando ao menu principal...')
                sleep(3)
                break
            elif len(num) == 1:
                print('Nada preocupante, mas cuide-se.'
                      '\nVoltando ao menu principal...')
                sleep(3)
                break
            elif len(num) == 2:
                print('Fique em casa e preste atenção à sua saúde.'
                      '\nVoltando ao menu principal...')
                sleep(3)
                break
            else:
                print('Preocupante. Por favor, encaminhe-se quando possível'
                      '\npara realizar o teste de detecção da COVID-19.'
                      '\nVoltando ao menu principal...')
                sleep(5)
                break
        elif option == 3:
            break
        else:
            print('\nOpção inválida. Digite novamente.')
            sleep(2)
            print(100*'\n')
            continue


def orientacoes():
    while True:
        print(f'\nOk, {nome} ({idade} anos), orientações para tratamento'
               ' selecionadas.'
               '\nCarregando...\n')
        sleep(2)
        print(100*'\n')
        arquivo = open('orientacoesCovid.txt', encoding='UTF-8')
        for linha in arquivo:
            print(linha)
        print(2*'\n')
        print('(Role para cima para ver o texto completo)')
        input('\nPressione qualquer tecla para voltar ao menu principal: ')
        break


menu()
