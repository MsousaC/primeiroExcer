nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade :
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido fica {nome[::-1]}')

    if '' in nome:
        print(f'Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços!')    

   
    print(f'Seu nome tem {len(nome)} Letras') 
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última ledra do seu nome é {nome[-1]}')
else:
    print('Desculpa, você deixou campo vazio.')


