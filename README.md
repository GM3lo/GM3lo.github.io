# 📚 Plataforma de Estudos

Uma plataforma educacional em português com quizzes interativos, videoaulas e materiais complementares.

## 🚀 Recursos

- **Simulados**: Quizzes com 50 questões, timer e feedback detalhado
- **Videoaulas**: Integração com YouTube e links dinâmicos
- **Materiais Complementares**: Recursos adicionados pelo admin
- **Painel de Admin**: Gerenciar recursos protegido por senha

## 🔐 Acesso ao Admin

- URL: `/admin.html`
- Senha padrão: `admin123`

**Para alterar a senha**, edite o arquivo `admin.html` e procure por `DEFAULT_PASSWORD`.

## 📋 Como Adicionar Recursos

1. Clique no ícone ⚙️ (engrenagem) no canto superior direito
2. Faça login com a senha do admin
3. Preencha:
   - **Título**: Nome do recurso
   - **URL**: Link para o recurso
   - **Categoria**: Simulados, Videoaulas ou Materiais Complementares
   - **Descrição**: (opcional)
4. Clique em "Adicionar Recurso"
5. Os recursos aparecem automaticamente na aba correspondente

## 🌐 Acesso Online

Esta plataforma está hospedada no **GitHub Pages**. Para acessar:

1. Vá para as configurações do repositório
2. Vá para "Pages" (na seção "Code and automation")
3. Em "Source", selecione "Deploy from a branch"
4. Selecione a branch `main` e a pasta `/ (root)`
5. Clique em "Save"
6. Sua plataforma estará disponível em: `https://seu-usuario.github.io/seu-repositorio`

## 📁 Estrutura de Arquivos

```
├── index.html                    # Página principal
├── admin.html                    # Painel de administração
├── simulado_vigilancia.html      # Quiz de 50 questões
├── server.py                     # Servidor para desenvolvimento local
├── replit.md                     # Documentação técnica
└── README.md                     # Este arquivo
```

## 💾 Armazenamento de Dados

- Os recursos são salvos no **localStorage** do navegador
- Cada usuário tem seus próprios dados
- Os dados persitem mesmo após fechar o navegador
- Para compartilhar recursos entre usuários, um backend seria necessário

## 🛠️ Desenvolvimento Local

### Com Python

```bash
python3 server.py
```

Acesse em: `http://localhost:5000`

### Com Live Server (VSCode)

1. Instale a extensão "Live Server"
2. Clique com direito em `index.html`
3. Selecione "Open with Live Server"

## 📝 Quiz Disponível

**Simulado: Vigilância e PNI**
- 50 questões de múltipla escolha
- Tópicos: PNI, Vacinas, Vigilância Epidemiológica, Virologia
- Explicações detalhadas para cada resposta
- Timer para controlar o tempo

## 🔒 Segurança

⚠️ **Nota Importante**: Este é um sistema educacional básico. Para uso em produção com múltiplos administradores:

- Migre para um backend real (Node.js, Python, etc)
- Implemente autenticação adequada (OAuth, JWT)
- Use um banco de dados seguro
- Implemente HTTPS

## 📄 Licença

Este projeto é de código aberto. Sinta-se livre para usar, modificar e distribuir.

---

Desenvolvido com ❤️ para educação!
