#ATIVIDADE

import re, validacpf
import re, validacnpj

saldo = 0.0 

score = 2000

while True:
    try:
        opcao = int(input("Seja bem-vindo. Selecione o que deseja fazer: 1 - Cadastrar-se\n2 - Depositar\n3 - Sacar\n4 - Consultar saldo\n5 - Alterar senha de acesso\n6 - Consultar score\n7 - Sair"))   
        
        #cadastrar cliente

        if opcao == 1:
            try:
                while True:
                    tipo = int(input("Digite o tipo de conta que deseja abrir: 1-Pessoa Física\n2 - Pessoa Jurídica"))
                    if tipo == 1:
                        while True:
                            
                            cpf = input("Digite seu CPF completo (formato XXX.XXX.XXX-XX): ")
                            
                            if(validacpf.validar_cpf(cpf)):
                                print("CPF correto")
                                break
                            else:
                                print("CPF inválido!")
                    elif tipo == 2:
                        while True:
                            
                            cnpj = input("Digite o CNPJ da pessoa jurídica (formato XX.XXX.XXX/XXXX-XX): ")
                            
                            if(validacnpj.validar_cnpj(cnpj)):
                                print("CNPJ correto")
                                break
                            else:
                                print("CNPJ inválido!")
                    else:
                        print("Opção inválida!")
                    break
                        
                
                from datetime import datetime 

                while True:
                    
                    entrada = input("Digite sua data de nascimento (dd/mm/aaaa): ").strip()
                    
                    try:
                        
                        data_nascimento = datetime.strptime(entrada, "%d/%m/%Y")
                        
                        if data_nascimento > datetime.now():
                            print("Erro: A data de nascimento não pode ser no futuro.")
                            continue
                            
                        break  
                        
                    except ValueError:
                        print("Formato inválido! Certifique-se de usar números e barras. Ex: 25/12/2000")

                print(f"Data armazenada: {data_nascimento.strftime('%d/%m/%Y')}")

                while True:
                    rg = input ("Digite o número do seu RG, caso tenha, ou enter para continuar ") 
                    break
                
                while True:
                    cliente = input("Digite seu nome: ").strip().upper()

                    if len(cliente) <3:
                        print("Número de letras insuficientes.")
                        continue
                    if not cliente:
                        print("Campo vazio. Preencha seu nome")
                    if not cliente.replace(" ", "").isalpha():
                        print("Seu nome não pode conter números!")
                    else:
                        print("Nome registrado!")
                        break
                
                while True:
                    rua = input("Digite o nome da sua rua: ")
                    if not rua:
                        print("Campo não pode ficar vazio!")
                    if not rua.replace(" ", "").isalpha():
                        print("O nome da sua rua não pode ter números")
                    else:
                        print("Dado armazenado")
                        break
                while True:
                    
                    casa = input("Digite o número da sua residência: ")

                    if not casa:
                        print("Número da casa ou edifício é obrigatório!")
                    else:
                        print("Número armazenado com sucesso!")
                        break

                while True:
                    complemento = input("Digite o complemento do seu endereço, cajo haja, ou enter para continuar: ")
                    break
                    
                while True:
                    
                    padraocep = r"^\d{5}-\d{3}$"

                    cep = input ("Digite o CEP do seu endereço (formato XXXXX-XXX): ")
                    
                    if(re.match(padraocep, cep)):
                        print("CEP registrado")
                        break
                    else:
                        print("Formato de CEP inválido!")
                        continue
                
                while True:

                    cidade = input("Digite o nome da sua cidade: ")

                    if not cidade.replace(" ", "").isalpha():
                        print(f"Cidade cadastrada: {cidade}")
                        break
                    else:
                        print("Não pode conter números no nome da cidade")
                        continue
                
                while True:

                    estado = input("Digite o nome do seu estado: ")

                    if not estado.replace(" ", "").isalpha():
                        print(f"Estado cadastrado: {estado}")
                        break
                    else:
                        print("Não pode conter números no nome do estado")
                        continue

                while True:
                    padraoemail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                    
                    email = input("Digite seu email: ")
                    
                    if(re.match(padraoemail,email)):
                        print("Email validado com sucesso!")
                        break
                    else:
                        print("Email inválido!")

                while True:
                    telefone = int(input("Digite seu número com DDD:").strip().lower())

                    if not telefone:
                        print("Campo não pode ficar vazio")
                    else:
                        print("Número de telefone armazenado!")
                        break
                    
                    print("Cadastro concluído com sucesso")


            except Exception as e:
                print(f"Ocorreu um erro", e) 


        elif opcao == 2:

            #depositar dinheiro

            
            deposito = float(input("Digite o valor que vai depositar: "))

            if not deposito:
                print("Digite um valor válido: ")
            else:
                print("Insira as notas no caixa")

                
            tiposconta = ["corrente", "poupança", "poupanca"]

            contaReceber = input("Digite o tipo de conta que vai receber o valor: Corrente ou Poupança").strip().lower()

            if contaReceber in tiposconta:
                saldo = saldo + deposito 
                print(f"Depósito de {deposito:.2f} reais feito com sucesso! Seu saldo atual é de {saldo}")
                if deposito > 10000:
                    score+=1000
                    print(f"Com seu depósito, seu score aumentou em 1.000 pontos")
                
            else: 
                print("Forma de pagamento inválida") 

            
        
        elif opcao == 3:
            #sacar dinheiro
            
            try:
                
                conta = int(input("Digite o número da sua conta: "))
                
                if not conta:
                    print("Número de conta inválido: ")
                else:
                    print("Siga para o próximo passo")

                senha = input("Digite sua senha: ")

                if not senha:
                    print("Senha inválida!")
                else:
                    print("Siga para o próximo passo")

                saque = float(input("Digite o valor que deseja sacar: "))

                if not saque:
                    print("Você não preencheu corretamente!")
                
                elif saque > saldo:
                    print(f"Seu valor de saque não pode ser maior que seu saldo. Você tem {saldo} reais depositados.")

                else: 
                    saldo = saldo - saque 
                    print("Retire suas notas")

            except Exception as e:
                print(f"Ocorreu um erro: {e}") 



            

        elif opcao == 4:
            
            #consultar saldo

            try:
                
                
                conta = int(input("Digite o número da sua conta: "))
                
                if not conta:
                    print("Número de conta inválido: ")
                else:
                    print("Siga para o próximo passo")

                senha = input("Digite sua senha: ")

                if not senha:
                    print("Senha inválida!")
                else:
                    print(f"Seu saldo atual é de {saldo}") 

            except Exception as e:
                print(f"Ocorreu um erro: {e}") 

            
        elif opcao == 5:
        
            #alterar senha
            
            contaSenha = int(input("Digite o número da sua conta: "))
            
            if not contaSenha:
                    print("Digite o número da sua conta")
            else:
                    print("Conta validada.")
                    

            try:
                while True:
                    senhaAntiga = input("Digite sua senha antiga: ")

                    if not senhaAntiga == "23235656":
                        print("Senha inválida. Tente novamente.")
                        break
            except Exception as e:
                print(e)
                
        elif opcao == 6:
            
            print(f"Seu score atual é de {score}")
        
        
        elif opcao == 7:
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida!")
    
    
    except Exception as e:
                print(e)