# Class
# Sintaxe

from PySimpleGUI import PySimpleGUI as sg

# Nome,Autor,Quatidadepaginas
# class Livro:
#  def __init__(self, autorLivro, nomeLivro, quantidadePaginas) :
#    self.autorLivro = autorLivro
#    self.nomeLivro = nomeLivro
#    self.quantidadePaginas = quantidadePaginas

# Layout
sg.theme('Reddit')

layout = [
    [sg.Text('Autor do Livro'), sg.Input(key='autorLivro')],
    [sg.Text('Nome do Livro'), sg.Input(key='nomeLivro')],
    [sg.Text('Quantidade de Paginas'), sg.Input(key='quantidadePaginas')],
    [sg.Button('Cadastrar')]
]
# Janela
janela = sg.Window('Cadastramento de livros', layout)

# Ler os eventos
while True:
    eventos, valores = janela.Read()
    if eventos == sg.WINDOW_CLOSED:
        break
