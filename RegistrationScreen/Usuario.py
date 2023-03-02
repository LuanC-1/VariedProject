import ConexaoDB


class usuario:
    def __init__(self, nome, email, endereco, telefone, senha, estado):
        self.__nome = nome
        self.__email = email
        self.__endereco = endereco
        self.__telefone = telefone
        self.__senha = senha
        self.__estado = estado

        def Cadastrar(self):
            con = ConexaoDB()

        def Login(self):
            con = conecta_db()

        def get_nome(self):
            return self.__nome

        def set_nome(self, nome):
            self.__nome = nome

        def get_email(self):
            return self.__email

        def set_email(self, email):
            self.__email = email

        def get_endereco(self):
            return self.__endereco

        def set_endereco(self, endereco):
            self.__endereco = endereco

        def get_telefone(self):
            return self.__telefone

        def set_telefone(self, telefone):
            self.__telefone = telefone

        def get_senha(self):
            return self.__senha

        def set_senha(self, senha):
            self.__senha = senha

        def get_estado(self):
            return self.__estado

        def set_estado(self, estado):
            self.__estado - estado
