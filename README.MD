# Calendar RPA

## Descrição
O projeto Calendar RPA é uma automação de processos robóticos (RPA) desenvolvida para gerenciar eventos de calendário do Google. Ele permite a leitura de eventos em um calendário digital de forma automatizada e o envio de mensagens com a lista de eventos pelo WhatsApp usando o serviço do Twilio.

## Funcionalidades
- **Leitura de Eventos**: Automatiza a leitura de eventos existentes no calendário.
- **Notificações**: Envia notificações sobre eventos lidos.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal utilizada no desenvolvimento do RPA.
- **Google Calendar API**: API utilizada para integração com o Google Calendar.
- **Twilio**: API de serviço de envio de mensagens via WhatsApp

## Integração com Twilio

Este projeto também utiliza o serviço Twilio para enviar notificações via SMS sobre eventos do calendário.

### Configuração do Twilio

1. Crie uma conta no [Twilio](https://www.twilio.com/).
2. Obtenha seu `Account SID` e `Auth Token` no painel do Twilio.

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
1. Configure as credenciais da API do Google Calendar e baixe o `credentials.json` na raiz do projeto.
2. Durante a primeira execução o serviço solicitará logon usando o OAuth do Google, portanto é necessário configurar no Google Console a liberação do seu domínio.
2. Certifique-se de que o arquivo `.env` está no diretório raiz do projeto com as seguintes chaves:
- TWILIO_ACCOUNT_SID: `<SID da conta do TWILIO que será usada>`
- TWILIO_AUTH_TOKEN: `<Token fornecido pela API>`
- TWILIO_WHATSAPP_NUMBER: `<Número sandbox do Twilio, aparece quando você receber a primeira mensagem do serviço>`
- MY_WHATSAPP_NUMBER: `<seu número WhatsApp>`

3. Crie uma conta no Twilio, siga as informações no site para habilitar o número de WhatsApp desejado
para receber as mensagens.

## Uso
1. Execute o script principal:
  ```bash
  python main.py
  ```
2. O Script acessará o calendário primário utilizado e você receberá a lista de eventos do dia.

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
Para mais informações, entre em contato com [renatomariner@gmail.com](mailto:renatomariner@gmail.com).

