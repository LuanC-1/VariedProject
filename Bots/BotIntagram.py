from instapy import InstaPy
from instapy.util import smart_run

# Credenciais de acesso Instagram
insta_username = 'UserInstagram'
insta_password = 'PasswordsInstagram'

# Configurar o executavel do Navegador

session = InstaPy(
    username=insta_username,
    password=insta_password,
    browser_executable_path=r"C:\Program Files\Mozilla Firefox\firefox.exe"

)

# Comentarío que será inserido na foto

comentarios = [
    '.'
]

# Usando o objeto session,declarado anteriormente, abrimos uma smart_run do InstaPy
with smart_run(session):

    # Configurações gerais
    session.set_relationship_bounds(
        enabled=False,
        potency_ratio=None,
        delimit_by_numbers=True,
        max_followers=4590,
        min_followers=45,
        min_following=77)

    # Aqui precisei configurar o skip_private para False
    # Caso contrário o InstaPy ignora contas configuradas
    # Como privadas, mesmo sendo seu amigo
    session.set_skip_users(skip_private=False)

    # Aqui estamos setando a matriz de comentários
    session.set_comments(comentarios)
    # Em seguida estamos dizendo ao bot que ele irá comentar
    # Em 100% das fotos que visitar
    session.set_do_comment(enabled=True, percentage=100)

    # Aqui estamos dizendo ao bot para dar o like em 100% dos posts
    session.set_do_like(True, percentage=100)

    # Definir a lista de perfis nos quais você irá comentar e dar like
    # Nas fotos e vídeos
    # O primeiro parâmetro é a lista de perfis
    # Amount=10 é a quantidade de posts que o bot irá visitar
    # Randomize=True diz para o bot pegar posts aleatoriamente, ao invés de
    # Dos mais novos para os mais antigos
    # Media='None' significa fotos e vídeos
    # Se quiser apenas fotos, use media='Photo', se quiser vídeo use Media='Video'

    session.interact_by_users(
        ['profile that will like'],
        amount=10,
        media='Photo'
    )
