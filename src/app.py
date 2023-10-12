from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def hello_world():
    return render_template("portfolio.html", title = "Home - Portfólio")

@app.route("/projetos")
def quem():
    return render_template("projetos.html", title = "Projetos")

@app.route("/sobre_mim")
def sobre():
    return render_template("sobre_mim.html", title = "Sobre Mim")