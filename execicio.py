"""
Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';

"""
nome = input('Digite o nome: ')
if len(nome) > 3:
    print(f'{nome}')
else:
    print('Nome não valido')

idade = int(input('Digite a idade: '))
if idade > 0:
    print(f'{idade} anos')
else:
    print('Idade não valido')

salario = float(input('Digite o Salario: '))
if salario > 0:
    print(f'Seu salario e R${salario} reais')
else:
    print('salario não valido')


sexo = input('Digite o sexo: ')

if sexo == 'm':
    print(f'O seu sexo e masculino')
elif sexo == 'f':
    print('o sexo e feminino')
else:
    print('sexo não valido')
estado_civil = input('Digite seu estado civil: ')

if estado_civil == 'c':
    print('CASADO(a)')
elif estado_civil == 's':
    print('SOLTEIR0(a)')
elif estado_civil == 'd':
    print('DIVORCIADO(a)')
else:
    print('estado civil envalido')

