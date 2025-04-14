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
    try:
        # Ambil payload sebagai JSON
        data = request.get_json(force=True)
    except Exception as e:
        data = request.form.to_dict()

    # Ambil data dengan kunci-kunci yang kita set di Pine Script
    pair   = data.get('pair', 'N/A')
    signal = data.get('signal', 'N/A')
    entry  = data.get('entry', 'N/A')
    sl     = data.get('sl', 'N/A')
    tp1    = data.get('tp1', 'N/A')
    tp2    = data.get('tp2', 'N/A')
    tp3    = data.get('tp3', 'N/A')
    tp4    = data.get('tp4', 'N/A')
    tp5    = data.get('tp5', 'N/A')
    target = data.get('target', 'N/A')

    # Susun pesan notifikasi ke Telegram
    message = f"""🚨 Sinyal Baru dari TradingView!

🔁 Pair: {pair}
📈 Signal: {signal}
💰 Entry: {entry}
🛡️ SL: {sl}
🎯 TP1: {tp1}
🎯 TP2: {tp2}
🎯 TP3: {tp3}
🎯 TP4: {tp4}
🎯 TP5: {tp5}
🚀 To The Moon: {target}"""

    send_telegram(message)
    return 'Pesan dikirim ke Telegram!', 200

def send_telegram(msg):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': msg}
    requests.post(url, data=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
