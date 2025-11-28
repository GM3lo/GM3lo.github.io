<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plataforma de Estudos - Black & Purple</title>
    <style>
        /* Estilos CSS */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #1a1a2e; /* Fundo principal escuro */
            color: #e0e0e0; /* Cor do texto padrão mais clara */
            line-height: 1.6;
        }

        header {
            background-color: #0f0f1a; /* Roxo escuro para o cabeçalho */
            color: #ffffff;
            padding: 25px 20px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }

        header h1 {
            margin: 0;
            font-size: 2.5em;
            letter-spacing: 1px;
        }

        nav {
            background-color: #2e0f4f; /* Roxo mais vibrante para a navegação */
            overflow: hidden;
            display: flex;
            justify-content: center;
            border-bottom: 2px solid #6a05ad; /* Linha roxa na parte inferior da nav */
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        }

        nav a {
            display: block;
            color: #ffffff;
            text-align: center;
            padding: 16px 25px;
            text-decoration: none;
            transition: background-color 0.3s ease, color 0.3s ease;
            font-weight: bold;
            letter-spacing: 0.5px;
        }

        nav a:hover,
        nav a.active-nav {
            background-color: #6a05ad; /* Roxo mais claro ao passar o mouse ou ativo */
            color: #ffffff;
        }

        .container {
            max-width: 1000px;
            margin: 30px auto;
            padding: 0 20px;
        }

        .content-section {
            display: none; /* Inicialmente oculta todas as seções */
            padding: 30px;
            background-color: #22223b; /* Fundo da seção um pouco mais claro que o body */
            border: 1px solid #4a007f; /* Borda roxa escura */
            border-radius: 12px;
            margin-top: 20px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
            animation: fadeIn 0.5s ease-in-out;
        }

        .content-section.active {
            display: block; /* Mostra a seção ativa */
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h2 {
            color: #be58f2; /* Roxo claro para os títulos das seções */
            border-bottom: 2px solid #be58f2;
            padding-bottom: 10px;
            margin-bottom: 25px;
            font-size: 2em;
            letter-spacing: 0.8px;
        }

        p {
            margin-bottom: 15px;
            color: #c0c0d0;
        }

        /* Estilos para o conteúdo de exemplo */
        .example-list {
            list-style: none; /* Remove marcadores de lista padrão */
            padding: 0;
            margin-top: 20px;
        }

        .example-list li {
            background-color: #311d4e; /* Fundo roxo para itens da lista */
            margin-bottom: 10px;
            padding: 15px 20px;
            border-radius: 8px;
            border-left: 5px solid #be58f2; /* Borda esquerda roxa clara */
            transition: transform 0.2s ease, background-color 0.2s ease;
        }

        .example-list li:hover {
            transform: translateX(5px);
            background-color: #3e265c; /* Ligeiramente mais claro ao passar o mouse */
        }

        /* Estilo do Botão do Novo Simulado (Diferente da lista) */
        .simulado-button {
            display: block;
            width: 100%;
            text-align: center;
            padding: 20px;
            background-color: #be58f2; /* Roxo brilhante */
            color: #0f0f1a; /* Texto escuro */
            font-weight: bold;
            font-size: 1.2em;
            border-radius: 12px;
            text-decoration: none;
            margin-bottom: 20px;
            box-shadow: 0 4px 10px rgba(190, 88, 242, 0.4);
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        
        .simulado-button:hover {
            background-color: #d175ff; /* Roxo mais claro no hover */
            transform: translateY(-2px);
        }
    </style>
</head>
<body>

    <header>
        <h1>📚 Minha Plataforma de Estudos</h1>
    </header>

    <nav>
        <a href="#simulados" id="nav-simulados" onclick="showSection('simulados')">Simulados</a>
        <a href="#videoaulas" id="nav-videoaulas" onclick="showSection('videoaulas')">Videoaulas</a>
    </nav>

    <div class="container">
        
        <section id="simulados" class="content-section active">
            <h2>🧠 Simulados Disponíveis</h2>
            
            <a href="simulado_vigilancia.html" target="_blank" class="simulado-button">
                🚨 Simulado: Vigilância e PNI (50 Questões)
            </a>
            
            <p>Outros simulados para testar seus conhecimentos:</p>
            <ul class="example-list">
                <li>Simulado de Matemática Avançada - 20 questões</li>
                <li>Simulado de Português - Interpretação de Texto</li>
                <li>Simulado Completo - ENEM (Todas as áreas)</li>
                <li>Simulado de Inglês - Gramática e Vocabulário</li>
            </ul>
        </section>

        <section id="videoaulas" class="content-section">
            <h2>🎬 Videoaulas</h2>
            <p>Assista às aulas preparadas pelos nossos professores especialistas.</p>
            <ul class="example-list">
                <li>Aula 1: Introdução à Física Quântica</li>
                <li>Aula 2: Revisão de História do Brasil Colonial</li>
                <li>Aula 3: Dicas de Redação para Vestibulares</li>
                <li>Aula 4: Fundamentos da Programação em Python</li>
            </ul>
            <p>Encontre o seu tema e comece a estudar!</p>
        </section>

    </div>

    <script>
        function showSection(sectionId) {
            document.querySelectorAll('.content-section').forEach(section => {
                section.classList.remove('active');
            });
            document.getElementById(sectionId).classList.add('active');

            document.querySelectorAll('nav a').forEach(link => {
                link.classList.remove('active-nav');
            });
            document.getElementById(`nav-${sectionId}`).classList.add('active-nav');
        }

        document.addEventListener('DOMContentLoaded', () => {
            const initialSection = window.location.hash ? window.location.hash.substring(1) : 'simulados';
            showSection(initialSection);
        });
    </script>

</body>
</html>
