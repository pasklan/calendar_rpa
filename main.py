from calendar_service import get_today_events
from whatsapp_service import send_whatsapp_message

# Obtém eventos do Google Calendar
events = get_today_events()

# Envia mensagem via Whatsapp
send_whatsapp_message(f"Bom dia! Eventos de hoje:\n{events}")