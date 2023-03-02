# int 7 -4 0 9875
# float  4.5 0.076 -15.223 7.0

# Adicão +
# Subtraçãp -
# Multiplicação *
# Divisão /
# Potência **   pow(n1,n2)(Perde a ordem de procedência)
# Divisão inteira //
# Resto da divisão %
# = recebe
# == igual
# raiz quadrada n1**(1/2) raiz cubica n1**(1/3) pow(n(1/2))

# Metodos math (Calculos matematicos)
# ceil - arredondar pra cima
# floor - arredondar pra baixo
# trunc - elimina depois da virgula
# pow - potência
# sqrt - raiz quadrada
# factorial - fatoração

# Ordem de procedência
# 1- ()
# 2- **
# 3- * // % /
# 4- + -

# Complementos '='*20 --> dentro do '' vai ser reproduzido 20 vezes nesse exemplo
# print('Prazer em te conhecer {:<20}!'.format(exemplo)) --- > Dentro do {} Alinhamentos e o numero 20 seria
# os caracteres que ele vai ocupar sendo maior ou menos ; (:>5,:<5,:5, :^5Centrlizado,:=^5 centraliza e fica cheio de igual envolta do nome)
# {:.3f} --> Exemplo de como diminuir uma soma ou qualquer conta para utilizar menos numeros;
# end = '' Se tiver dois print e vc nao quiser que pule linha adicione o End no final da linha acima da ultima;

# Antecessor e sucessor
# r = int(input('Digite um numero: '))
# a = r - 1
# s = r + 1
# print('Seu Sucessor e {} e seu Antecessor e {}'.format(s,a))

# Dobro,Triplo,Raiz quadrada
# r = float(input('Digite um numero: '))
# d = r * 2
# t = r * 3
# rd = r **(1/2)
# print('Dobro do numero é:{}\nTriplo do numero é: {}\nRaiz quadrada:{:}'.format(d,t,rd))

# Media Aritimetica
# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a Segunda nota: '))
# print('Sua média e : {}'.format((n1+n2)/2))

# Conversor de medidas
# t = float(input('Digite um tamanho em metros para ser convertido em centimetros e milimetros : '))
# c = t * 100
# m = t * 1000
# print('Valor em centimetros é: {} \n Valor em milimetros é: {} '.format(c,m))

# tabuada
# r = int(input('Digite um valor para mostrar a sua tabuada: '))
# print('tabuada do {} =\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format((r),(r*1),(r*2),(r*3),(r*4),(r*5),(r*6),(r*7),(r*8),(r*9),(r*10)))

# Conversor de moedas
# v = float(input('Digite o valor que você queria converter para dolar: '))
# print('Valor convertido é: {}'.format(v/3.27))

# Pintar uma parede
# l = float(input('Digite a largura da parede: '))
# a = float(input('Digite a altura da parede: '))
# r = (l*a)/2
# print('A sua parede tem {}m²\nVocê gastara {} litros de tinta'.format((a*l),(r)))

# Desconto
# v = float(input('Digite o valor do produto: '))
# d = v *0.05
# va = v - d
# print('Valor do produto:{}\nValor do desconto é:{}\nO valor apos o desconto é:{}'.format((v),(d),(va)))

# Aumento de salário
# s = float(input('Digite o valor do seu salario: '))
# a = s * 0.15
# sa = s + a
# print('Seu salário era: {}\nSeu aumento será de : {}\nSeu salário com aumento será:{}'.format((s),(a),(sa)))
