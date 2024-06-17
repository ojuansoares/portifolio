from flask import Flask, render_template

app = Flask("__name__")

projetos_academicos = [
    {
        'titulo': '2º API | Internet Ocean',
        'imagem_src': 'static/images/api2s.png',
        'descricao1': 'O projeto Internet Ocean tem o objetivo de realizar o gerenciamento de chamados de forma que aja maior otimização do processo de atendimento e suporte ao cliente, garantindo uma gestão eficiente das demandas.',
        'descricao2': 'Sendo o projeto desenvolvido em grupo, eu tive grande participação no desenvolvimento Frontend, criando as telas e fazendo a conexão com o Backend. Já no desenvolvimento Backend, somente desenvolvi algumas funcionalidades. Utilizamos as tecnologias: JavaScript, TypeScript, React, Node.JS, HTML & CSS, MySQL e Git.',
        'link_github': 'https://github.com/CoddingWarriors/Api_CoddingWarriors',
    },
    {
        'titulo': '1º API | Criança Renal',
        'imagem_src': 'static/images/api.png',
        'descricao1': 'O projeto Criança Renal consiste num site dedicado a mães que têm filhos com insuficiência renal crônica, visando fornecer informações e apoio relacionado à doença.',
        'descricao2': 'Tal projeto foi desenvolvido em grupo, do qual eu tive uma participação considerável. Fiz parte do desenvolvimento front-end e utilizamos as tecnologias: Python, HTML & CSS, Flask, MySQL e Git.',
        'link_github': 'https://github.com/Daiene/Pixels',
    },
]

projetos_pessoais = [
    {
        'titulo': 'Portfólio Pessoal',
        'imagem_src': 'static/images/pessoal.png',
        'descricao1': 'O Portfólio desenvolvido contém uma coleção de trabalhos, projetos e realizações da minha pessoa. Tem o intuito principal de destacar e apresentar de forma abrangente meu conjunto de habilidades, experiências e competências.',
        'descricao2': 'Foram utilizadas as Tecnologias: HTML & CSS, Python, Flask e Git.',
        'link_github': 'https://github.com/ojuansoares/portifolio_digital_dsm',
    },
    {
        'titulo': 'Curso de Violão',
        'imagem_src': 'static/images/cursoviolao.png',
        'descricao1': 'Este projeto foi feito com o intuito de compartilhar o curso de violão do meu pai. O site contém informações sobre o curso e o professor do mesmo, visualização do endereço pelo Google Maps e uma funcionalidade de enviar um e-mail automaticamente para o professor do curso através do próprio site.',
        'descricao2': 'Foram utilizadas as Tecnologias: HTML & CSS, Python, Flask e Git.',
        'link_github': 'https://github.com/ojuansoares/curso-violao',
    },
]

@app.route("/")
def hello_world():
    return render_template("portfolio.html", title = "Home - Portfólio")

@app.route("/projetos")
def quem():
    return render_template("projetos.html", title = "Projetos", projetos_academicos=projetos_academicos, projetos_pessoais=projetos_pessoais)

@app.route("/sobre_mim")
def sobre():
    return render_template("sobre_mim.html", title = "Sobre Mim")
