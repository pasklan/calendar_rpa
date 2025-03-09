# Calendar RPA

## Descrição
O projeto Calendar RPA é uma automação de processos robóticos (RPA) desenvolvida para gerenciar eventos de calendário. Ele permite a leitura de eventos em um calendário digital de forma automatizada.

## Funcionalidades
- **Leitura de Eventos**: Automatiza a leitura de eventos existentes no calendário.
- **Notificações**: Envia notificações sobre eventos lidos.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal utilizada no desenvolvimento do RPA.
- **Google Calendar API**: API utilizada para integração com o Google Calendar.

## Instalação
1. Clone o repositório:
  ```bash
  git clone https://github.com/seu-usuario/calendar_rpa.git
  ```
2. Navegue até o diretório do projeto:
  ```bash
  cd calendar_rpa
  ```
3. Crie um ambiente virtual:
  ```bash
  python -m venv venv
  ```
4. Ative o ambiente virtual:
  - No Windows:
    ```bash
    venv\Scripts\activate
    ```
  - No Linux/Mac:
    ```bash
    source venv/bin/activate
    ```
5. Instale as dependências:
  ```bash
  pip install -r requirements.txt
  ```

## Configuração
1. Configure as credenciais da API do Google Calendar no arquivo `config.json`.
2. Certifique-se de que o arquivo `config.json` está no diretório raiz do projeto.

## Uso
1. Execute o script principal:
  ```bash
  python main.py
  ```
2. Siga as instruções exibidas no terminal para interagir com o RPA.

## Contribuição
1. Faça um fork do projeto.
2. Crie uma nova branch:
  ```bash
  git checkout -b minha-nova-funcionalidade
  ```
3. Faça suas alterações e commit:
  ```bash
  git commit -m 'Adiciona nova funcionalidade'
  ```
4. Envie para o repositório remoto:
  ```bash
  git push origin minha-nova-funcionalidade
  ```
5. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato
Para mais informações, entre em contato com [seu-email@exemplo.com](mailto:seu-email@exemplo.com).

