<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plataforma de Estudos - Black & Purple</title>
    <style>
        /* Estilos CSS (Versão Preto e Roxo) */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #1a1a2e;
            color: #e0e0e0;
            line-height: 1.6;
        }

        header {
            background-color: #0f0f1a;
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
            background-color: #2e0f4f;
            overflow: hidden;
            display: flex;
            justify-content: center;
            border-bottom: 2px solid #6a05ad;
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
            background-color: #6a05ad;
            color: #ffffff;
        }

        .container {
            max-width: 1000px;
            margin: 30px auto;
            padding: 0 20px;
        }

        .content-section {
            display: none;
            padding: 30px;
            background-color: #22223b;
            border: 1px solid #4a007f;
            border-radius: 12px;
            margin-top: 20px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
            animation: fadeIn 0.5s ease-in-out;
        }

        .content-section.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h2 {
            color: #be58f2;
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

        /* Estilos para o conteúdo de exemplo (Simulados) */
        .example-list {
            list-style: none;
            padding: 0;
            margin-top: 20px;
        }

        .example-list li {
            background-color: #311d4e;
            margin-bottom: 10px;
            padding: 15px 20px;
            border-radius: 8px;
            border-left: 5px solid #be58f2;
            transition: transform 0.2s ease, background-color 0.2s ease;
        }

        .example-list li:hover {
            transform: translateX(5px);
            background-color: #3e265c;
        }

        /* Estilo dos Botões (Simulado e YouTube) */
        .primary-button {
            display: block;
            width: 100%;
            text-align: center;
            padding: 20px;
            font-weight: bold;
            font-size: 1.2em;
            border-radius: 12px;
            text-decoration: none;
            margin-bottom: 20px;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }

        /* Estilo Específico para o Botão do Simulados */
        .simulado-button {
            background-color: #be58f2; /* Roxo brilhante */
            color: #0f0f1a; /* Texto escuro */
            box-shadow: 0 4px 10px rgba(190, 88, 242, 0.4);
        }
        
        .simulado-button:hover {
            background-color: #d175ff;
            transform: translateY(-2px);
        }

        /* Estilo Específico para o Botão do YouTube */
        .youtube-button {
            background-color: #ff0000; /* Vermelho do YouTube */
            color: #ffffff; /* Texto branco */
            box-shadow: 0 4px 10px rgba(255, 0, 0, 0.4);
            margin-top: 25px; /* Separar do vídeo */
        }

        .youtube-button:hover {
            background-color: #cc0000;
            transform: translateY(-2px);
        }

        /* Estilo para o vídeo responsivo */
        .video-wrapper {
            position: relative;
            padding-bottom: 56.25%; /* Proporção 16:9 */
            height: 0;
            overflow: hidden;
            max-width: 100%;
            background: #000;
            border-radius: 8px;
            margin-top: 20px;
        }

        .video-wrapper iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: 0;
        }

        /* ========================================= */
        /* NOVOS ESTILOS PARA O GERENCIADOR DE ARQUIVOS */
        /* ========================================= */
        #file-manager {
            background-color: #311d4e;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 25px;
            border: 1px dashed #be58f2;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        #file-manager h3 {
            color: #be58f2;
            margin-top: 0;
        }
        #file-manager input[type="file"] {
            padding: 10px;
            background-color: #0f0f1a;
            color: #ffffff;
            border: 1px solid #4a007f;
            border-radius: 5px;
            width: calc(100% - 22px);
            margin-bottom: 15px;
        }
        /* Estilo Específico para o NOVO Botão de Arquivo Dinâmico */
        .file-button {
            background-color: #008cba; /* Azul para Download/Arquivo */
            color: #ffffff;
            box-shadow: 0 4px 10px rgba(0, 140, 186, 0.4);
            margin-bottom: 15px; /* Adicionar margem para o botão */
            padding: 15px; /* Ajustar padding para harmonizar */
            font-size: 1em; /* Ajustar fonte */
        }
        .file-button:hover {
            background-color: #005f7a;
            transform: translateY(-2px);
        }
        .dynamic-content-area {
            margin-top: 20px;
            border-top: 2px solid #3e265c;
            padding-top: 20px;
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

        <div id="file-manager">
            <h3>🔗 Adicionar Arquivo e Criar Botão (FUNCIONALIDADE DINÂMICA)</h3>
            <p>Selecione um arquivo para criar um botão de acesso temporário na seção ativa (Simulados ou Videoaulas). **O arquivo só estará disponível enquanto a página estiver aberta.**</p>
            <input type="file" id="fileInput" accept="*/*">
            <button onclick="createFileAccessButton()" class="primary-button file-button" style="width: 100%; display: block; margin-top: 15px;">
                ➕ Adicionar Botão de Acesso ao Arquivo
            </button>
        </div>
        <section id="simulados" class="content-section active">
            <h2>🧠 Simulados Disponíveis</h2>
            
            <a href="simulado_vigilancia.html" target="_blank" class="primary-button simulado-button">
                🚨 Simulado: Vigilância e PNI (50 Questões)
            </a>
            
            <p>Outros simulados para testar seus conhecimentos:</p>
            <ul class="example-list">
                <li>Simulado de Matemática Avançada - 20 questões</li>
                <li>Simulado de Português - Interpretação de Texto</li>
                <li>Simulado Completo - ENEM (Todas as áreas)</li>
                <li>Simulado de Inglês - Gramática e Vocabulário</li>
            </ul>

            <div id="dynamic-simulados-buttons" class="dynamic-content-area">
                <h4>Botões de Arquivos Personalizados (Simulados)</h4>
            </div>
        </section>

        <section id="videoaulas" class="content-section">
            <h2>🎬 Videoaula em Destaque</h2>
            
            <p class="font-bold text-lg text-[#be58f2]">Aula: O Papel da Vigilância Sanitária na Saúde Pública</p>

            <div class="video-wrapper">
                <iframe 
                    width="560" 
                    height="315" 
                    src="https://www.youtube.com/embed/dQw4w9WgXcQ?si=c-V-m9eB-t6dO7-P" 
                    title="YouTube video player" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                    referrerpolicy="strict-origin-when-cross-origin" 
                    allowfullscreen>
                </iframe>
            </div>

            <a href="https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1" target="_blank" class="primary-button youtube-button">
                ▶️ ACESSE NOSSO CANAL COMPLETO NO YOUTUBE
            </a>

            <p class="mt-4 text-sm text-gray-400">Clique no player acima para começar a aula. Use o botão vermelho para acessar o canal com todas as videoaulas.</p>

            <div id="dynamic-videoaulas-buttons" class="dynamic-content-area">
                <h4>Botões de Arquivos Personalizados (Videoaulas)</h4>
            </div>
        </section>

    </div>

    <script>
        /**
         * Função para alternar entre as seções.
         * @param {string} sectionId - O ID da seção a ser exibida ('simulados' ou 'videoaulas').
         */
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

        /**
         * Função principal para criar o botão de acesso ao arquivo.
         */
        function createFileAccessButton() {
            const fileInput = document.getElementById('fileInput');
            const file = fileInput.files[0];

            if (!file) {
                alert('🚫 Por favor, selecione um arquivo primeiro no campo acima.');
                return;
            }

            // 1. Encontra a seção (Simulados ou Videoaulas) que está ativa no momento.
            const activeSection = document.querySelector('.content-section.active');
            if (!activeSection) {
                alert('Erro: Nenhuma seção ativa encontrada.');
                return;
            }

            // 2. Define a área correta para anexar o novo botão.
            const targetDivId = `dynamic-${activeSection.id}-buttons`;
            const targetDiv = document.getElementById(targetDivId);

            // 3. Cria um URL temporário para o arquivo selecionado.
            // Isso permite que o navegador baixe o arquivo *enquanto* a página estiver aberta.
            const fileURL = URL.createObjectURL(file);
            const fileName = file.name;

            // 4. Cria o novo elemento de botão (link <a>).
            const newButton = document.createElement('a');
            newButton.href = fileURL;
            newButton.target = '_blank';
            newButton.className = 'primary-button file-button'; // Aplica o novo estilo azul
            newButton.download = fileName; // Sugere o nome do arquivo ao baixar
            newButton.innerHTML = `⬇️ Baixar Arquivo: ${fileName}`;

            // 5. Adiciona o botão ao topo da área dinâmica da seção ativa.
            targetDiv.prepend(newButton);

            // Limpa o campo de arquivo para um novo upload
            fileInput.value = '';

            alert(`✅ Botão para "${fileName}" adicionado com sucesso na seção "${activeSection.id.toUpperCase()}"!`);
        }

        document.addEventListener('DOMContentLoaded', () => {
            const initialSection = window.location.hash ? window.location.hash.substring(1) : 'simulados';
            showSection(initialSection);
        });
    </script>

</body>
</html>
