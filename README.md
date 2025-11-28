
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plataforma de Estudos</title>
    <style>
        /* Estilos CSS */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
        }

        header {
            background-color: #007bff;
            color: white;
            padding: 20px;
            text-align: center;
        }

        nav {
            background-color: #333;
            overflow: hidden;
            display: flex;
            justify-content: center;
        }

        nav a {
            float: left;
            display: block;
            color: white;
            text-align: center;
            padding: 14px 20px;
            text-decoration: none;
            transition: background-color 0.3s;
        }

        nav a:hover {
            background-color: #575757;
        }

        .container {
            padding: 20px;
        }

        .content-section {
            display: none; /* Inicialmente oculta todas as seções */
            padding: 20px;
            border: 1px solid #ccc;
            margin-top: 10px;
            background-color: white;
            border-radius: 8px;
        }

        .content-section.active {
            display: block; /* Mostra a seção ativa */
        }

        h2 {
            color: #007bff;
            border-bottom: 2px solid #007bff;
            padding-bottom: 5px;
            margin-bottom: 15px;
        }

        /* Estilos para o conteúdo de exemplo */
        .example-list li {
            padding: 8px 0;
            border-bottom: 1px dashed #eee;
        }
    </style>
</head>
<body>

    <header>
        <h1>📚 Minha Plataforma de Estudos</h1>
    </header>

    <nav>
        <a href="#simulados" onclick="showSection('simulados')">Simulados</a>
        <a href="#videoaulas" onclick="showSection('videoaulas')">Videoaulas</a>
    </nav>

    <div class="container">
        
        <section id="simulados" class="content-section active">
            <h2>🧠 Simulados</h2>
            <p>Escolha um simulado para testar seus conhecimentos e medir seu progresso.</p>
            <ul class="example-list">
                <li>Simulado de Matemática Avançada - 20 questões</li>
                <li>Simulado de Português - Interpretação de Texto</li>
                <li>Simulado Completo - ENEM (Todas as áreas)</li>
            </ul>
            <p>Clique em um simulado para começar!</p>
        </section>

        <section id="videoaulas" class="content-section">
            <h2>🎬 Videoaulas</h2>
            <p>Assista às aulas preparadas pelos nossos professores especialistas.</p>
            <ul class="example-list">
                <li>Aula 1: Introdução à Física Quântica</li>
                <li>Aula 2: Revisão de História do Brasil Colonial</li>
                <li>Aula 3: Dicas de Redação para Vestibulares</li>
            </ul>
            <p>Encontre o seu tema e comece a estudar!</p>
        </section>

    </div>

    <script>
        // Função para mostrar a seção selecionada e ocultar as outras
        function showSection(sectionId) {
            // Remove a classe 'active' de todas as seções
            document.querySelectorAll('.content-section').forEach(section => {
                section.classList.remove('active');
            });

            // Adiciona a classe 'active' à seção clicada
            document.getElementById(sectionId).classList.add('active');
        }

        // Garante que o simulados seja a aba inicial ao carregar a página (se não houver um hash)
        document.addEventListener('DOMContentLoaded', () => {
            if (!window.location.hash) {
                showSection('simulados');
            }
        });
    </script>

</body>
</html>
