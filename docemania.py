import os
import random
from datetime import date
import arqs


data_atual = date.today()

doces_dic={}
clientes_dic={}
vendas_dic={}

clientes_dic = arqs.read_all('clientes.dat')
doces_dic = arqs.read_all('doces.dat')
vendas_dic = arqs.read_all('vendas.dat')




########################################################################################################################################################

# TELA INICIAL #
def inicial():
    os.system("clear")
    print("########################################################")
    print("#                   < DOCE MANIA >                     #")
    print("#                                                      #")
    print("#  1. DOCES                                            #")
    print("#  2. CLIENTES                                         #")
    print("#  3. VENDAS                                           #")
    print("#  4. RELATÓRIOS                                       #")
    print("#  5. INFORMAÇÕES                                      #")
    print("#  0. SAIR                                             #")
    print("#                                                      #")
    print("########################################################")

    blablabla = input("Digite o que você desejaria realizar no programa: ")
    return blablabla

def doces():
    os.system("clear")
    print("########################################################")
    print("#                   < DOCE MANIA >                     #")
    print("#                     > DOCES <                        #")
    print("#                                                      #")
    print("#  1. CADASTRO DE DOCES                                #")
    print("#  2. PESQUISA DE DOCES                                #")
    print("#  3. EDIÇÃO DE DOCES                                  #")
    print("#  4. DELETAR DOCES                                    #")
    print("#  0. RETORNAR AO MENU INICIAL                         #")
    print("#                                                      #")
    print("########################################################")

    blablabla = input("Digite o que você desejaria realizar no programa: ")
    return blablabla

def clientes():
    os.system("clear")
    print("########################################################")
    print("#                   < DOCE MANIA >                     #")
    print("#                    > CLIENTES <                      #")
    print("#                                                      #")
    print("#  1. CADASTRO DE CLIENTES                             #")
    print("#  2. PESQUISA DE CLIENTES                             #")
    print("#  3. EDIÇÃO DE CLIENTES                               #")
    print("#  4. DELETAR CLIENTES                                 #")
    print("#  0. RETORNAR AO MENU INICIAL                         #")
    print("#                                                      #")
    print("########################################################")

    blablabla = input("Digite o que você desejaria realizar no programa: ")
    return blablabla

def vendas():
    os.system("clear")
    print("########################################################")
    print("#                   < DOCE MANIA >                     #")
    print("#                     > VENDAS <                       #")
    print("#                                                      #")
    print("#  1. CADASTRO DE VENDAS                               #")
    print("#  2. PESQUISA DE VENDAS                               #")
    print("#  3. CANCELAR VENDAS                                  #")
    print("#  0. RETORNAR AO MENU INICIAL                         #")
    print("#                                                      #")
    print("########################################################")

    blablabla = input("Digite o que você desejaria realizar no programa: ")
    return blablabla

def informacoes():
    os.system("clear")
    print("########################################################")
    print("#                   < DOCE MANIA >                     #")
    print("#                   > INFORMAÇÕES <                    #")
    print("#                                                      #")  
    print("#  AUTORIA - YASMIM DANTAS (@yasmimdanntass)           #")
    print("#  ORIENTAÇÃO - ARON SILVA (@AronSilva4)               #")
    print("#  OBJETIVO - PROMOVER A ORGANIZAÇÃO EMPRESARIAL DE    #")
    print("#  UM ESTABELECIMENTO ALIMENTÍCIO.                     #")
    print("#                                                      #")
    print("########################################################")
    print()
    input("TECLE ENTER PARA RETORNAR À TELA DE INÍCIO")
########################################################################################################################################################

