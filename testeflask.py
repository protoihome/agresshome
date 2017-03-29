from flask import Flask, render_template, request
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    templateData = {'sandro':12, 'Judison': 'Godinho'}
    return render_template('info.html', **templateData)

@app.route('/comodos',  methods=['POST', 'GET'])
def comodo():

    if request.method == 'POST':
        #aparelho = request.form['id_ap']
        acao = request.form['acao']
        print acao
    templateData = {'acao': acao, 'Judison': 'Godinho'}
    return render_template('testeform.html', **templateData)

@app.route('/codigo')
def hello_world2():
    return 'Hello World 2!'

@app.route('/_get_current_user')
def get_current_user():
    return jsonify(username='judison1',
                   email='teste@teste.com',
                   id=1)

@app.route('/get_dispositivos')
def get_dispositivos():
    return jsonify(comodo="sala",aparelhos=[dict(nome='teste',status=1,id=1),  dict(nome='teste2',status=0,id=2)])

if __name__ == '__main__':
    app.run()
    #app.run(host='10.42.0.1', port=8080, debug=True)