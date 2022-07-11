import login
import produtos
import cores


opcoesAdm = {1:produtos.Cadastrar,
          2:produtos.Alterar,
          3:produtos.Deletar,
          4:produtos.Visualizar,
          5:produtos.Sair}



# def menuCli(lista):
#     login.cabeçalho('Menu Cliente')
#     cont = 1
#     for item in lista:
#         print(f'{cont} - {item}')
#         cont += 1
#     print(login.linha())
#     opcao = int(input(f'{cores.color("azul")}Digite sua opção: {cores.color("limpa")}'))



def menuAdm(lista):
    opcoes = []
    login.cabeçalho('Menu Administrativo')
    for key, value in opcoesAdm.items():
        opcoes.append(key)
    cont = 1
    for item in lista:
        print(f'{cont} - {item}')
        cont += 1
    print(login.linha())
    opcao = str(input(f'{cores.color("amarelo")}Digite sua opção: {cores.color("limpa")}'))
    
    while opcao.isnumeric() != True:
        opcao = str(input(f'{cores.color("amarelo")}Digite uma opção válida: {cores.color("limpa")}'))
        
    while int(opcao) not in opcoes:
        opcao = str(input(f'{cores.color("amarelo")}Digite uma opção disponível do sistema: {cores.color("limpa")}'))
        
        while opcao.isnumeric() != True:
            opcao = str(input(f'{cores.color("amarelo")}Digite uma opção válida: {cores.color("limpa")}'))

    opcoesAdm[int(opcao)]()
    
  