# Cadastro de produtos 
def cadastro_doces():
    print()
    print("Olá! Você está na tela de cadastro de doces.")
    print("Para prosseguir, preencha as informações solicitadas.")
    print()
    
    while True:
        desc_prod = input("Insira uma breve descrição do produto: ")
        if desc_prod.replace(" ", "").isalpha():
            print("Nome válido!")
            break
        else:
            print("Nome inválido! Insira-o novamente certificando-se de que possui apenas caracteres alfabéticos.")
            

    cod_prod = input("Insira o código do produto (à sua escolha e diferente dos demais): ")
    while cod_prod in doces_dic:
        print("Código já utilizado em outro produto. Escolha outro!")
        cod_prod = input("Insira o código do produto (à sua escolha e diferente dos demais): ")
    else:
        print("Código de produto disponível!")

    qtd_prod = input("Insira a quantidade de produtos disponíveis: ")

    while qtd_prod.isnumeric() == False:
        qtd_prod = input("Valor inválido! Insira um valor numérico inteiro: ")
        
    qtd_prod = int(qtd_prod)
        
    valor_prod = input("Insira o valor do produto (com valor flutuante e ponto para indicar a casa decimal): R$")
    
    ponto = "."
    valor_sem_ponto = 0
    
    
    if ponto in valor_prod:
        valor_sem_ponto = valor_prod.replace(".", "")
        while valor_sem_ponto.isnumeric() == False:
            valor_sem_ponto = input("Valor inválido! Insira um valor numérico flutuante (seguindo o modelo - R$xx.x): R$")

    while ponto not in valor_prod:
        valor_prod = input("Valor inválido! Insira um valor numérico flutuante (R$xx.xx): R$")
    
    valor_prod = float(valor_prod)
    data_prod = "{}/{}/{}".format(data_atual.day, data_atual.month, data_atual.year)
    doces_dic[cod_prod] = [desc_prod, cod_prod, qtd_prod, valor_prod, data_prod]
    arqs.insert('doces.dat', doces_dic)
    print()
    print("Cadastro de doce concluído!")
    input("TECLE ENTER PARA PROSSEGUIR")

# Pesquisa de produtos
def pesquisa_doces():
    print()
    print("Olá! Você está na tela de pesquisa de doces.")
    cod_prod = input("Para prosseguir, insira o código do produto desejado: ")
    if cod_prod in doces_dic:
        print()
        print(f"Descrição do produto: {doces_dic[cod_prod][0]}")
        print(f"Código do produto: {doces_dic[cod_prod][1]}")
        print(f"Quantidade de produtos: {doces_dic[cod_prod][2]}")
        print(f"Valor do produto: R${doces_dic[cod_prod][3]}")
        print(f"Cadastro efetuado em {doces_dic[cod_prod][4]}")

        print()
        print("Pesquisa de doce concluída!")
        print()
        input("TECLE ENTER PARA PROSSEGUIR")

    else:
        print()
        print("Código de produto não encontrado!")
        print()
        input("TECLE ENTER PARA PROSSEGUIR")


# Edição de produtos  
def edicao_doces():
    print()
    print("Olá! Você está na tela de edição de doces.")
    cod_prod = input("Para prosseguir, insira o código do produto desejado: ")
    if cod_prod in doces_dic:
        print()
        desc_prod = input("Insira a alteração na descrição do produto: ")
        qtd_prod = int(input("Insira a alteração na quantidade de produtos disponíveis: "))
        valor_prod = float(input("Insira o novo valor do produto: R$"))
        data_prod = "{}/{}/{}".format(data_atual.day, data_atual.month, data_atual.year)
        doces_dic[cod_prod] = [desc_prod, cod_prod, qtd_prod, valor_prod, data_prod]
        arqs.insert('doces.dat', doces_dic)
        print(f"Data de cadastro agora refere-se ao dia {doces_dic[cod_prod][4]}")
        print()
        print("Edição concluída!")
        print()
        input("TECLE ENTER PARA PROSSEGUIR")

    else:
        print()
        print("Código de produto não encontrado!")
        print()
        input("TECLE ENTER PARA PROSSEGUIR")


# Deleção de produtos
def delecao_doces():
    print()
    print("Olá! Você está na tela de deleção de doces.")
    cod_prod = input("Para prosseguir, insira o código do produto desejado: ")
    if cod_prod in doces_dic:
        del doces_dic[cod_prod]
        arqs.insert('doces.dat', doces_dic)
        arqs.insert('doces.txt', doces_dic)
        print()
        print("Deleção de doce concluída!")
        print()
        input("TECLE ENTER PARA PROSSEGUIR")

    else:
        print()
        print("Código de produto não encontrado!")
        print()
        input("TECLE ENTER PARA PROSSEGUIR")

########################################################################################################################################################

# Cadastro de clientes

