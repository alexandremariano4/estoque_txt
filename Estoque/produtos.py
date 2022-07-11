from logging import shutdown
from time import sleep
import cores
import loja

def Cadastrar():
    """
    Realiza o cadastro de um produto, recebe os valores do usuário, faz verificações
    e se todos dados estiverem de acordo, envia-os para o arquivo TXT.
    """
    existente = []
    with open('produtos.txt','r',encoding='utf-8') as arq:
        prod = arq.readlines()
    arquivo = open('produtos.txt','a',encoding="utf-8")
    
    produto = str(input('Produto: ')).strip().lower().capitalize()
    for p in prod:
        existente.append(p.replace('Produto;','').replace('\n',''))


    while len(produto) > 10 or produto.replace(' ','').isalnum() != True or produto in existente:
        if len(produto) > 10:
            produto = str(input(f'{cores.color("vermelho")}Digite um produto com no máx 10 caracteres: {cores.color("limpa")}')).strip().lower().capitalize()   
        elif produto.replace(' ','').isalnum() != True:
            produto = str(input(f'{cores.color("vermelho")}Digite um valor válido para produto: {cores.color("limpa")}')).strip().lower().capitalize() 
        elif produto in existente:
            produto = str(input(f'{cores.color("vermelho")}Produto existente na base, favor inserir um outro nome de produto: {cores.color("limpa")}')).strip().lower().capitalize()
    

    quantidade = str(input('Quantidade total: ')).strip()
    while quantidade.isnumeric() != True:
        quantidade = str(input(f'{cores.color("vermelho")}Digite um valor válido para quantidade: {cores.color("limpa")}')).strip()
        

    #não permite o usuário escrever um número com vírgula e sem números depois dela
    

    
    preco = str(input('Preço unitário: R$')).strip().replace('.',',')
    while preco.replace('.','').replace(',','').isnumeric() != True:
        preco = str(input(f'{cores.color("vermelho")}Digite um valor válido para o preço: {cores.color("limpa")}R$')).strip().replace('.',',')

    cont = ValidaPreco(preco)          
    while cont > 1 and preco.isnumeric() != True:
        preco = str(input(f'{cores.color("vermelho")}Número inválido, digite novamente: {cores.color("limpa")}R$')).strip().replace('.',',')
        cont = ValidaPreco(preco)
    
    verifica = VerificaDecimal(preco)
    while verifica != True and preco.isnumeric() != True:
        preco = str(input(f'{cores.color("vermelho")}Número inválido, digite novamente: {cores.color("limpa")}R$')).strip().replace('.',',')
        verifica = VerificaDecimal(preco)
     
     
        
    arquivo.write(f'{"Produto"};{produto}\n')
    arquivo.write(f'{"Quantidade"};{quantidade}\n')
    arquivo.write(f'{"Preço"};{preco}\n')
    arquivo.close()
    loja.menuAdm([f'{cores.color("roxo")}Cadastrar Produto{cores.color("limpa")}',f'{cores.color("amarelo")}Alterar Produto{cores.color("limpa")}', f'{cores.color("verde")}Deletar Produto{cores.color("limpa")}',f'{cores.color("azul")}Ver Produtos{cores.color("limpa")}',f'{cores.color("vermelho")}Sair do Sistema{cores.color("limpa")}'])

def VerificaDecimal(preco):
    if ValidaPreco(preco) > 1:
        return False   
    cont = 0
    pare = 0
    for qtd,digito in enumerate(preco):
        cont += 1
        if digito == ',':
            pare = cont
        if qtd == 0:
            cont = 0 
    if cont == pare+2:
        return True
    else:
        return False

def ValidaPreco(preco):
    cont = 0
    for i,digito in enumerate(preco):
        if digito == ',':
            cont += 1
        if i == 0 and digito == ',':
            return cont + 2
    return cont

