from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # Necessário para sessions

def calcular_imc(peso, altura):
    """Função que calcula o IMC e retorna a classificação"""
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        classificacao = 'CUIDADO! Você está ABAIXO DO PESO ideal.'
        categoria = 'abaixo-peso'
    elif 18.5 <= imc < 25:
        classificacao = 'PARABÉNS! Você está no seu PESO IDEAL.'
        categoria = 'peso-ideal'
    elif 25 <= imc < 30:
        classificacao = 'CUIDADO! Você está em SOBREPESO.'
        categoria = 'sobrepeso'
    elif 30 <= imc < 40:
        classificacao = 'ALERTA! Você está em OBESIDADE.'
        categoria = 'obesidade'
    elif imc >= 40:
        classificacao = 'PERIGO! Você está em OBESIDADE MÓRBIDA.'
        categoria = 'obesidade-morbida'
    
    return imc, classificacao, categoria

@app.route('/', methods=['GET'])
def index():
    # Pegar dados da session se existirem
    imc = session.get('imc')
    classificacao = session.get('classificacao')
    categoria = session.get('categoria')
    peso = session.get('peso')
    altura = session.get('altura')
    erro = session.get('erro')
    
    # Limpar session após usar os dados
    session.clear()
    
    return render_template('index.html', 
                         imc=imc, 
                         classificacao=classificacao,
                         categoria=categoria,
                         peso=peso,
                         altura=altura,
                         erro=erro)

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        
        if peso <= 0 or altura <= 0:
            session['erro'] = "Por favor, insira valores válidos para peso e altura."
            return redirect(url_for('index'))
        
        imc, classificacao, categoria = calcular_imc(peso, altura)
        
        # Salvar resultados na session
        session['imc'] = round(imc, 1)
        session['classificacao'] = classificacao
        session['categoria'] = categoria
        session['peso'] = peso
        session['altura'] = altura
        
        return redirect(url_for('index'))
    
    except ValueError:
        session['erro'] = "Por favor, insira números válidos."
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)