def cadastro_clientes():
    print()
    print("Olá! Você está na tela de cadastro de seus clientes.")
    print("Para prosseguir, preencha as informações solicitadas.")
    substring = " "
    while True:
        nome_cliente = input("Insira o nome do cliente: ")
        
        if substring in nome_cliente and nome_cliente.replace(" ", "").isalpha():
            print("Valor válido!")
            break
        else:
            print("Nome inválido! Insira-o novamente certificando-se de que possui apenas caracteres alfabéticos.")

    cpf_cliente = 0

    while True:
        cpf_cliente = input("Insira o CPF do cliente: ")

        if cpf_cliente in clientes_dic:
            print("CPF já existe. Insira um CPF diferente.")
            continue 

        if len(cpf_cliente) == 11 and cpf_cliente.isdigit() and cpf_cliente != cpf_cliente[::-1]:
            # PRIMEIRA VALIDAÇÃO
            valor_final = sum(int(cpf_cliente[i]) * (10 - i) for i in range(9))
            resto = valor_final % 11

            if (resto <= 1 and cpf_cliente[9] == "0") or (resto >= 2 and cpf_cliente[9] == str(11 - resto)):
                # SEGUNDA VALIDAÇÃO
                valor_final = sum(int(cpf_cliente[i]) * (11 - i) for i in range(10))
                resto = valor_final % 11

                if (resto <= 1 and cpf_cliente[10] == "0") or (resto >= 2 and cpf_cliente[10] == str(11 - resto)):
                    print("CPF Válido!")
                    break
                else:
                    print("Valor inválido! Certifique-se de que o CPF do cliente é existente.")
            else:
                print("Valor inválido! Certifique-se de que o CPF do cliente é existente.")
        else:
            print("Valor inválido! Certifique-se de que o CPF do cliente possui 11 caracteres e não é um palíndromo.")
        
    data_cadastro = "{}/{}/{}".format(data_atual.day, data_atual.month, data_atual.year)
    clientes_dic[cpf_cliente]=[nome_cliente, cpf_cliente, data_cadastro]
    arqs.insert('clientes.dat', clientes_dic)
    print(f"Cadastro de cliente concluído em {data_cadastro}!")
    input("TECLE ENTER PARA PROSSEGUIR")
    

# Pesquisa de clientes

def pesquisa_clientes():
    print()
    print("Olá! Você está na tela de pesquisa de clientes.")
    cpf_cliente = input("Para prosseguir, insira o CPF do cliente: ")
    if cpf_cliente in clientes_dic:
        print()
        print(f"Nome do cliente: {clientes_dic[cpf_cliente][0]}")
        print(f"CPF: {clientes_dic[cpf_cliente][1]}")
        print(f"Data do cadastro: {clientes_dic[cpf_cliente][2]}")
        print()
        print("Pesquisa de cliente concluída!")
        print()
        input("TECLE ENTER PARA PROSSEGUIR")

    else:
        print()
        print("CPF do cliente não encontrado!")
        print()
        input("TECLE ENTER PARA PROSSEGUIR")

# Edição de clientes

def edicao_clientes():
    print()
    print("Olá! Você está na tela de edição de clientes.")
    cpf_cliente = input("Para prosseguir, insira o CPF do cliente: ")
    if cpf_cliente in clientes_dic:
        nome_cliente = input("Insira o nome completo alterado do cliente: ")
        data_cadastro = "{}/{}/{}".format(data_atual.day, data_atual.month, data_atual.year)
        clientes_dic[cpf_cliente]=[nome_cliente, cpf_cliente, data_cadastro]
        arqs.insert('clientes.dat', clientes_dic)
        
        print()
        print("Edição concluída!")
        print()
        input("TECLE ENTER PARA PROSSEGUIR")

    else:
        print()
        print("CPF do cliente não encontrado!")
        print()
        input("TECLE ENTER PARA PROSSEGUIR")

# Deleção de clientes

def delecao_clientes():
    print()
    print("Olá! Você está na tela de deleção do cadastro de clientes.")
    cpf_cliente = input("Para prosseguir, insira o CPF do cliente: ")
    if cpf_cliente in clientes_dic:
        del clientes_dic[cpf_cliente]
        arqs.insert('clientes.dat', clientes_dic)
        
        print()
        print("Deleção de cadastro do cliente concluída!")
        print()
        input("TECLE ENTER PARA PROSSEGUIR")
    else:
        print()
        print("CPF do cliente não encontrado!")
        print()
        input("TECLE ENTER PARA PROSSEGUIR")

