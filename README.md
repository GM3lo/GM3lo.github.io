# Plataforma de Estudos - Educational Platform

Uma plataforma educacional completa em português para gerenciamento de simulados, videoaulas e materiais complementares com painel administrativo protegido por senha.

## 📋 Funcionalidades

- **Simulados** - Quizzes interativos sobre tópicos médicos/saúde
- **Videoaulas** - Gestão de aulas em vídeo
- **Materiais Complementares** - Recursos educacionais adicionais
- **Painel Admin** - Interface protegida para upload e gerenciamento de arquivos
- **Design Responsivo** - Interface moderna com tema roxo e escuro

## 🛠️ Stack Tecnológico

- **Backend**: Python 3.11 com Flask
- **Banco de Dados**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript (templates Jinja2)
- **Armazenamento**: Pasta uploads local
- **Produção**: Gunicorn

## 📁 Estrutura do Projeto

```
.
├── app.py                           # Aplicação Flask principal
├── database.db                      # Banco de dados SQLite
├── uploads/                         # Pasta de armazenamento de arquivos
├── templates/
│   ├── index.html                   # Página inicial com 3 abas
│   ├── admin.html                   # Dashboard de administração
│   └── admin_login.html             # Página de login
├── static/                          # Arquivos CSS e JS estáticos
├── simulado_vigilancia.html         # Quiz com 50 questões (legacy)
└── README.md                        # Este arquivo
```

## ⚙️ Variáveis de Ambiente

### Obrigatórias
- `ADMIN_PASSWORD` - Senha para acesso ao painel administrativo

### Opcionais
- `SECRET_KEY` - Chave secreta do Flask (gerada automaticamente se não definida)

## 🚀 Como Executar

### Desenvolvimento Local

```bash
python app.py
```

O servidor Flask será iniciado em `http://0.0.0.0:5000` com:
- Modo debug ativado
- Cache desabilitado
- Banco de dados SQLite auto-inicializado

## 📊 Esquema do Banco de Dados

```sql
CREATE TABLE files (
    id TEXT PRIMARY KEY,
    filename TEXT NOT NULL,
    original_name TEXT NOT NULL,
    category TEXT NOT NULL,          -- 'simulado', 'aula', ou 'material'
    title TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🔐 Segurança

- Painel administrativo protegido por senha
- Senhas armazenadas em variáveis de ambiente
- Suporte para upload restrito de tipos de arquivo
- Desabilitação de cache para conteúdo dinâmico
- IDs de arquivo aleatórios (UUID)

## 📥 Tipos de Arquivo Suportados

PDF, DOC, DOCX, PPT, PPTX, TXT, MP4, MP3, JPG, JPEG, PNG, GIF, HTML

## 🎯 Rotas da API

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página inicial |
| `/admin/login` | GET, POST | Login do admin |
| `/admin/logout` | GET | Logout do admin |
| `/admin` | GET | Dashboard do admin |
| `/admin/upload` | POST | Upload de arquivo |
| `/admin/delete/<file_id>` | POST | Deletar arquivo |
| `/uploads/<filename>` | GET | Download de arquivo |

## 👤 Painel Administrativo

Acesse o painel clicando no botão "Admin" no canto superior direito da página.

- Upload de arquivos com seleção de categoria
- Visualização e gerenciamento de arquivos
- Adição de título e descrição
- Função de exclusão de arquivos

## 📝 Desenvolvimento

Para contribuir com o projeto:

1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Configure as variáveis de ambiente
4. Inicie o servidor em modo desenvolvimento
5. Faça suas alterações
6. Envie um pull request

## 📄 Licença

MIT License - veja o arquivo LICENSE para detalhes.

## 📧 Contato

Para dúvidas ou sugestões sobre a plataforma, entre em contato através do repositório.

---

**Última atualização**: Novembro de 2025
