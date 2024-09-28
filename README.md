# Spoti-Ninho 🎵

## Descrição

**Spoti-Ninho** é um player de música desenvolvido em Python, com interfaces gráficas criadas em **PyQt6** e reprodução em **PySimpleGUI**. O projeto também inclui um sistema de gerenciamento de usuários e playlists utilizando SQL, além de funções para criar playlists, ver o histórico de reprodução e escutar suas músicas favoritas de forma simples e eficiente.

## Funcionalidades Principais

- **Gerenciamento de Usuários (SQL)**: Cadastro, login e remoção de usuários.
- **Playlists Personalizadas**: Criação, visualização e reprodução de playlists.
- **Histórico de Reprodução**: Visualize suas faixas reproduzidas.
- **Player de Música Completo**: Reprodução, pausa, retroceder e avançar faixas.
- **Informações das Faixas**: Exibição do nome da música, artista e capa do álbum.

## Estrutura do Projeto

- **`conexao.py`**: Gerencia a comunicação com o banco de dados SQL.
- **`interface.py`**: Interface do player musical feita em PySimpleGUI.
- **`menuQT.py`**: Gerencia os menus e interações com o usuário via PyQt6.
- **`player.py`**: Lida com a reprodução das faixas usando Pygame.
- **`setup.py`**: Configura o banco de dados (MySQL Workbench).

## Interfaces Gráficas

### Menu Spoti-Ninho:
- **Menu Spoti-Ninho**: Para cadastro, login e remoção de usuários.
- **Menu Usuário**: Acesso às funcionalidades de playlists e histórico, além do player de música.

### Menu do Usuário:
- **Playlists**: Criação e gerenciamento.
- **Histórico**: Acompanhe suas faixas reproduzidas.
- **Player**: Acesso ao player PySimpleGUI para tocar as playlists.

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
4. Execute o menu principal:
   ```bash
   python menuQT.py
   ```

## Contribuição

Contribuições são sempre bem-vindas! Se desejar sugerir melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request. Para grandes alterações, por favor, abra uma issue antes para discutirmos sua proposta.