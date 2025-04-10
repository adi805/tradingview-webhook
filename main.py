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

    # Ambil semua data dari payload TradingView
    pair = data.get('pair', 'N/A')
    signal = data.get('signal', 'N/A')
    entry = data.get('entry', 'N/A')
    tp = data.get('tp', 'N/A')
    sl = data.get('sl', 'N/A')

    # Buat pesan format yang rapi
    message = f"""🚨 Sinyal Baru dari TradingView!

🔁 Pair: {pair}
📉 Sinyal: {signal}
💰 Entry: {entry}
🎯 TP: {tp}
🛡️ SL: {sl}"""

    send_telegram(message)
    return 'Pesan dikirim ke Telegram!', 200


def send_telegram(msg):
    url = f'https://api.telegram.org/bot8165162109:AAEMmiaZRuBeAEgx_Tj6ouDLpSCg4R-nxcg/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': msg}
    requests.post(url, data=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    print("Webhook data received:", data)  # <- ini penting
    ...