########################################################################################################################################################

# Cadastro de vendas
def cadastro_vendas():
    print()
    print("Olá! Você está na tela de cadastro de vendas.")
    print("Para prosseguir, preencha as informações solicitadas.")
    print()

    id_venda = random.randint(1000, 9999)
    print(f"O ID da venda é {id_venda}")
    print()

    cod_prod = input("Insira o código do produto em transação: ")

    if cod_prod in doces_dic:
      print(f"O produto foi encontrado no cadastro! Se trata de {doces_dic[cod_prod][0]}.")
      print()

      cpf_cliente_venda = input("Insira o CPF do cliente participante da venda: ")
      print()

      if cpf_cliente_venda in clientes_dic:
        print("O CPF foi encontrado em nosso sistema!")
        print()
        
        while True:
            qtd_prod_venda = (input("Insira a quantidade de produtos na venda: "))
            if qtd_prod_venda.isdigit():
                qtd_prod_venda = int(qtd_prod_venda)

                if 0 < qtd_prod_venda <= doces_dic[cod_prod][2]:
                    print("Há produtos disponíveis!")
                    break
                else:
                    print("Quantidade inválida! Insira novamente a quantidade de produtos na venda.")
            else:
                print("Valor inválido! Insira novamente a quantidade de produtos na venda.")

        qtd_prod_venda = float(qtd_prod_venda)

        valor_prod_venda = doces_dic[cod_prod][3]
        valor_prod_venda = float(valor_prod_venda)
        valor_venda = qtd_prod_venda * valor_prod_venda
        valor_venda = float(valor_venda)

        data_venda = "{}/{}/{}".format(data_atual.day, data_atual.month, data_atual.year)

        vendas_dic[id_venda] = [id_venda, cod_prod, cpf_cliente_venda, qtd_prod_venda, valor_venda, data_venda]

        doces_dic[cod_prod][2] = doces_dic[cod_prod][2] - qtd_prod_venda
        arqs.insert('vendas.dat', vendas_dic)
        arqs.insert('doces.dat', doces_dic)
       
        print(f"O valor final da transação é de R${valor_venda:.2f}")
        print(f"Serviço efetuado em {data_venda}")
        input("TECLE ENTER PARA PROSSEGUIR")


      else:
        print("O CPF não foi registrado em antecipação! Você será direcionado à tela de início para realizar o cadastro.")
        input("TECLE ENTER PARA PROSSEGUIR")
        var_inicial = inicial()

    else: 
        print("O produto não foi encontrado em nosso sistema. Você será direcionado para realizar o cadastro na tela de início!")
        input("TECLE ENTER PARA PROSSEGUIR")
        inicial()




def pesquisa_vendas():
    print("Olá! Você está na tela de pesquisa de vendas.")
    id_venda = input("Para prosseguir, insira o ID da venda: ")
    if id_venda in vendas_dic:
        print()
        print(f"ID da venda: {vendas_dic[id_venda][0]}")
        print(f"Código do produto: {vendas_dic[id_venda][1]}")
        print(f"CPF do cliente: {vendas_dic[id_venda][2]}")
        print(f"Quantidade de produtos: {vendas_dic[id_venda][3]}")
        print(f"Valor final: {vendas_dic[id_venda][4]}")
        print(f"Data da venda: {vendas_dic[id_venda][5]}")
        print()
        print("Pesquisa de venda concluída!")
        print()
        input("TECLE ENTER PARA PROSSEGUIR")

    else:
        print()
        print("ID da venda não encontrado!")
        print()
        input("TECLE ENTER PARA PROSSEGUIR")

def delecao_vendas():
   print()
   print("Olá! Você está na tela de cancelamento de vendas.")   
   id_venda =  input("Para prosseguir, insira o ID da venda que gostaria de cancelar")
   if id_venda in vendas_dic:
       del vendas_dic[id_venda]
       arqs.insert('vendas.dat', vendas_dic)
       arqs.insert('doces.dat', doces_dic)
       
       print()
       print("Deleção de cadastro do cliente concluída!")
       print()
       input("TECLE ENTER PARA PROSSEGUIR")
   else:
       print()
       print("ID da venda não encontrado!")
       print()
       input("TECLE ENTER PARA PROSSEGUIR")


