# Índices
nome = input("Insira um nome: ")
# Trará a letra que estiver no 0(E a primeira letra, tendo em vista que a contagem começa do 0)
print(f"Letra atual: {nome[0]}")
# Trará a letra na posição 0 até 3(Três primeiras letras)
print(f"Letra atual: {nome[0:3]}")
# Começara a contagem de trás para frente
print(f"Letra atual: {nome[-2]}")

# Imutabilidade

# Identidade do objeto(sequencia dos caracteres)
# Uma String vai receber dois valores,mas a identidade do objeto se altera, garantindo integridade
# Identidade no Python é o valor de referência do endereço de memória
name = input("Insira um nome: ")
name1 = id(name)
print(f"Id : {name1}")
name = input("Insira um Nome: ")
name1 = id(name)
print(f"Id : {name1}")

# Comprimento da String
nameone = input("Insira um nome: ")
namelen = len(nameone)
print(f"Comprimento do Nome : {namelen}")

# Concatenando String
String1 = input("Insira um nome: ")
String2 = input("Insira um sobrenome: ")
String3 = f"Nome: {String1} \nSobrenome: {String2}"
string4 = String2 + " " + String2

print(f"Usuário{string4}")
print(f"Usuário: \n{String3}")
print("Usuário: \n" + String3)
print("Usuário \n{}".format(String3))

# Comparação de Strings
nameon = input("Insira um nome: ")
nametw = input("Insita um nome: ")
# is e == equivale a igual
if nameon is nametw:
    print(f"Iguais")
else:
    print(f"Diferentes !")

# Procurando Subtrings dentro de uma String
mensage = 'O que é Python'
print(mensage.find('Python'))

# Substituir String, primeiro 'valor a ser substituido' 'Novo valor'
mensagem = 'Sou Python'
nova_mensagem = mensagem.replace('Python', 'Java')
print(nova_mensagem)

# Separando string
mensage = 'Hello World, for my friends'
new_mensage = mensage.split(' ')
print(type(new_mensage))
print(new_mensage)

# Converter String as letras todas para Maisculo
mensagem = 'eu gosto de Java'
nova_mensagem = mensagem.upper()
print(nova_mensagem)

# Converter String as letras todas para Minusculo
mensagem = 'eu gosto de Java'
nova_mensagem = mensagem.lower()
print(nova_mensagem)

# Estruturas de Repetições

# For percorre todos os itens da lista
newname = input("Insira um nome: ")
newnameone = input("Insira um nome: ")
nomes = [newname, newnameone]
for n in nomes:
    print(n)

# While definimos condições para que sejam executadas
counter = 0
while counter < 5:
    print(counter)
    counter = counter + 1


# Resume:

frase = 'frase um dois'
# print (frase[9]) #print (frase[9:12]) ele ira pegar até o 11 cortando a casa 12
# (frase[9:12:2]) pula de dois em dois
# (frase[:5]) ele começa do 0 e vai ate o 5
# (frase[5:]) ele começa do 5 e vai ate o final
# (frase[5::3]) ele começa do 5 e vai ate o final de 3 em 3
# print(len(frase)) #Len conta o tamanho da string
# print(frase.count('s')) # count conta quantas string tem do que estiver entre ''
# print(frase.count('s',0,5)) # count conta quantas string tem do que estiver entre '' começando do 0 e indo ate o 4 pois o 5 não conta
# print(frase.find('um')) #Fin vai procurar o conteudo '' e ira mostrar em qual 'casa' ele começa,seria posição da String #caso receba o valor -1 e pq não existe o conteudo
# print('curso' in frase) #ira procurar a palavra curso na string frase #retornando true e false

n = input('Digite algo: ')
print('Qual o tipo primitivo? ', type(n))
print('E Alfanumerico? ', n.isalnum())
print('E alfabetico? ', n.isalpha())
print('Está em maisculo? ', n.isupper())
print('Está em minusculo? ', n.islower())
print('Posso mostrar esse dado informado? ', n.isprintable())
# Capitalizado quer dizer que a letra está em maiusculo e minusculo ao mesmo tempo;
print('Está Capitalizado? ', n.istitle())

# print(s.isnumeric()) mostra se o valor de s e numero ou não
# print(s.isalpha()) mostra se o valor de s e letra ou não
# print(s.isalnum()) mostra se o valor de s e letra ou numero
# print(s.isupper()) mostra se o valor de s a letra esta maiusculo
