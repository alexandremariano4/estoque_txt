from time import sleep
import cores

def linha():
    return '-' * 42

def cabeçalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())

def menuLogin():
    cabeçalho('Sistema de Estoque')
    arquivo = open('autenticador.txt','r')
    existeDados = arquivo.readlines()==[]
    try:
        resp = str(input('\033[34mTem cadastro: [S/N] \033[m')).strip().upper()[0]
        while resp not in 'SsNn':
            resp = str(input('\033[31mDigite uma opção válida! [S/N] \033[m')).strip().upper()[0]
        if resp == 'N' or existeDados == True:
            if resp == 'S' and existeDados == True:
                print('\033[31mNão foi encontrado dados na base, favor fazer um cadastro.\033[m')
            sleep(1)
            Cadastrar()
        if resp == 'S' and existeDados == False:
            Login()
    except (KeyboardInterrupt):
        print('\n\033[31mUsuário interrompeu o sistema... Finalizando!\033[m')
        sleep(1)
    except (FileNotFoundError):
        print('\033[33mNenhum usuário encontrado na base de dados, favor cadastrar.\033[m')
        sleep(1)
        menuLogin()
    except (TypeError) as error:
        print('ERRO!!! ',error.__class__)
    except (IndexError):
        print('\033[31mOpção inválida, favor digitar corretamente!\033[m')
        menuLogin()
         
def Login():
    valida = []
    conta = []
    posUsu = []

    cabeçalho('Tela de Login')
    arquivo = open('autenticador.txt','r',encoding="utf-8") 
    
    for linha in arquivo:
        if 'Usuario' or 'Senha' in linha:
            dado = linha.split(';')
            conta.append(dado[1].replace('\n','').strip())
  
    while True:
        try:
            if valida[0] == True:
                break
        except:
            pass

        #Validação se o usuário existe na base de dados 
        usuario = str(input('Usuario: ')).strip().lower().capitalize()
        for i,v in enumerate(conta):
            if v == usuario:
                posUsu.clear()
                posUsu.append(True)
                posUsu.append(i)
            else:
                posUsu.append(0)
        if posUsu[0] == True:
            break
        if posUsu[0] != True:
            print('\033[31mUsuário não encontrado, digite novamente\033[m')
            posUsu.clear()
            sair = str(input('Deseja fazer um novo cadastro: [S/N] ')).strip().upper()[0]
            while sair not in 'SsNn':
                sair = str(input('Digite uma opção válida! [S/N] ')).strip().upper()[0]
            if sair in 'Ss':
                Cadastrar()
                valida.insert(0,True)
                # Login()
                break
            elif sair in 'nN':
                valida.insert(0,True)
                Login()
    
    while True:    
        #Validação se a senha existe na base de dados 
        try:
            if valida[0] == True:
                break
        except:
            pass
        senha = str(input('Senha: ')).strip()
        if senha == conta[posUsu[1]+1]:
            print(f'\033[32mAutenticação feita com sucesso, Seja bem Vindo: {conta[posUsu[1]]}\033[m')
            break         
            
        else:
            print('\033[31mSenha incorreta, informe novamente sua senha.\033[m')
        
def Cadastrar():
    cabeçalho('Cadastro')
    existe = []

    arquivo = open('autenticador.txt','r')

    for linha in arquivo:
        dado = linha.replace('\n','').split(';')[1]
        existe.append(dado)
    
    
    usuario = str(input('Usuario: ')).strip().lower().capitalize()
    
    while usuario == '':
        usuario = str(input('Não é permitido usuário em branco: ')).strip().lower().capitalize()
    while usuario in existe:
        usuario = str(input('\033[31mUsuário existente: \033[m')).strip().lower().capitalize()
    
    senha = str(input('Senha: ')).strip()
    while senha == '':
        senha = str(input('Senha: ')).strip()
    enviarTXT(usuario,senha)

def enviarTXT(usuario,senha):
    try:
        arquivo = open('autenticador.txt','a',encoding="utf-8")
    except:
        print('Houve um erro para abrir o arquivo!')
    else:
        try:
            arquivo.write(f'{"Usuario"};{usuario}\n')
            arquivo.write(f'{"Senha"};{senha}\n')
            print('Usuário cadastrado!')
        except:
            print('Houve um erro para realizar o cadastro')
        else:
            print(f'\033[32mNovo registro de {usuario} feito com sucesso!\033[m')     
    finally:
        arquivo.close()
        menuLogin()   
