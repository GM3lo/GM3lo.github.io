<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simulado: Infecções Virais e PNI</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        body { font-family: 'Inter', sans-serif; }
        .option-label { transition: all 0.2s; }
        .option-radio:checked + .option-label {
            background-color: #eff6ff;
            border-color: #3b82f6;
            color: #1e40af;
        }
        .correct-answer { background-color: #dcfce7 !important; border-color: #22c55e !important; color: #14532d !important; }
        .wrong-answer { background-color: #fee2e2 !important; border-color: #ef4444 !important; color: #7f1d1d !important; }
        /* Animação suave */
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        .animate-fade-in { animation: fadeIn 0.3s ease-out forwards; }
    </style>
</head>
<body class="bg-gray-50 text-gray-800 min-h-screen pb-20">

    <!-- Header Fixo -->
    <header class="bg-blue-900 text-white shadow-lg sticky top-0 z-50">
        <div class="max-w-4xl mx-auto px-4 py-3 flex justify-between items-center">
            <div>
                <h1 class="text-lg font-bold">Simulado: Infecções Virais</h1>
                <p class="text-xs text-blue-200">Baseado no material TBL31NCS2</p>
            </div>
            <div class="text-right">
                <div id="timer" class="text-xl font-mono font-bold text-yellow-400">00:00</div>
                <div class="text-xs text-blue-200">Tempo decorrido</div>
            </div>
        </div>
    </header>

    <!-- Container Principal -->
    <main class="max-w-4xl mx-auto px-4 py-8">
        
        <!-- Instruções -->
        <div class="bg-white rounded-lg shadow-sm p-6 mb-8 border-l-4 border-blue-500">
            <h2 class="text-xl font-bold mb-2 text-gray-900">Instruções</h2>
            <ul class="list-disc list-inside text-sm text-gray-600 space-y-1">
                <li>Este simulado contém <strong>50 questões</strong> de múltipla escolha.</li>
                <li>O conteúdo abrange PNI, vacinas, vigilância epidemiológica e virologia.</li>
                <li>Ao finalizar, clique no botão no final da página para ver sua nota e as explicações.</li>
            </ul>
        </div>

        <!-- Área das Questões -->
        <form id="quiz-form" class="space-y-6">
            <!-- As questões serão injetadas aqui via JavaScript -->
            <div class="text-center text-gray-500 py-10">Carregando questões...</div>
        </form>

        <!-- Botão Finalizar -->
        <div class="mt-10 mb-20 text-center">
            <button type="button" onclick="submitQuiz()" class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-4 px-10 rounded-full shadow-lg transform transition hover:scale-105 text-lg">
                Finalizar e Corrigir Simulado
            </button>
        </div>

    </main>

    <!-- Modal de Resultado -->
    <div id="result-modal" class="fixed inset-0 bg-black bg-opacity-50 hidden items-center justify-center z-50 px-4 backdrop-blur-sm transition-opacity">
        <div class="bg-white rounded-xl shadow-2xl max-w-md w-full p-6 transform transition-all scale-100 border border-gray-200">
            <div class="text-center">
                <div id="icon-container" class="mx-auto flex items-center justify-center h-16 w-16 rounded-full bg-blue-100 mb-4 transition-colors">
                    <svg class="h-8 w-8 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                </div>
                <h3 class="text-2xl font-bold text-gray-900 mb-2">Resultado Final</h3>
                <div class="text-5xl font-bold text-blue-600 mb-2" id="score-display">0%</div>
                <p class="text-gray-500 mb-6" id="score-detail">Você acertou 0 de 50 questões.</p>
                <div class="flex gap-3 justify-center">
                    <button onclick="closeModal()" class="w-full bg-gray-100 hover:bg-gray-200 text-gray-800 font-semibold py-3 px-4 rounded-lg transition-colors">
                        Revisar Erros
                    </button>
                    <button onclick="location.reload()" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-4 rounded-lg transition-colors shadow-md">
                        Reiniciar
                    </button>
                </div>
            </div>
        </div>
    </div>

    <script>
        // --- BANCO DE DADOS DAS QUESTÕES ---
        const questionsData = [
            {
                id: 1,
                question: "O Programa Nacional de Imunizações (PNI) do Brasil, criado em 1973, é reconhecido mundialmente por sua abrangência. Sobre sua estrutura e objetivos, assinale a alternativa correta:",
                options: {
                    A: "Sua coordenação é descentralizada, sendo de responsabilidade exclusiva dos municípios a definição do calendário vacinal.",
                    B: "Tem como único propósito a erradicação de doenças virais, não atuando no controle de infecções bacterianas.",
                    C: "É coordenado nacionalmente pelo Ministério da Saúde e visa controlar, eliminar e erradicar doenças imunopreveníveis.",
                    D: "Utiliza apenas vacinas produzidas em território nacional, proibindo a importação de imunobiológicos."
                },
                correct: "C",
                explanation: "O PNI tem coordenação nacional pelo Ministério da Saúde e gestão compartilhada. Seu objetivo abrange o controle, eliminação e erradicação de doenças imunopreveníveis (bacterianas e virais)."
            },
            {
                id: 2,
                question: "A diferenciação entre os conceitos de 'vacinação' e 'imunização' é fundamental na prática clínica. Qual das opções abaixo define corretamente essa distinção?",
                options: {
                    A: "Vacinação é o ato de administrar o imunobiológico, enquanto imunização é a aquisição da proteção imunológica.",
                    B: "Vacinação refere-se à proteção passiva, e imunização refere-se à proteção ativa natural.",
                    C: "Os termos são estritamente sinônimos e podem ser usados de forma intercambiável em documentos técnicos.",
                    D: "Imunização é o procedimento físico da injeção, enquanto vacinação é a resposta celular do organismo."
                },
                correct: "A",
                explanation: "Vacinação é o procedimento técnico (o ato). Imunização é o efeito biológico (a proteção adquirida). Nem toda vacinação resulta em imunização (falha vacinal)."
            },
            {
                id: 3,
                question: "Sobre os indicadores epidemiológicos utilizados para monitorar a saúde das populações, a 'letalidade' é definida como:",
                options: {
                    A: "O número total de óbitos em uma população dividido pelo número total de habitantes.",
                    B: "A proporção de mortes ocorridas especificamente entre os casos diagnosticados de uma doença.",
                    C: "O número de novos casos de uma doença registrados em um determinado período de tempo.",
                    D: "A quantidade total de casos existentes (novos e antigos) em um ponto específico do tempo."
                },
                correct: "B",
                explanation: "Letalidade mede a gravidade de uma doença: é o número de óbitos dividido pelo número de doentes (casos)."
            },
            {
                id: 4,
                question: "A vacina Tríplice Viral, disponível no SUS, confere proteção contra quais doenças infecciosas?",
                options: {
                    A: "Sarampo, Caxumba e Rubéola.",
                    B: "Sarampo, Catapora e Tétano.",
                    C: "Dengue, Zika e Chikungunya.",
                    D: "Hepatite A, Hepatite B e Hepatite C."
                },
                correct: "A",
                explanation: "A Tríplice Viral (SRC) protege contra Sarampo, Rubéola e Caxumba."
            },
            {
                id: 5,
                question: "As vacinas atenuadas (vivas) são caracterizadas por conterem patógenos enfraquecidos. Uma contraindicação importante e comum para esse tipo de vacina é:",
                options: {
                    A: "Administração em crianças maiores de 2 anos.",
                    B: "Uso em indivíduos imunocompetentes.",
                    C: "Aplicação simultânea com outras vacinas inativadas.",
                    D: "Administração em pacientes gravemente imunocomprometidos ou gestantes."
                },
                correct: "D",
                explanation: "Vacinas vivas atenuadas podem causar doença vacinal em indivíduos com sistema imune debilitado ou atravessar a placenta e afetar o feto em gestantes."
            },
            {
                id: 6,
                question: "No contexto da vigilância epidemiológica, o indicador que mede o 'número de novos casos em um período' é denominado:",
                options: {
                    A: "Prevalência.",
                    B: "Incidência.",
                    C: "Cobertura vacinal.",
                    D: "Virulência."
                },
                correct: "B",
                explanation: "Incidência refere-se aos casos novos, dando ideia de risco e velocidade de propagação. Prevalência refere-se ao total de casos (novos + antigos)."
            },
            {
                id: 7,
                question: "O Vírus da Imunodeficiência Humana (HIV) apresenta grandes desafios para o desenvolvimento de uma vacina eficaz. A principal razão biológica para essa dificuldade é:",
                options: {
                    A: "A baixa patogenicidade do vírus, que não estimula o sistema imune.",
                    B: "A alta variabilidade genética do vírus e a dificuldade em identificar antígenos imunogênicos estáveis.",
                    C: "A inexistência de modelos animais para testes de vacinas retrovirais.",
                    D: "A capacidade do vírus de sobreviver fora do corpo humano por longos períodos."
                },
                correct: "B",
                explanation: "O HIV tem altíssima taxa de mutação e variabilidade genética, o que dificulta criar uma vacina que cubra todas as variantes e gere anticorpos neutralizantes eficazes."
            },
            {
                id: 8,
                question: "Sobre a vacinação contra a Hepatite B, é correto afirmar que:",
                options: {
                    A: "A vacina é composta por vírus vivo atenuado e deve ser evitada em recém-nascidos.",
                    B: "A primeira dose deve ser administrada preferencialmente nas primeiras 24 horas após o nascimento.",
                    C: "A proteção completa só é adquirida após a infecção natural pelo vírus.",
                    D: "É indicada apenas para profissionais de saúde e profissionais do sexo."
                },
                correct: "B",
                explanation: "A dose ao nascer (preferencialmente nas primeiras 12-24h) é crucial para prevenir a transmissão vertical (mãe para filho) da Hepatite B."
            },
            {
                id: 9,
                question: "A vacina contra o HPV (Papilomavírus Humano) oferecida pelo SUS é a quadrivalente. Ela protege contra quais tipos virais?",
                options: {
                    A: "Tipos 6 e 11 (câncer) e tipos 16 e 18 (verrugas).",
                    B: "Tipos 6, 11, 16 e 18, protegendo contra verrugas genitais e lesões precursoras de câncer.",
                    C: "Apenas contra os tipos 16 e 18, responsáveis pela maioria dos casos de câncer de colo do útero.",
                    D: "Tipos 31, 33, 45 e 52, que são os mais prevalentes na população brasileira."
                },
                correct: "B",
                explanation: "A vacina quadrivalente cobre os tipos 6 e 11 (baixo risco oncogênico, causam verrugas) e 16 e 18 (alto risco oncogênico, causam câncer)."
            },
            {
                id: 10,
                question: "Qual é a função da 'cobertura vacinal' como indicador epidemiológico?",
                options: {
                    A: "Determinar a gravidade clínica dos casos de uma doença em vacinados.",
                    B: "Calcular o custo financeiro das campanhas de vacinação.",
                    C: "Avaliar o percentual da população-alvo que efetivamente recebeu a vacina.",
                    D: "Medir a quantidade de anticorpos produzidos por um indivíduo vacinado."
                },
                correct: "C",
                explanation: "Cobertura vacinal é a porcentagem da população-alvo que foi vacinada. É essencial para estimar a proteção coletiva."
            },
            {
                id: 11,
                question: "As vacinas de RNA mensageiro (mRNA), como algumas desenvolvidas para COVID-19, funcionam através de qual mecanismo?",
                options: {
                    A: "Introdução de um vírus inativado inteiro no organismo.",
                    B: "Uso de uma proteína pronta do vírus cultivada em laboratório.",
                    C: "Introdução de sequências de RNA que ensinam as células a produzir uma proteína viral específica.",
                    D: "Modificação do DNA do paciente para criar resistência permanente."
                },
                correct: "C",
                explanation: "As vacinas de mRNA entregam instruções genéticas para que as próprias células do corpo produzam a proteína viral (antígeno), desencadeando a resposta imune."
            },
            {
                id: 12,
                question: "A vacinação anual contra a Influenza é necessária principalmente porque:",
                options: {
                    A: "A vacina induz imunidade de curtíssima duração, de apenas 2 meses.",
                    B: "O vírus Influenza sofre frequentes mutações (drift antigênico), exigindo atualização das cepas vacinais.",
                    C: "A vacina anterior causa dependência imunológica, exigindo novas doses.",
                    D: "É uma estratégia comercial para manter a produção dos laboratórios."
                },
                correct: "B",
                explanation: "O vírus da gripe sofre pequenas mutações constantes (antigenic drift). A OMS atualiza a composição da vacina anualmente para combater as cepas mais circulantes."
            },
            {
                id: 13,
                question: "A vacina Qdenga, recentemente incorporada para o controle da Dengue, é classificada como:",
                options: {
                    A: "Vacina inativada monovalente.",
                    B: "Vacina de subunidade proteica.",
                    C: "Vacina atenuada tetravalente (protege contra os 4 sorotipos).",
                    D: "Vacina de vetor viral não replicante."
                },
                correct: "C",
                explanation: "A Qdenga é uma vacina de vírus vivo atenuado que protege contra os quatro sorotipos do vírus da dengue (DENV-1, 2, 3 e 4)."
            },
            {
                id: 14,
                question: "Qual das alternativas abaixo descreve corretamente a 'imunidade de rebanho'?",
                options: {
                    A: "Proteção individual adquirida exclusivamente através de soros hiperimunes.",
                    B: "Resistência natural de animais de pecuária a vírus humanos.",
                    C: "Fenômeno onde a alta cobertura vacinal de uma população protege indiretamente os indivíduos não vacinados.",
                    D: "Imunidade transmitida geneticamente de pais para filhos."
                },
                correct: "C",
                explanation: "Quando muitas pessoas estão imunes (vacinadas), o vírus não consegue circular, protegendo indiretamente aqueles que não podem se vacinar."
            },
            {
                id: 15,
                question: "A vacina contra a Hepatite A está indicada no calendário infantil do SUS. Qual é o esquema padrão para crianças?",
                options: {
                    A: "Dose única aos 15 meses de idade.",
                    B: "Três doses: ao nascer, 2 e 6 meses.",
                    C: "Dose anual até os 5 anos de vida.",
                    D: "Apenas em situações de surto ou viagem para áreas de risco."
                },
                correct: "A",
                explanation: "No Calendário Nacional de Vacinação do Brasil, a vacina contra Hepatite A é administrada em dose única aos 15 meses."
            },
            {
                id: 16,
                question: "O sarampo é uma doença viral altamente contagiosa. Um dos sinais clínicos característicos que, associado à febre alta, sugere o diagnóstico é:",
                options: {
                    A: "Icterícia (pele amarelada).",
                    B: "Exantema (manchas vermelhas no corpo).",
                    C: "Rigidez de nuca intensa.",
                    D: "Sangramento gengival espontâneo."
                },
                correct: "B",
                explanation: "O exantema maculopapular (manchas vermelhas) que começa na face e desce para o corpo é clássico do sarampo."
            },
            {
                id: 17,
                question: "Vacinas conjugadas são desenvolvidas para aumentar a resposta imunológica contra bactérias capsuladas. Elas consistem na ligação de:",
                options: {
                    A: "Dois vírus vivos diferentes na mesma ampola.",
                    B: "Um polissacarídeo bacteriano a uma proteína carreadora.",
                    C: "Um toxóide a um vírus inativado.",
                    D: "DNA viral a uma enzima humana."
                },
                correct: "B",
                explanation: "A conjugação liga um polissacarídeo (antígeno fraco em crianças) a uma proteína (carreadora), tornando a resposta imune mais robusta e duradoura (T-dependente)."
            },
            {
                id: 18,
                question: "Sobre a Poliomielite e suas vacinas (VIP e VOP), assinale a correta:",
                options: {
                    A: "A VIP (Vacina Inativada Poliomielite) é administrada por via oral (gotinha).",
                    B: "A VOP (Vacina Oral Poliomielite) é composta por vírus inativados e não causa pólio vacinal.",
                    C: "A VIP é composta por vírus inativados e é a preferida para as primeiras doses do esquema.",
                    D: "O Brasil utiliza exclusivamente a VOP em todas as doses do calendário atual."
                },
                correct: "C",
                explanation: "A VIP é inativada (injetável) e segura, usada nas primeiras doses (2, 4 e 6 meses) para evitar o risco (raríssimo) de pólio vacinal associado à VOP."
            },
            {
                id: 19,
                question: "A Vigilância em Saúde tem como um de seus pilares a Vigilância Epidemiológica, que visa:",
                options: {
                    A: "Apenas o tratamento clínico individual dos pacientes doentes.",
                    B: "A fiscalização sanitária de estabelecimentos comerciais de alimentos.",
                    C: "A coleta e análise de dados para orientar medidas de prevenção e controle de doenças.",
                    D: "A produção industrial de medicamentos e vacinas pelo Estado."
                },
                correct: "C",
                explanation: "A função da Vigilância Epidemiológica é gerar informação para a ação: coletar dados, analisar e propor medidas de controle."
            },
            {
                id: 20,
                question: "A imunidade passiva difere da imunidade ativa (vacinação) pois:",
                options: {
                    A: "Confere proteção duradoura e gera memória imunológica.",
                    B: "Envolve a administração de anticorpos prontos (soros ou imunoglobulinas) e tem proteção temporária.",
                    C: "Estimula o próprio corpo a produzir seus anticorpos.",
                    D: "É utilizada apenas preventivamente, nunca como tratamento pós-exposição."
                },
                correct: "B",
                explanation: "Imunidade passiva é a transferência de anticorpos prontos. É rápida, mas não gera memória imunológica, sendo temporária."
            },
            {
                id: 21,
                question: "Qual o agente etiológico da Hepatite B e sua classificação viral?",
                options: {
                    A: "Vírus HAV, um vírus de RNA.",
                    B: "Vírus HBV, um vírus de DNA (Hepadnaviridae).",
                    C: "Vírus HCV, um flavivírus.",
                    D: "Vírus HEV, um vírus entérico."
                },
                correct: "B",
                explanation: "O agente da Hepatite B é o HBV, um vírus de DNA pertencente à família Hepadnaviridae."
            },
            {
                id: 22,
                question: "Em relação à vacina contra Febre Amarela, ela é classificada como:",
                options: {
                    A: "Inativada, necessitando de reforços anuais.",
                    B: "Atenuada, sendo altamente eficaz e aplicada a partir dos 9 meses em áreas recomendadas.",
                    C: "Recombinante, produzida em fungos.",
                    D: "Toxóide, derivada da toxina do mosquito vetor."
                },
                correct: "B",
                explanation: "A vacina da Febre Amarela utiliza vírus vivo atenuado (cepa 17D) e é uma das mais eficazes existentes."
            },
            {
                id: 23,
                question: "As vacinas de 'vetor viral' (ex: AstraZeneca para COVID-19) utilizam:",
                options: {
                    A: "Um vírus diferente e inofensivo modificado para transportar genes do patógeno alvo.",
                    B: "O próprio vírus causador da doença, apenas morto por calor.",
                    C: "Partículas de lipídios contendo proteínas virais purificadas.",
                    D: "Anticorpos de cavalo modificados geneticamente."
                },
                correct: "A",
                explanation: "Vacinas vetoriais usam um vírus (como o adenovírus) modificado para não causar doença, servindo apenas como transporte para o material genético do alvo."
            },
            {
                id: 24,
                question: "O conceito de 'vacina de subunidade' refere-se a imunobiológicos que contêm:",
                options: {
                    A: "O microrganismo inteiro vivo.",
                    B: "O microrganismo inteiro morto.",
                    C: "Apenas fragmentos específicos (ex: proteínas ou polissacarídeos) do patógeno.",
                    D: "O material genético completo do vírus."
                },
                correct: "C",
                explanation: "Subunidade significa que a vacina não tem o patógeno inteiro, mas apenas partes dele (antígenos) que estimulam o sistema imune."
            },
            {
                id: 25,
                question: "A baixa cobertura vacinal pode acarretar o ressurgimento de doenças já controladas. Um exemplo recente desse fenômeno no Brasil foi a reintrodução do vírus:",
                options: {
                    A: "Varíola.",
                    B: "Poliomielite (tipo selvagem 2).",
                    C: "Sarampo.",
                    D: "Ebola."
                },
                correct: "C",
                explanation: "O Brasil perdeu o certificado de eliminação do Sarampo em 2019 devido à queda nas coberturas vacinais e reintrodução do vírus."
            },
            {
                id: 26,
                question: "Para recém-nascidos de mães portadoras de Hepatite B (HBsAg positivas), a conduta recomendada nas primeiras horas de vida é:",
                options: {
                    A: "Apenas a vacina contra Hepatite B.",
                    B: "Apenas a imunoglobulina humana anti-hepatite B.",
                    C: "Administração simultânea da vacina contra Hepatite B e da imunoglobulina específica.",
                    D: "Aguardar 6 meses para iniciar o esquema vacinal."
                },
                correct: "C",
                explanation: "Para prevenir a transmissão vertical, deve-se administrar tanto a vacina (imunização ativa) quanto a imunoglobulina (imunização passiva) em sítios diferentes."
            },
            {
                id: 27,
                question: "As vacinas contra rotavírus e poliomielite (VOP) são exemplos de vacinas administradas por via:",
                options: {
                    A: "Intramuscular.",
                    B: "Subcutânea.",
                    C: "Intradérmica.",
                    D: "Oral."
                },
                correct: "D",
                explanation: "Ambas são vacinas administradas pela boca (gotinha)."
            },
            {
                id: 28,
                question: "Qual faixa etária é o foco principal da vacinação contra o HPV no calendário nacional do SUS para meninas e meninos?",
                options: {
                    A: "Ao nascer.",
                    B: "15 a 24 anos.",
                    C: "9 a 14 anos.",
                    D: "Acima de 60 anos."
                },
                correct: "C",
                explanation: "O alvo principal são adolescentes antes do início da vida sexual. A faixa etária no SUS abrange meninas e meninos de 9 a 14 anos."
            },
            {
                id: 29,
                question: "O Tétano é prevenido através de vacinas que utilizam:",
                options: {
                    A: "Bactérias vivas atenuadas.",
                    B: "Toxóides (toxinas inativadas e modificadas).",
                    C: "Vírus inativados.",
                    D: "Polissacarídeos capsulares livres."
                },
                correct: "B",
                explanation: "A doença é causada pela toxina da bactéria, não pela bactéria em si. Portanto, a vacina usa o toxóide tetânico (toxina inativada)."
            },
            {
                id: 30,
                question: "A vacina Pentavalente no calendário infantil brasileiro protege contra:",
                options: {
                    A: "Difteria, Tétano, Coqueluche, Hepatite B e Haemophilus influenzae tipo b.",
                    B: "Sarampo, Caxumba, Rubéola, Varicela e Pólio.",
                    C: "Hepatite A, Hepatite B, Tétano, Febre Amarela e HPV.",
                    D: "Tuberculose, Hanseníase, Malária, Dengue e Zika."
                },
                correct: "A",
                explanation: "A vacina pentavalente celular combina a DTP (Difteria, Tétano, Pertussis) + Hepatite B + Hib."
            },
            {
                id: 31,
                question: "Sobre a transmissão da Hepatite A, é correto afirmar que ocorre predominantemente por via:",
                options: {
                    A: "Sexual e sanguínea.",
                    B: "Fecal-oral (água e alimentos contaminados).",
                    C: "Respiratória (gotículas de saliva).",
                    D: "Vetorial (picada de mosquito)."
                },
                correct: "B",
                explanation: "A Hepatite A é uma doença de transmissão entérica, ligada a condições de saneamento e higiene."
            },
            {
                id: 32,
                question: "'Hesitação vacinal' é um termo que descreve:",
                options: {
                    A: "A falta de vacinas nos postos de saúde.",
                    B: "O atraso na aceitação ou recusa das vacinas, apesar da disponibilidade dos serviços.",
                    C: "A demora do sistema imune em produzir anticorpos após a vacina.",
                    D: "A reação adversa grave imediata após a aplicação."
                },
                correct: "B",
                explanation: "Hesitação vacinal é o comportamento de demorar ou recusar a vacinação, mesmo quando as doses estão disponíveis."
            },
            {
                id: 33,
                question: "O estudo RV144, citado no material sobre HIV, demonstrou uma eficácia vacinal parcial de aproximadamente:",
                options: {
                    A: "95%.",
                    B: "80%.",
                    C: "31%.",
                    D: "0% (nenhuma eficácia)."
                },
                correct: "C",
                explanation: "O ensaio clínico RV144 na Tailândia foi um dos poucos a mostrar alguma eficácia, embora baixa (31%), contra o HIV."
            },
            {
                id: 34,
                question: "A vacina Tetraviral substitui uma dose da Tríplice Viral e acrescenta proteção contra:",
                options: {
                    A: "Hepatite A.",
                    B: "Varicela (catapora).",
                    C: "Poliomielite.",
                    D: "Meningite C."
                },
                correct: "B",
                explanation: "Tetraviral = Sarampo, Caxumba, Rubéola (Tríplice) + Varicela."
            },
            {
                id: 35,
                question: "As vacinas inativadas geralmente exigem múltiplas doses ou reforços porque:",
                options: {
                    A: "São rapidamente eliminadas pela urina.",
                    B: "Não se replicam no hospedeiro, gerando um estímulo imunológico inicial mais fraco que as atenuadas.",
                    C: "Causam doença leve que interfere na imunidade.",
                    D: "São compostas apenas por água e adjuvantes."
                },
                correct: "B",
                explanation: "Como o agente está morto e não se multiplica, o estímulo ao sistema imune é menos intenso e persistente, exigindo doses de reforço para manter a proteção."
            },
            {
                id: 36,
                question: "A estratégia de 'Campanha' de vacinação difere da estratégia de 'Rotina' pois:",
                options: {
                    A: "Visa vacinar indiscriminadamente toda a população em um curto espaço de tempo para alcançar altas coberturas rapidamente.",
                    B: "Ocorre apenas dentro dos hospitais para pacientes internados.",
                    C: "Utiliza vacinas experimentais não aprovadas para rotina.",
                    D: "É focada exclusivamente em idosos."
                },
                correct: "A",
                explanation: "A rotina é contínua nos postos. A campanha é intensiva, num curto período (ex: Dia D), visando elevar rapidamente a cobertura vacinal."
            },
            {
                id: 37,
                question: "Qual dos seguintes profissionais integra os grupos prioritários para vacinação contra Influenza?",
                options: {
                    A: "Apenas médicos e enfermeiros.",
                    B: "Trabalhadores da saúde, professores e profissionais das forças de segurança.",
                    C: "Apenas profissionais que trabalham em UTI.",
                    D: "Profissionais de tecnologia da informação em home office."
                },
                correct: "B",
                explanation: "O Ministério da Saúde define grupos prioritários com base no risco de exposição e transmissão, incluindo saúde, educação e segurança."
            },
            {
                id: 38,
                question: "O principal objetivo da Vigilância das Coberturas Vacinais é:",
                options: {
                    A: "Identificar áreas com baixas taxas de vacinação (bolsões de suscetíveis) para intervir e prevenir surtos.",
                    B: "Punir as famílias que não vacinam seus filhos.",
                    C: "Testar novas vacinas na população sem consentimento.",
                    D: "Reduzir o número de salas de vacina para economizar recursos."
                },
                correct: "A",
                explanation: "Monitorar a cobertura permite saber onde a população está desprotegida e agir antes que ocorram surtos."
            },
            {
                id: 39,
                question: "O vírus Influenza A é conhecido por causar:",
                options: {
                    A: "Apenas resfriados leves sem febre.",
                    B: "Grandes pandemias devido à sua capacidade de mudança antigênica (shift).",
                    C: "Infecções crônicas no fígado.",
                    D: "Verrugas genitais."
                },
                correct: "B",
                explanation: "O Influenza A é o único capaz de realizar 'antigenic shift' (mudança brusca), o que pode gerar vírus novos para os quais ninguém tem imunidade, causando pandemias."
            },
            {
                id: 40,
                question: "A vacina BCG, embora não citada detalhadamente como viral no texto, é um exemplo clássico de vacina:",
                options: {
                    A: "Atenuada bacteriana.",
                    B: "Inativada viral.",
                    C: "De RNA mensageiro.",
                    D: "De vetor viral."
                },
                correct: "A",
                explanation: "A BCG (Bacilo Calmette-Guérin) previne formas graves de tuberculose e é feita de bactérias vivas atenuadas."
            },
            {
                id: 41,
                question: "A contraindicação absoluta para vacinação com vírus vivo em gestantes se deve ao risco teórico de:",
                options: {
                    A: "A mãe desenvolver alergia ao ovo.",
                    B: "Transmissão do vírus vacinal ao feto, causando danos teratogênicos.",
                    C: "A vacina não funcionar devido aos hormônios da gravidez.",
                    D: "Causar diabetes gestacional."
                },
                correct: "B",
                explanation: "Vacinas vivas (como Tríplice Viral) podem, teoricamente, cruzar a placenta e infectar o feto, causando malformações."
            },
            {
                id: 42,
                question: "No Brasil, a vacina contra a Dengue (Qdenga) no SUS foi inicialmente priorizada para qual faixa etária devido à capacidade de fornecimento e epidemiologia?",
                options: {
                    A: "Idosos acima de 80 anos.",
                    B: "Crianças e adolescentes de 10 a 14 anos.",
                    C: "Bebês menores de 1 ano.",
                    D: "Apenas gestantes."
                },
                correct: "B",
                explanation: "Devido à limitação de doses e dados epidemiológicos de hospitalização, o MS priorizou a faixa de 10 a 14 anos na introdução da vacina."
            },
            {
                id: 43,
                question: "O termo 'imunobiológico' engloba:",
                options: {
                    A: "Apenas vacinas.",
                    B: "Apenas soros e imunoglobulinas.",
                    C: "Vacinas, soros imununes e imunoglobulinas.",
                    D: "Antibióticos e antivirais."
                },
                correct: "C",
                explanation: "Imunobiológico é o termo técnico que abrange todos os produtos usados para imunização (ativa ou passiva)."
            },
            {
                id: 44,
                question: "Uma das desvantagens das vacinas de RNA (mRNA) mencionada no material é:",
                options: {
                    A: "A necessidade de armazenamento em temperaturas muito baixas (ultrafreezers).",
                    B: "O alto risco de causar a doença completa no paciente.",
                    C: "A impossibilidade de produção em larga escala.",
                    D: "A presença de conservantes à base de mercúrio."
                },
                correct: "A",
                explanation: "O RNA é uma molécula instável, exigindo cadeia de frio rigorosa (muitas vezes temperaturas negativas extremas) para conservação."
            },
            {
                id: 45,
                question: "A vacina contra a Varicela (catapora) pode ser encontrada no SUS sob a forma de:",
                options: {
                    A: "Vacina monovalente apenas.",
                    B: "Componente da vacina Tetraviral.",
                    C: "Componente da vacina Pentavalente.",
                    D: "Componente da vacina contra Influenza."
                },
                correct: "B",
                explanation: "No SUS, a proteção contra varicela é administrada principalmente através da vacina Tetraviral (aos 15 meses) ou monovalente em situações específicas."
            },
            {
                id: 46,
                question: "A 'Mortalidade' por uma doença específica é calculada relacionando:",
                options: {
                    A: "O número de óbitos pela doença com a população total exposta.",
                    B: "O número de doentes com o número de curados.",
                    C: "O número de vacinados com o número de não vacinados.",
                    D: "O número de internações com o número de consultas."
                },
                correct: "A",
                explanation: "A taxa de mortalidade mede o risco de morrer pela doença na população geral (Óbitos / População Total)."
            },
            {
                id: 47,
                question: "Os soros heterólogos (ex: soro antiofídico ou antirrábico) são produzidos geralmente em:",
                options: {
                    A: "Humanos voluntários.",
                    B: "Animais (como cavalos), que são imunizados para produzir anticorpos.",
                    C: "Bactérias transgênicas.",
                    D: "Plantas geneticamente modificadas."
                },
                correct: "B",
                explanation: "Animais de grande porte (equinos) são estimulados com o antígeno e seus anticorpos são purificados para criar o soro."
            },
            {
                id: 48,
                question: "A Rubéola é uma doença viral que preocupa a saúde pública principalmente devido ao risco de:",
                options: {
                    A: "Síndrome da Rubéola Congênita (má-formação fetal) se adquirida na gestação.",
                    B: "Evolução para câncer de fígado.",
                    C: "Paralisia flácida permanente.",
                    D: "Hemorragias graves."
                },
                correct: "A",
                explanation: "A infecção em crianças é leve, mas em gestantes pode causar surdez, catarata e problemas cardíacos no bebê (Síndrome da Rubéola Congênita)."
            },
            {
                id: 49,
                question: "O esquema vacinal completo da vacina HPV para crianças e adolescentes no PNI consiste atualmente (conforme material ou padrão recente) em:",
                options: {
                    A: "Uma dose única.",
                    B: "Três doses com intervalo de 6 meses.",
                    C: "Duas doses com intervalo de 6 meses.",
                    D: "Dose mensal por um ano."
                },
                correct: "A",
                explanation: "Em 2024, o Brasil adotou o esquema de DOSE ÚNICA para a vacina HPV na faixa de 9 a 14 anos, seguindo recomendação da OMS."
            },
            {
                id: 50,
                question: "A vigilância de eventos adversos pós-vacinação é essencial para:",
                options: {
                    A: "Garantir a segurança e manter a confiança da população no programa de imunização.",
                    B: "Provar que as vacinas não funcionam.",
                    C: "Aumentar o custo das vacinas.",
                    D: "Desestimular a vacinação em massa."
                },
                correct: "A",
                explanation: "Monitorar efeitos colaterais (farmacovigilância) é vital para garantir que os benefícios continuem superando os riscos e para manter a credibilidade do sistema."
            }
        ];

        // --- LÓGICA DO APP ---
        
        // Timer
        let seconds = 0;
        let intervalId;
        function startTimer() {
            intervalId = setInterval(() => {
                seconds++;
                const min = Math.floor(seconds / 60).toString().padStart(2, '0');
                const sec = (seconds % 60).toString().padStart(2, '0');
                document.getElementById('timer').innerText = `${min}:${sec}`;
            }, 1000);
        }

        // Renderizar Questões
        function renderQuiz() {
            const form = document.getElementById('quiz-form');
            form.innerHTML = questionsData.map((q, index) => `
                <div class="bg-white rounded-lg shadow-sm p-6 mb-4 border border-gray-100 transition hover:shadow-md" id="question-card-${q.id}">
                    <div class="flex items-start gap-4 mb-4">
                        <span class="bg-blue-100 text-blue-800 text-sm font-bold px-3 py-1 rounded-full flex-shrink-0">
                            Questão ${index + 1}
                        </span>
                        <h3 class="text-lg font-medium text-gray-800 leading-snug pt-1">${q.question}</h3>
                    </div>
                    
                    <div class="space-y-3 ml-2 md:ml-12">
                        ${Object.entries(q.options).map(([key, value]) => `
                            <div class="relative">
                                <input type="radio" name="q${q.id}" id="q${q.id}-${key}" value="${key}" class="option-radio peer hidden">
                                <label for="q${q.id}-${key}" class="option-label block w-full text-left p-4 rounded-lg border border-gray-200 cursor-pointer hover:bg-gray-50 peer-checked:ring-2 peer-checked:ring-blue-500">
                                    <span class="font-bold text-gray-500 mr-2">${key})</span> ${value}
                                </label>
                            </div>
                        `).join('')}
                    </div>

                    <!-- Explicação (Oculta inicialmente) -->
                    <div id="explanation-${q.id}" class="hidden mt-4 p-4 bg-blue-50 rounded-lg border-l-4 border-blue-500 text-sm text-gray-700 animate-fade-in">
                        <p class="font-bold text-blue-900 mb-1">💡 Comentário:</p>
                        ${q.explanation}
                    </div>
                </div>
            `).join('');
            startTimer();
        }

        // Corrigir Simulado
        function submitQuiz() {
            clearInterval(intervalId);
            let score = 0;
            let answered = 0;

            questionsData.forEach(q => {
                const selected = document.querySelector(`input[name="q${q.id}"]:checked`);
                const card = document.getElementById(`question-card-${q.id}`);
                const explanation = document.getElementById(`explanation-${q.id}`);
                
                // Remover estilos anteriores
                card.querySelectorAll('.option-label').forEach(el => {
                    el.classList.remove('correct-answer', 'wrong-answer');
                });

                // Lógica de Correção Visual
                const correctInput = document.getElementById(`q${q.id}-${q.correct}`);
                if (correctInput) {
                    const correctLabel = document.querySelector(`label[for="q${q.id}-${q.correct}"]`);
                    correctLabel.classList.add('correct-answer'); // Sempre destaca a correta em verde
                }

                if (selected) {
                    answered++;
                    if (selected.value === q.correct) {
                        score++;
                    } else {
                        // Se errou, pinta a selecionada de vermelho
                        const selectedLabel = document.querySelector(`label[for="${selected.id}"]`);
                        selectedLabel.classList.add('wrong-answer');
                    }
                }

                // Mostrar explicação
                explanation.classList.remove('hidden');
            });

            // Exibir Resultado
            const percentage = Math.round((score / questionsData.length) * 100);
            document.getElementById('score-display').innerText = `${percentage}%`;
            document.getElementById('score-detail').innerText = `Você acertou ${score} de ${questionsData.length} questões.`;
            
            // Ícone dinâmico
            const iconContainer = document.getElementById('icon-container');
            if(percentage >= 70) {
                 iconContainer.classList.remove('bg-red-100');
                 iconContainer.classList.add('bg-green-100');
                 iconContainer.innerHTML = `<svg class="h-8 w-8 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>`;
            } else {
                 iconContainer.classList.remove('bg-green-100');
                 iconContainer.classList.add('bg-red-100');
                 iconContainer.innerHTML = `<svg class="h-8 w-8 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>`;
            }

            const modal = document.getElementById('result-modal');
            modal.classList.remove('hidden');
            modal.classList.add('flex');
            
            // Scroll para o topo
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function closeModal() {
            document.getElementById('result-modal').classList.add('hidden');
            document.getElementById('result-modal').classList.remove('flex');
        }

        // Inicializar
        renderQuiz();

    </script>
</body>
</html>
