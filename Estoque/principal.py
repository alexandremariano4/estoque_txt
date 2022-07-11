from logging import shutdown
from os import system
from time import sleep
import login
import estoque
import cores
import produtos



login.menuLogin()



try:
    opcao = str(input(f'{cores.color("azul")}Digite [2] para acessar a tela principal do sistema: {cores.color("limpa")}')).strip()
    # while True:  
    while opcao not in '2':
        opcao = str(input(f'{cores.color("amarelo")}Favor digitar uma opção válida [2]: {cores.color("limpa")}')).strip()
        
    while opcao == '':
        opcao = str(input(f'{cores.color("vermelho")}Favor digitar uma opção válida [2]: {cores.color("limpa")}')).strip()

    #     if opcao == '1':
    #         print(f'{cores.color("vermelho")}Menu de Cliente Ainda em construção, acesse o menu Administrador.{cores.color("limpa")}')
    #         sleep(1.5)
            
    #         # estoque.menuCli(['Ver Produtos','Comprar Produtos','Sair do Sistema'])    
    #         break

    if opcao == '2':
        print('Autenticador = "admin"')
        autenticador = str(input('Digite o autenticador para acessar o menu ADM: ')).strip()
        while autenticador != 'admin' and autenticador != '0':
            system('cls')
            print(f'{cores.color("verde")}Para fechar o sistema digite 0{cores.color("limpa")}')
            autenticador = str(input(f'{cores.color("vermelho")}Autenticador incorreto, digite o correto para acessar o menu ADM: {cores.color("limpa")}')).strip()
        if autenticador == '0':
            produtos.Sair()
        if autenticador == 'admin':
            estoque.menuAdm([f'{cores.color("roxo")}Cadastrar Produto{cores.color("limpa")}',f'{cores.color("amarelo")}Alterar Produto{cores.color("limpa")}', f'{cores.color("verde")}Deletar Produto{cores.color("limpa")}',f'{cores.color("azul")}Ver Produtos{cores.color("limpa")}',f'{cores.color("vermelho")}Sair do Sistema{cores.color("limpa")}'])    
            
        else:
            opcao = str(input('Favor digitar uma opção válida [1] Cliente [2] ADM: ')).strip()
except Exception as error:
    print(f'Tivemos um erro! {error.__class__}')
except KeyboardInterrupt:
    print(f'\n{cores.color("vermelho")}Usuário encerrou o sistema!{cores.color("limpa")}')
