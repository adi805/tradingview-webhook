from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '8165162109:AAEMmiaZRuBeAEgx_Tj6ouDLpSCg4R-nxcg'
CHAT_ID = '8195235297'

@app.route('/', methods=['GET'])
def home():
    return 'Webhook Aktif ✔️'

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    message = f"🚨 Sinyal Baru dari TradingView!\n\n{data.get('message', 'Tidak ada isi pesan')}"
    send_telegram(message)
    return 'Pesan dikirim ke Telegram!', 200

def send_telegram(msg):
    url = f'https://api.telegram.org/bot8165162109:AAEMmiaZRuBeAEgx_Tj6ouDLpSCg4R-nxcg/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': msg}
    requests.post(url, data=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
