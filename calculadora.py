from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def calculadora():
    return '<html><head><title>Calculadora</title></head>' \
           '<body><form method="get" action="/somar">' \
           '<label for="num1">Primeiro Numero: </label><input type="number" name="n1" id="num1" value="0"/>' \
           '<br/>' \
           '<label for="num2">Segundo Numero: </label><input type="number" name="n2" id="num2" value="0"/>' \
           '<br/>' \
           '<br/>' \
           '<input type="submit" value="somar"/>' \
           '<input type="submit" value="subtrair" formaction="/subtrair"/>' \
           '<input type="submit" value="multiplicar" formaction="/multiplicar"/>' \
           '<input type="submit" value="dividir" formaction="/dividir"/>' \
           '</form>' \
           '</body></html>'



@app.route('/somar')
def somar():
    n1 = int(request.args.get('n1', default="0"))
    n2 = int(request.args.get('n2', default="0"))
    return str(n1 + n2) + '<br/><br/><a href="/"> Voltar</a>'

@app.route('/subtrair')
def sub():
    n1 = int(request.args.get('n1', default="0"))
    n2 = int(request.args.get('n2', default="0"))
    return str(n1 - n2) + '<br/><br/><a href="/"> Voltar</a>'

@app.route('/multiplicar')
def mult():
    n1 = int(request.args.get('n1', default="0"))
    n2 = int(request.args.get('n2', default="0"))
    return str(n1 * n2) + '<br/><br/><a href="/"> Voltar</a>'

@app.route('/dividir')
def div():
    n1 = int(request.args.get('n1', default="0"))
    n2 = int(request.args.get('n2', default="0"))
    if n2 == 0:
        return 'Não é possível dividir por "0" <br/><br/><a href="/"> Voltar</a>'
    return str(n1 / n2) + '<br/><br/><a href="/"> Voltar</a>'


if __name__ == '__main__':
    app.run(debug=True)