def Visualizar(sair=0):
    try:
        arquivo = open('produtos.txt','r',encoding='utf-8')
        if ArquivoVazio() == True:
            print(f'{cores.color("amarelo")}Sem produtos cadastrado na base de dados, cadastre novos produtos.{cores.color("limpa")}')
            loja.menuAdm([f'{cores.color("roxo")}Cadastrar Produto{cores.color("limpa")}',f'{cores.color("amarelo")}Alterar Produto{cores.color("limpa")}', f'{cores.color("verde")}Deletar Produto{cores.color("limpa")}',f'{cores.color("azul")}Ver Produtos{cores.color("limpa")}',f'{cores.color("vermelho")}Sair do Sistema{cores.color("limpa")}'])

        
        print('--'*43)
        print(f'{"ID":<5}{"Produto":<5}',f'{"Quantidade":>33}',f'{"Preço":>31}')
        print('--'*43)
        arq = open('produtos.txt','r',encoding='utf-8')
        identificar = {}
        for i,nome in enumerate(arq):        
            if 'Produto' in nome:
                identificar[i] = nome.replace('Produto;','').replace('\n','')

        pos = 0
        lista = []

        for key, value in identificar.items():
            lista.append(key)

        for itens in arquivo:
            item = itens.split(';')
            item[1] = item[1].replace('\n','')
            if item[0] == 'Produto':
                print(lista[pos],end=' - ')
                pos+=1
            print(f'{item[1]}',end='\t\t\t\t')
            if item[0] == 'Preço':
                print('')
        print('--'*43)
    except Exception as error:
        Visualizar(f'Erro no processo {error.__class__} ')
    if sair == 0:
        voltar = 'Texto aleatório'
        arq.close()
        arquivo.close()
        try:
            voltar = str(input(f'{cores.color("azul")}Deseja voltar para o menu principal? [N] irá encerrar o programa: [S/N] {cores.color("limpa")}')).upper().strip()[0]
            while voltar not in 'NnSs':
                voltar = str(input(f'{cores.color("vermelho")}Opção inválida, deseja voltar ao menu principal? [N] irá encerrar o programa [S/N] {cores.color("limpa")}')).upper().strip()[0]     
            if voltar.isnumeric() == True:
                voltar = str(input(f'{cores.color("vermelho")}Digite um valor válido para voltar ao menu ou encerrar o programa: [S/N] {cores.color("limpa")}')).upper().strip()[0]
            if 'N' == voltar:
                sleep(2)
                Sair()
            if 'S' == voltar:
                sleep(2)
                loja.menuAdm([f'{cores.color("roxo")}Cadastrar Produto{cores.color("limpa")}',f'{cores.color("amarelo")}Alterar Produto{cores.color("limpa")}', f'{cores.color("verde")}Deletar Produto{cores.color("limpa")}',f'{cores.color("azul")}Ver Produtos{cores.color("limpa")}',f'{cores.color("vermelho")}Sair do Sistema{cores.color("limpa")}'])
        except Exception as error:
            print(f'Erro no processo de saída da visualização de produtos{error.__class__}')  
    
def ArquivoVazio(): 
    resultado = False
    try:
        arquivo = open('produtos.txt','r',encoding='utf-8')
    except:
        arquivo = open('produtos.txt','w',encoding='utf-8')
    if arquivo.read().strip()=='':
        resultado = True
    return resultado

def Alterar():
    identificadores = []
    novaLista = []
    Visualizar(1)
    with open('produtos.txt','r',encoding='utf-8') as arquivo:
        itens = arquivo.readlines()
        for i,identificador in enumerate(itens):
            novaLista.append(identificador)   
            if 'Produto' in identificador:
                identificadores.append(i)
        
        
    opcao = str(input(f'{cores.color("azul")}Qual opção deseja alterar: {cores.color("limpa")}')).strip()
    while opcao.isnumeric() != True or int(opcao) not in identificadores:
        opcao = str(input(f'{cores.color("vermelho")}Opção inválida, digite um valor válido: {cores.color("limpa")}')).strip()
    
    with open('produtos.txt','r',encoding='utf-8') as arquivo:
        nomesProd = arquivo.readlines()
        for i,nomeProd in enumerate(nomesProd):
            if i == int(opcao):
                nome = nomeProd.replace('Produto;','').replace('\n','')
    
