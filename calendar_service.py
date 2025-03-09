import os
import pickle
from datetime import datetime, timedelta, timezone
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Escopo de acesso / leitura
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

# Arquivos de credenciais e token
CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.pickle"

def authenticate_google_calendar():
    '''
    Autentica no Google Calendar e retorna o serviço da API
    '''
    creds = None

    # Verifica se o arquivo credentials.json existe
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"ERRO: Arquivo {CREDENTIALS_FILE} não encontrado!")
        print(f"Por favor, baixe suas credenciais do Google Cloud Console e")
        print(f"salve como {CREDENTIALS_FILE} na pasta: {os.path.abspath('.')}")
        return None

    # Tenta carregar credenciais já salvas previamente
    if os.path.exists(TOKEN_FILE):
        try:
            with open(TOKEN_FILE, "rb") as token:
                creds = pickle.load(token)
            print("Token carregado com sucesso.")
        except Exception as e:
            print(f"Erro ao carregar token: {e}")
            creds = None

    # Se não houver credenciais válidas, solicita ao usuário login novamente
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
                print("Token atualizado com sucesso.")
            except Exception as e:
                print(f"Erro ao atualizar token: {e}")
                creds = None
        else:
            print("Iniciando fluxo de autenticação OAuth...")
            try:
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)

                # Use o método console, que não depende de URIs de redirecionamento
                # Descomente a linha abaixo se continuar tendo problemas com redirect_uri_mismatch
                # creds = flow.run_console()

                # Ou use porta fixa (recomendado)
                port = 8080
                print(f"Usando porta {port} para redirecionamento.")
                print(f"Certifique-se de que os seguintes URIs estão configurados no Google Cloud Console:")
                print(f"- http://localhost:{port}/")
                print(f"- http://127.0.0.1:{port}/")
                creds = flow.run_local_server(port=port)

                print("Autenticação concluída com sucesso.")
            except Exception as e:
                print(f"Erro no processo de autenticação: {e}")
                print("Dica: Se o erro for 'redirect_uri_mismatch', adicione os URIs sugeridos acima no Google Cloud Console.")
                raise

        # Salva as credenciais para uso futuro
        try:
            with open(TOKEN_FILE, "wb") as token:
                pickle.dump(creds, token)
            print(f"Token salvo em: {os.path.abspath(TOKEN_FILE)}")
        except Exception as e:
            print(f"Erro ao salvar token: {e}")

    try:
        return build("calendar", "v3", credentials=creds)
    except Exception as e:
        print(f"Erro ao criar serviço: {e}")
        return None

def get_today_events():
    '''
    Busca eventos do Google Calendar para o dia atual
    '''
    service = authenticate_google_calendar()

    if not service:
        return "Falha na autenticação. Verifique os erros acima."

    # Obtém Fuso horário
    local_tz = datetime.now().astimezone().tzinfo

    # Obtém inicio do dia atual no fuso horário local
    today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    today_start = today_start.astimezone(local_tz)

    # Obtém final do dia atual no fuso horário local
    today_end = today_start + timedelta(days=1)

    #  Converte para formato ISO
    time_min = today_start.isoformat()
    time_max = today_end.isoformat()
    print(f'Buscando eventos de {time_min} até {time_max}')

    try:
        events_result = service.events().list(
            calendarId="primary",
            timeMin=time_min,
            timeMax=time_max,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        ).execute()

        events = events_result.get("items", [])

        if not events:
            return "Nenhum evento encontrando para hoje."

        # Formata lista de eventos
        event_list = []
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            if "T" in start:
                # Assume formato ISO
                try:
                    start_dt = datetime.fromisoformat(start)
                    start = start_dt.strftime("%H:%M - %d/%m/%Y")
                except:
                    # Não conseguir analisar, mantém formato original
                    pass

            event_list.append(f"{event['summary']} - {start}")

        return "\n".join(event_list)
    except Exception as e:
        return f"Erro ao buscar eventos: {e}"

if __name__ == "__main__":
    print("Buscando eventos do calendário...")
    print("=" * 40)
    print(get_today_events())