import psycopg2


def ConexaoDB():
    con = psycopg2.connect(host='localhost',
                           database='bakery',
                           user='postgres',
                           password='Aa@147852369')
    return con
