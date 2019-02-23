#
# from flask import Flask, request
#
# # objeto Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def principal():
#     return '<html><head><title>Página Inicial</title>' \
#            '</head>' \
#            '<body>' \
#            '<form method="get" action="/exibir">' \
#            '<label for="inome">Nome: </label>' \
#            '<input type="text" name="nome" id="inome"/>' \
#            '<br/>' \
#            '<label for="isn">Sobrenome: </label>' \
#            '<input type="text" name="sn" id="isn"/>' \
#            '<br/>' \
#            '<input type="submit" value="enviar"/>' \
#            '</form>' \
#            '</body>' \
#            '</html>'
#
#
#
# # rota para /nome
#
# @app.route('/nome')
# @app.route('/mn')
# def nome():
#     return 'Pedro Paulo'
#
# # rota para /exibir
# @app.route('/exibir')
# def exibir():
#     nome = request.args.get('nome', default='[nome não informado]')
#     sobrenome = request.args.get('sn', default='[sobrenome não informado]')
#     return nome+' '+sobrenome+'<br/><a href="/">Voltar</a>'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
