from flask import Flask, render_template # type: ignore

app = Flask("__name__")

projetos_academicos = [
    {
        'semestre-titulo': '2023-2',
        'titulo': '1º API | Rim do Amor',
        'imagem_src': 'static/images/api.png',
        'semestre': 'Participei no projeto chamado Rim do Amor juntamente com minha equipe da faculdade. O objetivo era criar um site dedicado a mães com filhos diagnosticados com insuficiência renal crônica, fornecendo informações e suporte relacionados à doença. Durante esse semestre, utilizamos Python Flask para o backend e HTML & CSS para o frontend, aplicando boas práticas de desenvolvimento para entregar uma solução funcional e acessível.',
        'tecnologias': 'Plataforma de Interação, Analytics',
        'contribuicoes': 'Dentro do projeto, minha maior contribuição foi no desenvolvimento do frontend, criando interfaces acessíveis e conectando-as ao backend. Trabalhar com minha equipe proporcionou um ambiente colaborativo, mas com desafios que ajudaram no meu aprendizado. Hoje, essa experiência me incentiva a aprimorar habilidades como agilidade e proatividade em projetos futuros.',
        'hard': 'Python, Flask, HTML, CSS, MySQL, Git',
        'soft': 'Proatividade e Comunicação. Além disso, desenvolvi habilidades como trabalho em equipe e organização para cumprir os prazos e garantir uma entrega eficiente.',
        'link_github': 'https://github.com/Daiene/Pixels',
    },
    {
        'semestre-titulo': '2024-1',
        'titulo': '2º API | Internet Ocean',
        'imagem_src': 'static/images/api2s.png',
        'semestre': 'Participei no projeto da API chamado Internet Ocean juntamente com minha equipe da faculdade. Nesse projeto, o objetivo era realizar o gerenciamente de chaamdos de forma otimizada, para gestão de demandas no atendimento ao cliente. Durante esse semestre, exploramos como a utilização de frameworks Front-end modernos, como Bootstrap, aliados às boas práticas de orientação a objetos, poderiam otimizar a experiência do usuário e a eficiência operacional. A integração eficiente das tecnologias envolvidas provou ser essencial para atender às demandas do mercado atual.',
        'tecnologias': 'Plataforma de Interaçãos, Analytics',
        'contribuicoes': 'Dentro do projeto, minha maior contribuição foi na criação e estruturação do Frontend, desenvolvendo interfaces intuitivas e garantindo a integração funcional com o Backend. Dentro do grupo, tivemos uma relação amigável e as tarefas eram feitas de forma rápida. Não era uma equipe ágil, entretanto, serviu de aprendizado para meu crescimento hoje em dia, para melhorar em proatividade e agilidade nos projetos.',
        'hard': 'Typescript, Javascript, Bootstrap, Node.js, React, Git.',
        'soft': 'Proatividade e Autonomia. Ainda assim, aprimorei minhas habilidades de trabalho em equipe e gerenciamento de tempo para cumprir os prazos do projeto.',
        'link_github': 'https://github.com/CoddingWarriors/Api_CoddingWarriors',
    },
    {
        'semestre-titulo': '2024-2',
        'titulo': '3º API | Portal Transparencia FAPG',
        'imagem_src': 'static/images/api3s.png',
        'semestre': 'Participei do projeto da API Portal da Transparência FAPG, desenvolvido com minha equipe na faculdade. O objetivo foi facilitar a gestão e consulta de informações sobre projetos da fundação, promovendo transparência e acessibilidade. O sistema incluiu funcionalidades como cadastro e edição de projetos, filtros avançados por data, controle administrativo e módulos para gerenciamento de administradores, bolsistas, convênios e materiais. Durante o projeto, enfrentamos problemas com a formação dos grupos, exigindo mudanças drásticas nos membros, o que me forçou a melhorar minha interação em equipe e, consequentemente, minha entrega de resultados.',
        'tecnologias': 'Plataforma de Interação, Analytics',
        'contribuicoes': 'Contribuí de forma significativa no backend, implementando filtros, histórico do sistema e atendendo demandas críticas, além de corrigir aspectos do frontend. Fui mais proativo, ágil e eficiente em relação a projetos anteriores.',
        'hard': 'Java, TypeScript, JavaScript, MySQL, Tailwind, Bootstrap, Spring Boot',
        'soft': 'Proatividade, Agilidade, Colaboração e Entrega de Resultado. Esse projeto foi fundamental para consolidar minha capacidade de entrega, mentalidade profissional e colaboração em equipe.',
        'link_github': 'https://github.com/A-Sync-Fatec/api-fatec-3sem-24',
    },
    {
        'semestre-titulo': '2025-2',
        'titulo': '5º API | Aplicativo militar de controle logístico setorial de ativos',
        'imagem_src': 'static/images/militar_app.png',
        'semestre': 'Participei do projeto da 5ª API, cujo objetivo foi desenvolver um aplicativo mobile para gestão do almoxarifado militar. O desafio central era substituir um processo burocrático, manual e sujeito a erros por uma solução moderna, rápida e segura. O sistema deveria permitir o cadastro de materiais, atualização de estoque, leitura via QR Code e uma interface simples e responsiva, acessível tanto em smartphones quanto em tablets. Esse projeto ampliou minha visão sobre boas práticas de desenvolvimento mobile e organização de processos logísticos.',
        'tecnologias': 'Plataforma de Interação, Analytics',
        'contribuicoes': 'Minhas principais contribuições foram no desenvolvimento de funcionalidades essenciais, como o envio automático de e-mails, o registro de pedidos com múltiplos itens do estoque e a integração das operações de cadastro e movimentação dos materiais. Também participei na construção de telas e lógica interna que garantem uma experiência fluida e organizada para o usuário final.',
        'hard': 'Flutter, Supabase, Node.js, Python, Figma, Trello',
        'soft': 'Proatividade, Comunicação, Colaboração, Organização.',
        'link_github': 'https://github.com/TeamHiveAPI/API-2025.02',
    }
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
    }
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