#Relatórios
       
def relatorios():
    print()
    print("Olá! Você está na tela de relatórios.")
    print()
    print("Para prosseguir, digite:")
    print("[1] - Para visualizar dados dos doces disponíveis.")
    print("[2] - Para visualizar dados dos clientes.")
    print("[3] - Para visualizar dados das vendas")
    print("[0] - Para retornar à tela de início")
    print()
    resposta = input()
    print()
    if resposta == "1":
        print(f"Os dados sobre doces disponíveis são:")
        print()
        arquivos_doces = arqs.read_all("doces.dat")
        for line in arquivos_doces:
            print("Descrição: ", doces_dic[line][0], "Código: ", doces_dic[line][1], "Estoque: ", doces_dic[line][2], "Preço: ", doces_dic[line][3], "Data de Cadastro: ", doces_dic[line][4])           
        input("TECLE ENTER PARA PROSSEGUIR")
    elif resposta == "2":
        print(f"Os dados sobre clientes disponíveis são:")
        print()
        arquivos_clientes = arqs.read_all("clientes.dat")
        for line in arquivos_clientes:
            print("Nome: ", clientes_dic[line][0], "CPF: ", clientes_dic[line][1], "Data de cadastro: ", clientes_dic[line][2])
        input("TECLE ENTER PARA PROSSEGUIR")
        
    elif resposta == "3":
        print(f"Os dados sobre vendas disponíveis são:")
        print()
        arquivos_vendas = arqs.read_all("vendas.dat")
        for line in arquivos_vendas:
            print("ID: ", vendas_dic[line][0], "Código do produto: ", vendas_dic[line][1], "CPF do cliente: ", vendas_dic[line][2], "Quantidade de produtos: ", vendas_dic[line][3], "Data de cadastro: ", vendas_dic[line][4])
        input("TECLE ENTER PARA PROSSEGUIR")
        
    elif resposta == "0":
        input("TECLE ENTER PARA PROSSEGUIR")
        
    else:
        print(f"Resposta inválida! Você será enviado novamente à tela de início!")
        input("TECLE ENTER PARA PROSSEGUIR")
        

    


########################################################################################################################################################


# PROCESSAMENTO CENTRAL 

var_inicial = inicial()

while var_inicial != "0":
    if var_inicial == "1":
        var_doces = doces()
        while var_doces != "0":
            if var_doces == "1":
               cadastro_doces() 
            elif var_doces == "2":
                pesquisa_doces()
            elif var_doces == "3":
                edicao_doces()
            elif var_doces == "4":
                delecao_doces()
            else:
                print("OPÇÃO INVÁLIDA")
                input("TECLE ENTER PARA PROSSEGUIR")
            var_doces = doces()


    elif var_inicial == "2":
        var_clientes = clientes()
        while var_clientes != "0":
            if var_clientes == "1":
                cadastro_clientes()
            elif var_clientes == "2":
                pesquisa_clientes()
            elif var_clientes == "3":
                edicao_clientes()
            elif var_clientes == "4":
                delecao_clientes()
            else:
                print("OPÇÃO INVÁLIDA")
                input("TECLE ENTER PARA PROSSEGUIR")
            var_clientes = clientes()

    elif var_inicial == "3":
        var_vendas = vendas()
        while var_vendas != "0":
            if var_vendas == "1":
                cadastro_vendas()
            elif var_vendas == "2":
                pesquisa_vendas()
            elif var_vendas == "3":
                delecao_vendas()
            else:
                print("OPÇÃO INVÁLIDA")
                input("TECLE ENTER PARA PROSSEGUIR")
            var_vendas = vendas()

    elif var_inicial == "4":
        var_relatorios = relatorios()

    elif var_inicial == "5":
        var_informacoes = informacoes()


    else:
        print("OPÇÃO INVÁLIDA")
        input("TECLE ENTER PARA PROSSEGUIR")
    var_inicial = inicial()

print()
print("OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS! :)")
