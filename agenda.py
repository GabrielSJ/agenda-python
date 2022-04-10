AGENDA = {}


def exibir_agenda():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print(">>> Não existe nenhum contato na sua agenda.")


def buscar_contato(nome):
    try:
        pessoa = AGENDA[nome]
        print("Name:", nome)
        print("Telephone:", AGENDA[nome]['tel'])
        print("Email:", pessoa['email'])
        print("Address:", pessoa['endereco'])
        print("Years:", pessoa['idade'])
        print("--------------------------------")
    except KeyError:
        print(">>> Nao foi localizado nenhum contato com o valor informado.")
    except:
        print(">>> Um erro ocorreu.")

def detalhes_contato():
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    endereco = input('Digite o endereço : ')
    idade = input('Digite a idade: ')

    return telefone, email, endereco, idade


def inserir_editar_contato(nome, telefone, email, endereco, idade):
    try:
        AGENDA[nome] = {
            'tel': telefone,
            'email': email,
            'endereco': endereco,
            'idade': idade
        }
        salvar()
        print(">>> Contato {} adicionado/editado com sucesso.".format(nome))
    except:
        print('>>> Ocorreu algum erro inesperado, tente novamente.')

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as contatos:
            for contato in AGENDA:
                telefone = AGENDA[contato]['tel']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                idade = AGENDA[contato]['idade']
                contatos.write('{},{},{},{},{}\n'.format(contato, telefone, email, endereco, idade))
        print('>>> Contatos exportados com sucesso.')
    except Exception as erro:
        print(">>> Arquivo não encontrado.")


def importar_contatos(arquivo):
    try:
        with open(arquivo, 'r') as agenda:
            linhas = agenda.readlines()
            for linha in linhas:
                detalhe = linha.strip().split(',')
                nome = detalhe[0]
                telefone = detalhe[1]
                email = detalhe[2]
                endereco = detalhe[3]
                idade = detalhe[4]
                inserir_editar_contato(nome, telefone, email, endereco, idade)
    except FileNotFoundError:
        print('>>> Arquivo não encontrado.')
    except:
        print('>>> Um erro inesperado ocorreu.')


def excluir_contato(nome):
    try:
        AGENDA.pop(nome)
        salvar()
    except KeyError:
        print(">>> Contato não encontrado.")
    except:
        print(">>> Um erro ocorreu.")


def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as agenda:
            linhas = agenda.readlines()
            for linha in linhas:
                detalhe = linha.strip().split(',')

                nome = detalhe[0]
                telefone = detalhe[1]
                email = detalhe[2]
                endereco = detalhe[3]
                idade = detalhe[4]

                AGENDA[nome] = {
                    'tel': telefone,
                    'email': email,
                    'endereco': endereco,
                    'idade': idade
                }
            print('>>> Database carregado com sucesso.')
    except FileNotFoundError:
        print('>>>Arquivo não encontrado')
    except:
        print('>>> Um erro inesperado ocorreu.')


def imprimir_menu():
    print("--------------------------------")
    print('1 - Adicionar um contato')
    print('2 - Excluir um contato')
    print('3 - Ver contatos')
    print('4 - Buscar um contato')
    print('5 - Editar um contato')
    print('6 - Exportar contatos')
    print('7 - Importar contatos')
    print('0 - Sair')
    print("--------------------------------")


carregar()
while True:
    imprimir_menu()
    opcao = input("Escolha uma opção: ")
    print()

    if opcao == '1':

        nome = input('Digite o nome do contato: ')
        try:
            AGENDA[nome]
            print("Contato já existe.")
        except KeyError:
            print("Criando o contato {}".format(nome))
            telefone, email, endereco, idade = detalhes_contato()
            inserir_editar_contato(nome, telefone, email, endereco, idade)

    elif opcao == '5':

        nome = input('Digite o nome do contato: ')
        try:
            AGENDA[nome]
            print("Editando o contao {}".format(nome))
            telefone, email, endereco, idade = detalhes_contato()
            inserir_editar_contato(nome, telefone, email, endereco, idade)
        except KeyError:
            print("Não encontrado")

    elif opcao == '2':
        nome = input('Digite o nome do contato que deseja excluir: ')
        excluir_contato(nome)
    elif opcao == '3':
        exibir_agenda()
    elif opcao == '4':
        nome = input('Digite o nome do contato que deseja encontrar: ')
        buscar_contato(nome)
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo para exportar os contatos: ')
        exportar_contatos(nome_do_arquivo)
    elif opcao == '7':
        arquivo = input('Digite o nome do arquivo para importar: ')
        importar_contatos(arquivo)
    elif opcao == '0':
        print('OBRIGADO, ATÉ LOGO!!')
        break;
    else:
        print('Voce não digitou uma opção valida.')



