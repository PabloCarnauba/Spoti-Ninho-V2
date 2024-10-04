# Spoti-Ninho

## Descrição

**Spoti-Ninho** é um player de música desenvolvido em Python, utilizando **PyQt6** para as interfaces gráficas, **PySimpleGUI** para a reprodução de músicas, e gerenciamento de usuários e playlists com **SQL**. O projeto oferece uma experiência completa de criação, gestão e reprodução de playlists de forma simples e intuitiva, tanto via interface gráfica quanto terminal.

## Funcionalidades Principais

- **Gerenciamento de Usuários (SQL)**: Cadastro, login e remoção de usuários.
- **Playlists Personalizadas**: Criação, visualização e reprodução de playlists.
- **Histórico de Reprodução**: Visualize suas faixas reproduzidas.
- **Player de Música Completo**: Reprodução, pausa, retroceder e avançar faixas.
- **Interação via Terminal**: Menu de usuário e menu principal no terminal.
- **Informações das Faixas**: Exibição do nome da música, artista e capa do álbum.

## Estrutura do Projeto

- **`conexao.py`**: Gerencia a comunicação com o banco de dados SQL.
- **`interface.py`**: Interface do player musical feita em PySimpleGUI.
- **`menuQT.py`**: Gerencia os menus e interações com o usuário via PyQt6.
- **`player.py`**: Lida com a reprodução das faixas usando Pygame.
- **`menu.py`**: Menu de interação via terminal.
- **`setup.py`**: Configura o banco de dados (MySQL Workbench).

## Menus

### Menu Spoti-Ninho (Terminal - `menu.py`):
- [1] CADASTRAR USUÁRIO
- [2] REMOVER USUÁRIO
- [3] ENTRAR
- [0] SAIR

### Menu Usuário (Terminal - `menu.py`):
- [1] CRIAR PLAYLIST
- [2] VER PLAYLISTS
- [3] VER HISTÓRICO
- [4] ESCUTAR PLAYLISTS
- [5] SAIR

### Menu Spoti-Ninho (Interface - `menuQT.py`):
- **Cadastro de Usuários**
- **Login de Usuários**
- **Remoção de Usuários**

> **Nota**: As funções de "Ver Playlists" e "Ver Histórico" ainda não foram implementadas na versão de interface gráfica (`menuQT.py`).

### Menu do Usuário (Interface):
- **Criação de Playlists**
- **Player de Música**: Acesso ao player PySimpleGUI para tocar as playlists.

## Requisitos

- **Python** 3.6 ou superior
- **PyQt6** para interfaces gráficas
- **PySimpleGUI** para o player de música
- **Pygame** para funcionalidades de reprodução
- **SQL** (MySQL Workbench)

## Instruções de Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/PabloCarnauba/Spoti-Ninho.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure o banco de dados:
   ```bash
   python setup.py
   ```
4. Execute o menu principal (PyQt6):
   ```bash
   python menuQT.py
   ```
5. Ou utilize a versão terminal:
   ```bash
   python menu.py
   ```

## Contribuição

Contribuições são bem-vindas! Para sugerir melhorias, abra uma issue ou envie um pull request. Para grandes alterações, por favor, abra uma issue para discutir sua proposta.