#Após selecionar a linha que o usuário deseja alterar, nessa seção o usuário deverá informar o nome, quantidade e preço do produto a alterar
    existente = []
    with open('produtos.txt','r',encoding='utf-8') as arq:
        prod = arq.readlines()
    arquivo = open('produtos.txt','a',encoding="utf-8")
    
    produto = str(input(f'{cores.color("verde")}Novo nome de Produto: {cores.color("limpa")}')).strip().lower().capitalize()
    for p in prod:
        existente.append(p.replace('Produto;','').replace('\n',''))

    while len(produto) > 10 or produto.replace(' ','').isalnum() != True or produto in existente:
        if len(produto) > 10:
            produto = str(input(f'{cores.color("vermelho")}Digite um produto com no máx 10 caracteres: {cores.color("limpa")}')).strip().lower().capitalize()   
        elif produto.replace(' ','').isalnum() != True:
            produto = str(input(f'{cores.color("vermelho")}Digite um valor válido para produto: {cores.color("limpa")}')).strip().lower().capitalize() 
        elif produto in existente:
            produto = str(input(f'{cores.color("vermelho")}Produto existente na base, favor inserir um outro nome de produto: {cores.color("limpa")}')).strip().lower().capitalize()
    

    quantidade = str(input(f'{cores.color("verde")}Nova quantidade: {cores.color("limpa")}')).strip()
    while quantidade.isnumeric() != True:
        quantidade = str(input(f'{cores.color("vermelho")}Digite um valor válido para quantidade: {cores.color("limpa")}')).strip()
        

    #não permite o usuário escrever um número com vírgula e sem números depois dela
    

    preco = str(input(f'{cores.color("verde")}Novo preço: {cores.color("limpa")}R$')).strip().replace('.',',')
    while preco.replace('.','').replace(',','').isnumeric() != True:
        preco = str(input(f'{cores.color("vermelho")}Digite um valor válido para o preço: {cores.color("limpa")}R$')).strip().replace('.',',')

    cont = ValidaPreco(preco)          
    while cont > 1 and preco.isnumeric() != True:
        preco = str(input(f'{cores.color("vermelho")}Número inválido, digite novamente: {cores.color("limpa")}R$')).strip().replace('.',',')
        cont = ValidaPreco(preco)
    
    verifica = VerificaDecimal(preco)
    while verifica != True and preco.isnumeric() != True:
        preco = str(input(f'{cores.color("vermelho")}Número inválido, digite novamente: {cores.color("limpa")}R$')).strip().replace('.',',')
        verifica = VerificaDecimal(preco)

    for deletar in range(int(opcao),int(opcao)+3):
        del novaLista[int(opcao)]
        
    
    novaLista.insert(int(opcao),f'Produto;{produto}\n')
    novaLista.insert(int(opcao)+1,f'Quantidade;{quantidade}\n')
    novaLista.insert(int(opcao)+2,f'Preço;{preco}\n')
    
    with open('produtos.txt','w',encoding='utf-8') as arquivo:
        for item in novaLista:
            arquivo.write(item)
    print(f'{cores.color("verde")}{nome}{cores.color("limpa")} {cores.color("amarelo")}foi alterado com sucesso!{cores.color("limpa")}')
    sleep(1.5)
    loja.menuAdm([f'{cores.color("roxo")}Cadastrar Produto{cores.color("limpa")}',f'{cores.color("amarelo")}Alterar Produto{cores.color("limpa")}', f'{cores.color("verde")}Deletar Produto{cores.color("limpa")}',f'{cores.color("azul")}Ver Produtos{cores.color("limpa")}',f'{cores.color("vermelho")}Sair do Sistema{cores.color("limpa")}'])    
        
    
def Deletar():
    arq = open('produtos.txt','r',encoding='utf-8')
    identificar = {}
    for i,nome in enumerate(arq):        
        if 'Produto' in nome:
            identificar[i] = nome.replace('Produto;','').replace('\n','')


    lista = []

    for key, value in identificar.items():
        lista.append(key)
    identificar.clear()


    while True:
        Visualizar(1)
        arquivo = open('produtos.txt','r',encoding='utf-8')

        #Validação do ID que o usuário insere
        print(f'{cores.color("amarelo")}Caso não queira deletar nenhum item, digite: 0{cores.color("limpa")}')
        item = str(input(f'{cores.color("roxo")}ID do item que deseja excluir: {cores.color("limpa")}')).strip()
        if item == '0':
            break
        while item.isnumeric() != True:
            item = str(input(f'{cores.color("roxo")}Digite um ID válido do item que deseja excluir: {cores.color("limpa")}')).strip()
            
        while int(item) not in lista:
            item = str(input(f'{cores.color("roxo")}Digite um ID válido do item que deseja excluir: {cores.color("limpa")}')).strip()
            while item.isnumeric() != True:
                item = str(input(f'{cores.color("roxo")}Digite um ID válido do item que deseja excluir: {cores.color("limpa")}')).strip()
        dados = arquivo.readlines()
        print(f'{cores.color("limpa")}')
        
        #Captura nome do item que deseja excluir
        produto = dados[int(item)].replace('Produto;','').replace('\n','')
        arquivo.close()
        deletar = open('produtos.txt','w',encoding='utf-8')
        #Deleta os dados específicos escolhidos pelo usuário
        for i in range(int(item),int(item)+3):
            del dados[int(item)]
        print(f'{cores.color("verde")}{produto}{cores.color("limpa")}',end=' ')
        print(f'{cores.color("amarelo")}foi excluído com sucesso da base de dados.{cores.color("limpa")}')
        #Adiciona a lista nova, com o item escolhido já apagado
        for i in dados:
            deletar.write(i)
        deletar.close()
        Visualizar(1)
        opcao = str(input(f'{cores.color("azul")}Deseja apagar outro produto [S/N] {cores.color("limpa")}')).upper().strip()[0]
        while opcao not in 'SsnN':
            opcao = str(input(f'{cores.color("vermelho")}Digite uma opção válida para apagar ou não um produto [S/N] {cores.color("limpa")}')).upper().strip()[0]
        if opcao == 'N':
            break
    loja.menuAdm([f'{cores.color("roxo")}Cadastrar Produto{cores.color("limpa")}',f'{cores.color("amarelo")}Alterar Produto{cores.color("limpa")}', f'{cores.color("verde")}Deletar Produto{cores.color("limpa")}',f'{cores.color("azul")}Ver Produtos{cores.color("limpa")}',f'{cores.color("vermelho")}Sair do Sistema{cores.color("limpa")}'])       
           
def Sair():
    print(f'{cores.color("verde")}Encerrando o sistema...Até logo!{cores.color("limpa")}')
    shutdown()