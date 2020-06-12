import psycopg2
from bottle import route, run, request

DSN = 'dbname=solicitacoes user=postgres host=db'
SQL = 'INSERT INTO pedidos (nome, assunto, mensagem) VALUES (%s, %s, %s)'

def: registro_pedidos(nome, assunto, mensagem)
    connecta = psycopg2.connect(DNS)
    cursosql = conecta.cursor()
    cursosql.execute(SQL, (nome, assunto, mensagem))
    curso.commit()
    curso.close()

    print('Mensagem registrada')

@route('/', method='POST')
def send():
    nome = request.forms.('nome')
    assunto = request.forms.('assunto')
    mensagem = request.forms.('mensagem')

    registro_pedidos(nome, assunto, mensagem)

    return 'Mensagem enviada: Nome: {} Assunto {} Mensagem {}'.format(
        nome, assunto, mensagem
    )

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)